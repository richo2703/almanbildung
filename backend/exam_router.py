"""Exam preparation API router — Alman Bildung
IMPORTANT: Route order matters in FastAPI.
Specific literal paths (tasks/, sections/, writing/, me/) MUST come
before wildcard paths (/{provider}/{level}) to prevent shadowing.
"""
import os
import hmac
import hashlib
import json
from urllib.parse import parse_qs, unquote

from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

import exam_db
import database as db

router = APIRouter(prefix="/api/exam", tags=["exam"])

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")


# ── Auth helper ───────────────────────────────────────────────────────────────

def _get_user_id(x_init_data: str) -> int:
    if not x_init_data:
        raise HTTPException(status_code=401, detail="Missing init data")

    if not BOT_TOKEN:
        parsed = parse_qs(unquote(x_init_data))
        user_str = parsed.get("user", ["{}"])[0]
        user = json.loads(user_str)
    else:
        parsed = {}
        parts = []
        received_hash = ""
        for part in unquote(x_init_data).split("&"):
            key, _, value = part.partition("=")
            if key == "hash":
                received_hash = value
            else:
                parts.append(f"{key}={value}")
                parsed[key] = value
        parts.sort()
        secret = hmac.new(b"WebAppData", BOT_TOKEN.encode(), hashlib.sha256).digest()
        computed = hmac.new(secret, "\n".join(parts).encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(computed, received_hash):
            raise HTTPException(status_code=401, detail="Invalid init data")
        user = json.loads(parsed.get("user", "{}"))

    uid = user.get("id")
    if not uid:
        raise HTTPException(status_code=401, detail="No user id")
    db.upsert_user(
        int(uid),
        username=user.get("username", ""),
        full_name=f"{user.get('first_name','')} {user.get('last_name','')}".strip()
    )
    return int(uid)


def _try_get_uid(x_init_data: str) -> int | None:
    """Get user id without raising — for optional auth endpoints."""
    try:
        return _get_user_id(x_init_data) if x_init_data else None
    except Exception:
        return None


# ── Pydantic models ───────────────────────────────────────────────────────────

class AttemptPayload(BaseModel):
    answers: dict   # {str(question_id): answer_text}

class WritingSubmitPayload(BaseModel):
    task_id: int
    user_text: str


# ══════════════════════════════════════════════════════════════════════════════
# SPECIFIC routes first — BEFORE any wildcard routes
# ══════════════════════════════════════════════════════════════════════════════

# ── Providers (literal prefix "providers") ────────────────────────────────────

@router.get("/providers")
def get_providers():
    return exam_db.get_providers()


@router.get("/providers/{provider_name}")
def get_provider(provider_name: str):
    p = exam_db.get_provider_by_name(provider_name)
    if not p:
        raise HTTPException(404, "Provider not found")
    return p


# ── Sections tasks (literal prefix "sections") ────────────────────────────────

@router.get("/sections/{section_id}/tasks")
def get_tasks(section_id: int, x_init_data: str = Header(default="")):
    tasks = exam_db.get_tasks(section_id)
    uid = _try_get_uid(x_init_data)
    if uid:
        for t in tasks:
            t['best_attempt'] = exam_db.get_best_attempt(uid, t['id'])
    return tasks


# ── Tasks (literal prefix "tasks") ────────────────────────────────────────────

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = exam_db.get_task_full(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    # Hide correct answers from client
    for q in task.get('questions', []):
        for opt in q.get('options', []):
            opt.pop('is_correct', None)
    return task


@router.post("/tasks/{task_id}/attempt")
def submit_attempt(task_id: int, payload: AttemptPayload,
                   x_init_data: str = Header(default="")):
    uid = _get_user_id(x_init_data)
    task = exam_db.get_task_full(task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    score = 0
    max_score = 0
    question_results = []

    for q in task['questions']:
        max_score += q['points']
        user_answer = payload.answers.get(str(q['id']), "")
        correct_opt = next((o for o in q['options'] if o.get('is_correct')), None)
        correct_text = correct_opt['option_text'] if correct_opt else q.get('correct_answer', '')
        is_correct = user_answer.strip().lower() == correct_text.strip().lower()
        if is_correct:
            score += q['points']
        question_results.append({
            "question_id": q['id'],
            "question_text": q['question_text'],
            "user_answer": user_answer,
            "correct_answer": correct_text,
            "is_correct": is_correct,
            "explanation_ru": q.get('explanation_ru', ''),
            "explanation_uz": q.get('explanation_uz', ''),
        })

    result = exam_db.save_attempt(uid, task_id, payload.answers, score, max_score)
    result['question_results'] = question_results

    # Update section progress
    conn = exam_db.get_conn()
    section = conn.execute(
        "SELECT es.type, el.level, ep.name as pname "
        "FROM exam_sections es "
        "JOIN exam_tasks et ON et.section_id = es.id "
        "JOIN exam_levels el ON el.id = es.level_id "
        "JOIN exam_providers ep ON ep.id = el.provider_id "
        "WHERE et.id=?", (task_id,)
    ).fetchone()
    conn.close()
    if section:
        exam_db.update_progress(
            uid, section['pname'], section['level'],
            section['type'], result['percentage']
        )
    return result


# ── Progress (literal prefix "me") ────────────────────────────────────────────

@router.get("/me/{provider_name}/{level}/progress")
def get_my_progress(provider_name: str, level: str,
                    x_init_data: str = Header(default="")):
    uid = _get_user_id(x_init_data)
    progress = exam_db.get_progress(uid, provider_name, level)
    sections = exam_db.get_sections(provider_name, level)

    result = {}
    for section in sections:
        tasks = exam_db.get_tasks(section['id'])
        prog = next((p for p in progress if p['section_type'] == section['type']), None)
        result[section['type']] = {
            "title_de": section['title_de'],
            "title_ru": section.get('title_ru'),
            "title_uz": section.get('title_uz'),
            "total_tasks": len(tasks),
            "completed_tasks": prog['completed_tasks'] if prog else 0,
            "average_score": prog['average_score'] if prog else 0,
        }
    return result


# ── Writing (literal prefix "writing") ────────────────────────────────────────

@router.post("/writing/submit")
def submit_writing(payload: WritingSubmitPayload,
                   x_init_data: str = Header(default="")):
    uid = _get_user_id(x_init_data)
    task = exam_db.get_task_full(payload.task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    sub_id = exam_db.save_writing(uid, payload.task_id, payload.user_text)

    extra = task.get('extra') or {}
    model_answer = extra.get('model_answer', '')
    checklist = extra.get('checklist', [])
    redemittel = extra.get('redemittel', [])

    conn = exam_db.get_conn()
    section = conn.execute(
        "SELECT es.type, el.level, ep.name as pname "
        "FROM exam_sections es "
        "JOIN exam_tasks et ON et.section_id = es.id "
        "JOIN exam_levels el ON el.id = es.level_id "
        "JOIN exam_providers ep ON ep.id = el.provider_id "
        "WHERE et.id=?", (payload.task_id,)
    ).fetchone()
    conn.close()
    if section:
        exam_db.update_progress(uid, section['pname'], section['level'], section['type'], 70.0)

    return {
        "submission_id": sub_id,
        "model_answer": model_answer,
        "checklist": checklist,
        "redemittel": redemittel,
        "ai_available": False,
        "message": "Текст сохранён. AI-проверка будет доступна в следующей версии.",
    }


@router.get("/writing/{task_id}/latest")
def get_latest_writing(task_id: int, x_init_data: str = Header(default="")):
    uid = _get_user_id(x_init_data)
    return exam_db.get_latest_writing(uid, task_id) or {}


# ══════════════════════════════════════════════════════════════════════════════
# WILDCARD routes last — these would shadow specific paths if placed above
# ══════════════════════════════════════════════════════════════════════════════

@router.get("/{provider_name}/levels")
def get_levels(provider_name: str):
    levels = exam_db.get_levels(provider_name)
    if not levels:
        raise HTTPException(404, "No levels found")
    return levels


@router.get("/{provider_name}/{level}/sections/{section_type}")
def get_section(provider_name: str, level: str, section_type: str):
    s = exam_db.get_section_by_type(provider_name, level, section_type)
    if not s:
        raise HTTPException(404, "Section not found")
    return s


@router.get("/{provider_name}/{level}/sections")
def get_sections(provider_name: str, level: str):
    return exam_db.get_sections(provider_name, level)


@router.get("/{provider_name}/{level}")
def get_level_info(provider_name: str, level: str):
    info = exam_db.get_level_info(provider_name, level)
    if not info:
        raise HTTPException(404, "Level not found")
    return info
