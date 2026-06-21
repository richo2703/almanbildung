"""Database layer for Alman Bildung Mini App"""
import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "alman_bildung.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER PRIMARY KEY,
            username    TEXT,
            full_name   TEXT,
            lang        TEXT DEFAULT 'ru',
            xp          INTEGER DEFAULT 0,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS progress (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            level       TEXT NOT NULL,
            lesson_id   INTEGER NOT NULL,
            completed   INTEGER DEFAULT 0,
            score       INTEGER DEFAULT 0,
            max_score   INTEGER DEFAULT 0,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, level, lesson_id)
        );

        CREATE TABLE IF NOT EXISTS vocab_progress (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            level       TEXT NOT NULL,
            word_de     TEXT NOT NULL,
            known       INTEGER DEFAULT 0,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, level, word_de)
        );

        CREATE TABLE IF NOT EXISTS test_results (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            level       TEXT NOT NULL,
            lesson_id   INTEGER NOT NULL,
            score       INTEGER NOT NULL,
            max_score   INTEGER NOT NULL,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)


def upsert_user(user_id: int, username: str = "", full_name: str = ""):
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO users (user_id, username, full_name)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                username = excluded.username,
                full_name = excluded.full_name
        """, (user_id, username or "", full_name or ""))


def get_user(user_id: int) -> dict | None:
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
        return dict(row) if row else None


def set_lang(user_id: int, lang: str):
    with get_conn() as conn:
        conn.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, user_id))


def add_xp(user_id: int, amount: int):
    with get_conn() as conn:
        conn.execute("UPDATE users SET xp = xp + ? WHERE user_id=?", (amount, user_id))


def mark_lesson(user_id: int, level: str, lesson_id: int, score: int = 0, max_score: int = 0):
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO progress (user_id, level, lesson_id, completed, score, max_score, updated_at)
            VALUES (?, ?, ?, 1, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, level, lesson_id) DO UPDATE SET
                completed = 1,
                score = MAX(score, excluded.score),
                max_score = excluded.max_score,
                updated_at = CURRENT_TIMESTAMP
        """, (user_id, level, lesson_id, score, max_score))
        add_xp(user_id, 5)


def mark_vocab(user_id: int, level: str, word_de: str, known: bool):
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO vocab_progress (user_id, level, word_de, known, updated_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, level, word_de) DO UPDATE SET
                known = excluded.known,
                updated_at = CURRENT_TIMESTAMP
        """, (user_id, level, word_de, int(known)))
        if known:
            add_xp(user_id, 2)


def save_test(user_id: int, level: str, lesson_id: int, score: int, max_score: int):
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO test_results (user_id, level, lesson_id, score, max_score)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, level, lesson_id, score, max_score))
        add_xp(user_id, score * 2)


def get_stats(user_id: int) -> dict:
    with get_conn() as conn:
        user = conn.execute("SELECT xp FROM users WHERE user_id=?", (user_id,)).fetchone()
        xp = user["xp"] if user else 0

        levels = ["A1.1", "A1.2", "A2.1", "A2.2", "B1.1", "B1.2"]
        stats = {}
        for level in levels:
            row = conn.execute("""
                SELECT COUNT(*) as done FROM progress
                WHERE user_id=? AND level=? AND completed=1
            """, (user_id, level)).fetchone()
            known = conn.execute("""
                SELECT COUNT(*) as cnt FROM vocab_progress
                WHERE user_id=? AND level=? AND known=1
            """, (user_id, level)).fetchone()
            stats[level] = {
                "lessons_done": row["done"] if row else 0,
                "vocab_known": known["cnt"] if known else 0,
            }
        return {"xp": xp, "levels": stats}


def get_lesson_progress(user_id: int, level: str) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT lesson_id, completed, score, max_score
            FROM progress WHERE user_id=? AND level=?
        """, (user_id, level)).fetchall()
        return [dict(r) for r in rows]


def get_vocab_progress(user_id: int, level: str) -> dict:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT word_de, known FROM vocab_progress
            WHERE user_id=? AND level=?
        """, (user_id, level)).fetchall()
        return {r["word_de"]: bool(r["known"]) for r in rows}
