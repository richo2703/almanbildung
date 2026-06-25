"""Alman Bildung Mini App — FastAPI Backend"""
import os
import hmac
import hashlib
import json
from urllib.parse import parse_qs, unquote

import httpx
from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

import database as db
import exam_db
from exam_router import router as exam_router
from content import (
    get_lesson, get_lesson_vocab, get_exercises,
    get_all_vocab, total_lessons, LEVELS_ORDER, CONTENT
)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

app = FastAPI(title="Alman Bildung API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db.init_db()
exam_db.init_exam_db()
app.include_router(exam_router)

# Auto-seed exam content on first run
if not exam_db.get_providers():
    try:
        import exam_seed
        exam_seed.run()
        print("✅ Exam content seeded automatically")
    except Exception as e:
        print(f"⚠️  Auto-seed failed: {e}")

# ── Telegram init data validation ────────────────────────────────────────────

def validate_init_data(init_data: str) -> dict:
    """Validate Telegram WebApp initData and return parsed user data."""
    if not BOT_TOKEN:
        # Dev mode: accept any init_data
        parsed = parse_qs(unquote(init_data))
        user_str = parsed.get("user", ["{}"])[0]
        return json.loads(user_str)

    parsed = {}
    data_check_string_parts = []
    for part in unquote(init_data).split("&"):
        key, _, value = part.partition("=")
        if key == "hash":
            received_hash = value
        else:
            data_check_string_parts.append(f"{key}={value}")
            parsed[key] = value

    data_check_string_parts.sort()
    data_check_string = "\n".join(data_check_string_parts)

    secret_key = hmac.new(b"WebAppData", BOT_TOKEN.encode(), hashlib.sha256).digest()
    computed_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    if not hmac.compare_digest(computed_hash, received_hash):
        raise HTTPException(status_code=401, detail="Invalid init data")

    user_str = parsed.get("user", "{}")
    return json.loads(user_str)


def get_user_id(x_init_data: str = Header(default="")) -> int:
    if not x_init_data:
        raise HTTPException(status_code=401, detail="Missing init data")
    user = validate_init_data(x_init_data)
    user_id = user.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="No user id")
    db.upsert_user(
        user_id,
        username=user.get("username", ""),
        full_name=f"{user.get('first_name','')} {user.get('last_name','')}".strip()
    )
    return int(user_id)


# ── Models ────────────────────────────────────────────────────────────────────

class LessonDonePayload(BaseModel):
    level: str
    lesson_id: int
    score: int = 0
    max_score: int = 0

class VocabPayload(BaseModel):
    level: str
    word_de: str
    known: bool

class TestResultPayload(BaseModel):
    level: str
    lesson_id: int
    score: int
    max_score: int

class LangPayload(BaseModel):
    lang: str


# ── TTS proxy ────────────────────────────────────────────────────────────────

@app.get("/api/tts")
async def api_tts(q: str = Query(..., max_length=200)):
    """Proxy Google Translate TTS — returns German mp3 audio."""
    url = (
        "https://translate.google.com/translate_tts"
        f"?ie=UTF-8&q={httpx.URL(q)}&tl=de&client=tw-ob&ttsspeed=0.85"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://translate.google.com/",
    }
    try:
        async with httpx.AsyncClient(timeout=8.0, follow_redirects=True) as client:
            resp = await client.get(url, headers=headers)
        if resp.status_code != 200:
            raise HTTPException(status_code=502, detail="TTS upstream error")
        return StreamingResponse(
            iter([resp.content]),
            media_type="audio/mpeg",
            headers={
                "Cache-Control": "public, max-age=86400",
                "Content-Length": str(len(resp.content)),
            }
        )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="TTS timeout")
    except Exception:
        raise HTTPException(status_code=502, detail="TTS unavailable")


# ── Content endpoints ─────────────────────────────────────────────────────────

