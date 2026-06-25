"""Exam preparation database module — Alman Bildung"""
import sqlite3
import json
import os

DB_PATH = os.environ.get("DB_PATH", "alman_bildung.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_exam_db():
    with get_conn() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS exam_providers (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL UNIQUE,
            title       TEXT NOT NULL,
            description_ru TEXT,
            description_uz TEXT,
            description_de TEXT,
            logo_emoji  TEXT DEFAULT '🎓',
            is_active   INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS exam_levels (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            provider_id      INTEGER NOT NULL REFERENCES exam_providers(id),
            level            TEXT NOT NULL,
            title            TEXT NOT NULL,
            description_ru   TEXT,
            description_uz   TEXT,
            description_de   TEXT,
            target_audience_ru TEXT,
            target_audience_uz TEXT,
            duration_total   TEXT,
            pass_score       INTEGER DEFAULT 60,
            exam_parts_json  TEXT DEFAULT '[]',
            tips_ru          TEXT,
            tips_uz          TEXT,
            is_active        INTEGER DEFAULT 1,
            UNIQUE(provider_id, level)
        );

        CREATE TABLE IF NOT EXISTS exam_sections (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            level_id        INTEGER NOT NULL REFERENCES exam_levels(id),
            type            TEXT NOT NULL,
            title_de        TEXT NOT NULL,
            title_ru        TEXT,
            title_uz        TEXT,
            description_ru  TEXT,
            description_uz  TEXT,
            duration_minutes INTEGER DEFAULT 20,
            sort_order      INTEGER DEFAULT 0,
            is_active       INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS exam_tasks (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            section_id      INTEGER NOT NULL REFERENCES exam_sections(id),
            title_de        TEXT NOT NULL,
            title_ru        TEXT,
            task_type       TEXT NOT NULL,
            instruction_de  TEXT,
            instruction_ru  TEXT,
            instruction_uz  TEXT,
            text_content    TEXT,
            extra_data      TEXT DEFAULT '{}',
            audio_url       TEXT,
            image_url       TEXT,
            is_active       INTEGER DEFAULT 1,
            sort_order      INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS exam_questions (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id         INTEGER NOT NULL REFERENCES exam_tasks(id),
            question_text   TEXT NOT NULL,
            question_type   TEXT NOT NULL DEFAULT 'choice',
            correct_answer  TEXT,
            explanation_ru  TEXT,
            explanation_uz  TEXT,
            points          INTEGER DEFAULT 1,
            sort_order      INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS exam_answer_options (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id     INTEGER NOT NULL REFERENCES exam_questions(id),
            option_text     TEXT NOT NULL,
            is_correct      INTEGER DEFAULT 0,
            sort_order      INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS user_exam_progress (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         INTEGER NOT NULL,
            provider        TEXT NOT NULL,
            level           TEXT NOT NULL,
            section_type    TEXT NOT NULL,
            completed_tasks INTEGER DEFAULT 0,
            total_tasks     INTEGER DEFAULT 0,
            average_score   REAL DEFAULT 0,
            last_activity   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, provider, level, section_type)
        );

        CREATE TABLE IF NOT EXISTS user_exam_attempts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         INTEGER NOT NULL,
            task_id         INTEGER NOT NULL,
            answers         TEXT DEFAULT '{}',
            score           INTEGER DEFAULT 0,
            max_score       INTEGER DEFAULT 0,
            percentage      REAL DEFAULT 0,
            passed          INTEGER DEFAULT 0,
            created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS writing_submissions (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         INTEGER NOT NULL,
            task_id         INTEGER NOT NULL,
            user_text       TEXT NOT NULL,
            ai_feedback     TEXT,
            score           REAL,
            created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)


# ── Providers ─────────────────────────────────────────────────────────────────

def get_providers() -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM exam_providers WHERE is_active=1 ORDER BY id"
        ).fetchall()
        return [dict(r) for r in rows]


def get_provider_by_name(name: str) -> dict | None:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT * FROM exam_providers WHERE name=? AND is_active=1", (name,)
        ).fetchone()
        return dict(row) if row else None


# ── Levels ────────────────────────────────────────────────────────────────────

def get_levels(provider_name: str) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT el.* FROM exam_levels el
            JOIN exam_providers ep ON ep.id = el.provider_id
            WHERE ep.name=? AND el.is_active=1
            ORDER BY CASE el.level WHEN 'A1' THEN 1 WHEN 'A2' THEN 2 WHEN 'B1' THEN 3 WHEN 'B2' THEN 4 ELSE 5 END
        """, (provider_name,)).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d['exam_parts'] = json.loads(d.get('exam_parts_json') or '[]')
            result.append(d)
        return result


def get_level_info(provider_name: str, level: str) -> dict | None:
    with get_conn() as conn:
        row = conn.execute("""
            SELECT el.*, ep.name as provider_name, ep.title as provider_title,
                   ep.logo_emoji as provider_emoji
            FROM exam_levels el
            JOIN exam_providers ep ON ep.id = el.provider_id
            WHERE ep.name=? AND el.level=? AND el.is_active=1
        """, (provider_name, level)).fetchone()
        if not row:
            return None
        d = dict(row)
        d['exam_parts'] = json.loads(d.get('exam_parts_json') or '[]')
        return d


# ── Sections ──────────────────────────────────────────────────────────────────

def get_sections(provider_name: str, level: str) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT es.* FROM exam_sections es
            JOIN exam_levels el ON el.id = es.level_id
            JOIN exam_providers ep ON ep.id = el.provider_id
            WHERE ep.name=? AND el.level=? AND es.is_active=1
            ORDER BY es.sort_order
        """, (provider_name, level)).fetchall()
        return [dict(r) for r in rows]


def get_section_by_type(provider_name: str, level: str, section_type: str) -> dict | None:
    with get_conn() as conn:
        row = conn.execute("""
            SELECT es.* FROM exam_sections es
            JOIN exam_levels el ON el.id = es.level_id
            JOIN exam_providers ep ON ep.id = el.provider_id
            WHERE ep.name=? AND el.level=? AND es.type=? AND es.is_active=1
        """, (provider_name, level, section_type)).fetchone()
        return dict(row) if row else None


# ── Tasks ─────────────────────────────────────────────────────────────────────

def get_tasks(section_id: int) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT * FROM exam_tasks WHERE section_id=? AND is_active=1
            ORDER BY sort_order
        """, (section_id,)).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d['extra'] = json.loads(d.get('extra_data') or '{}')
            result.append(d)
        return result


def get_task_full(task_id: int) -> dict | None:
    """Return task with all questions and answer options."""
    with get_conn() as conn:
        task_row = conn.execute(
            "SELECT * FROM exam_tasks WHERE id=? AND is_active=1", (task_id,)
        ).fetchone()
        if not task_row:
            return None
        task = dict(task_row)
        task['extra'] = json.loads(task.get('extra_data') or '{}')

        questions = conn.execute(
            "SELECT * FROM exam_questions WHERE task_id=? ORDER BY sort_order", (task_id,)
        ).fetchall()

        task['questions'] = []
        for q in questions:
            qd = dict(q)
            opts = conn.execute(
                "SELECT * FROM exam_answer_options WHERE question_id=? ORDER BY sort_order",
                (q['id'],)
            ).fetchall()
            qd['options'] = [dict(o) for o in opts]
            task['questions'].append(qd)

        return task


# ── Attempts ──────────────────────────────────────────────────────────────────

def save_attempt(user_id: int, task_id: int, answers: dict,
                 score: int, max_score: int) -> dict:
    pct = round((score / max_score * 100) if max_score > 0 else 0, 1)
    passed = 1 if pct >= 60 else 0
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO user_exam_attempts
              (user_id, task_id, answers, score, max_score, percentage, passed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, task_id, json.dumps(answers), score, max_score, pct, passed))
    return {"score": score, "max_score": max_score, "percentage": pct, "passed": bool(passed)}


def get_best_attempt(user_id: int, task_id: int) -> dict | None:
    with get_conn() as conn:
        row = conn.execute("""
            SELECT * FROM user_exam_attempts
            WHERE user_id=? AND task_id=?
            ORDER BY percentage DESC LIMIT 1
        """, (user_id, task_id)).fetchone()
        return dict(row) if row else None


def get_all_attempts_for_task(user_id: int, task_id: int) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT * FROM user_exam_attempts
            WHERE user_id=? AND task_id=?
            ORDER BY created_at DESC LIMIT 5
        """, (user_id, task_id)).fetchall()
        return [dict(r) for r in rows]


# ── Progress ──────────────────────────────────────────────────────────────────

def update_progress(user_id: int, provider: str, level: str,
                    section_type: str, new_pct: float):
    with get_conn() as conn:
        existing = conn.execute("""
            SELECT * FROM user_exam_progress
            WHERE user_id=? AND provider=? AND level=? AND section_type=?
        """, (user_id, provider, level, section_type)).fetchone()

        if existing:
            new_avg = max(existing['average_score'], new_pct)
            new_completed = existing['completed_tasks'] + 1
            conn.execute("""
                UPDATE user_exam_progress
                SET completed_tasks=?, average_score=?, last_activity=CURRENT_TIMESTAMP
                WHERE user_id=? AND provider=? AND level=? AND section_type=?
            """, (new_completed, new_avg, user_id, provider, level, section_type))
        else:
            conn.execute("""
                INSERT INTO user_exam_progress
                  (user_id, provider, level, section_type, completed_tasks, average_score)
                VALUES (?, ?, ?, ?, 1, ?)
            """, (user_id, provider, level, section_type, new_pct))


def get_progress(user_id: int, provider: str, level: str) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT * FROM user_exam_progress
            WHERE user_id=? AND provider=? AND level=?
        """, (user_id, provider, level)).fetchall()
        return [dict(r) for r in rows]


# ── Writing ───────────────────────────────────────────────────────────────────

def save_writing(user_id: int, task_id: int, user_text: str,
                 ai_feedback: str | None = None, score: float | None = None) -> int:
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO writing_submissions (user_id, task_id, user_text, ai_feedback, score)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, task_id, user_text, ai_feedback, score))
        return cur.lastrowid


def get_latest_writing(user_id: int, task_id: int) -> dict | None:
    with get_conn() as conn:
        row = conn.execute("""
            SELECT * FROM writing_submissions
            WHERE user_id=? AND task_id=?
            ORDER BY created_at DESC LIMIT 1
        """, (user_id, task_id)).fetchone()
        return dict(row) if row else None


def update_writing_feedback(submission_id: int, ai_feedback: str, score: float):
    with get_conn() as conn:
        conn.execute("""
            UPDATE writing_submissions
            SET ai_feedback=?, score=? WHERE id=?
        """, (ai_feedback, score, submission_id))