@app.get("/api/levels")
def api_levels():
    result = []
    for level in LEVELS_ORDER:
        data = CONTENT.get(level, {})
        result.append({
            "id": level,
            "title_ru": data.get("title_ru", level),
            "title_uz": data.get("title_uz", level),
            "total_lessons": total_lessons(level),
        })
    return result


@app.get("/api/levels/{level}/lessons")
def api_lessons(level: str):
    data = CONTENT.get(level)
    if not data:
        raise HTTPException(status_code=404, detail="Level not found")
    lessons = []
    for l in data["lessons"]:
        merged = get_lesson(level, l["id"])
        lessons.append({
            "id": l["id"],
            "title_de": l["title_de"],
            "title_ru": l["title_ru"],
            "title_uz": l["title_uz"],
            "vocab_count": len(merged["vocab"]),
            "exercise_count": len(merged["exercises"]),
        })
    return lessons


@app.get("/api/levels/{level}/lessons/{lesson_id}")
def api_lesson(level: str, lesson_id: int):
    lesson = get_lesson(level, lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@app.get("/api/levels/{level}/lessons/{lesson_id}/vocab")
def api_vocab(level: str, lesson_id: int):
    vocab = get_lesson_vocab(level, lesson_id)
    if vocab is None:
        raise HTTPException(status_code=404, detail="Not found")
    return vocab


@app.get("/api/levels/{level}/lessons/{lesson_id}/exercises")
def api_exercises(level: str, lesson_id: int):
    exercises = get_exercises(level, lesson_id)
    if exercises is None:
        raise HTTPException(status_code=404, detail="Not found")
    return exercises


@app.get("/api/levels/{level}/vocab")
def api_level_vocab(level: str):
    return get_all_vocab(level)


# ── User / progress endpoints ─────────────────────────────────────────────────

@app.get("/api/me")
def api_me(x_init_data: str = Header(default="")):
    user_id = get_user_id(x_init_data)
    user = db.get_user(user_id)
    stats = db.get_stats(user_id)
    return {**user, **stats}


@app.post("/api/me/lang")
def api_set_lang(payload: LangPayload, x_init_data: str = Header(default="")):
    user_id = get_user_id(x_init_data)
    db.set_lang(user_id, payload.lang)
    return {"ok": True}


@app.get("/api/me/progress/{level}")
def api_level_progress(level: str, x_init_data: str = Header(default="")):
    user_id = get_user_id(x_init_data)
    lessons = db.get_lesson_progress(user_id, level)
    vocab = db.get_vocab_progress(user_id, level)
    return {"lessons": lessons, "vocab": vocab}


@app.post("/api/me/lesson-done")
def api_lesson_done(payload: LessonDonePayload, x_init_data: str = Header(default="")):
    user_id = get_user_id(x_init_data)
    db.mark_lesson(user_id, payload.level, payload.lesson_id, payload.score, payload.max_score)
    return {"ok": True, "xp_earned": 5}


@app.post("/api/me/vocab")
def api_mark_vocab(payload: VocabPayload, x_init_data: str = Header(default="")):
    user_id = get_user_id(x_init_data)
    db.mark_vocab(user_id, payload.level, payload.word_de, payload.known)
    return {"ok": True, "xp_earned": 2 if payload.known else 0}


@app.post("/api/me/test-result")
def api_test_result(payload: TestResultPayload, x_init_data: str = Header(default="")):
    user_id = get_user_id(x_init_data)
    db.save_test(user_id, payload.level, payload.lesson_id, payload.score, payload.max_score)
    return {"ok": True, "xp_earned": payload.score * 2}


# ── Serve frontend (after `npm run build`) ────────────────────────────────────

FRONTEND_DIST = os.path.join(os.path.dirname(__file__), "..", "frontend", "dist")

if os.path.isdir(FRONTEND_DIST):
    app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIST, "assets")), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    def serve_spa(full_path: str):
        return FileResponse(os.path.join(FRONTEND_DIST, "index.html"))
