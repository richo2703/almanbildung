"""Alman Bildung Bot — Content Aggregator"""
from content_a1 import A1_1, A1_2
from content_a2 import A2_1, A2_2
from content_b1 import B1_1, B1_2
from ext_a1 import EXT_A1_1, EXT_A1_2
from ext_a2 import EXT_A2_1, EXT_A2_2
from ext_b1 import EXT_B1_1, EXT_B1_2

CONTENT = {
    "A1.1": A1_1,
    "A1.2": A1_2,
    "A2.1": A2_1,
    "A2.2": A2_2,
    "B1.1": B1_1,
    "B1.2": B1_2,
}

EXTENSIONS = {
    "A1.1": EXT_A1_1,
    "A1.2": EXT_A1_2,
    "A2.1": EXT_A2_1,
    "A2.2": EXT_A2_2,
    "B1.1": EXT_B1_1,
    "B1.2": EXT_B1_2,
}

LEVELS_ORDER = ["A1.1","A1.2","A2.1","A2.2","B1.1","B1.2"]


def _merge_lesson(lesson: dict, ext: dict) -> dict:
    """Merge extension vocab and exercises into base lesson."""
    if not ext:
        return lesson
    lesson = dict(lesson)
    lesson["vocab"] = lesson["vocab"] + ext.get("vocab_extra", [])
    lesson["exercises"] = lesson["exercises"] + ext.get("exercises_extra", [])
    return lesson


def get_lesson(level: str, lesson_id: int):
    data = CONTENT.get(level)
    if not data:
        return None
    for l in data["lessons"]:
        if l["id"] == lesson_id:
            ext = EXTENSIONS.get(level, {}).get(lesson_id, {})
            return _merge_lesson(l, ext)
    return None


def get_all_vocab(level: str):
    """Return all vocab words for a level (including extensions)."""
    data = CONTENT.get(level)
    if not data:
        return []
    words = []
    for lesson in data["lessons"]:
        ext = EXTENSIONS.get(level, {}).get(lesson["id"], {})
        merged = _merge_lesson(lesson, ext)
        for w in merged["vocab"]:
            words.append({**w, "lesson_id": lesson["id"]})
    return words


def get_lesson_vocab(level: str, lesson_id: int):
    lesson = get_lesson(level, lesson_id)
    return lesson["vocab"] if lesson else []


def get_exercises(level: str, lesson_id: int):
    lesson = get_lesson(level, lesson_id)
    return lesson["exercises"] if lesson else []


def total_lessons(level: str) -> int:
    data = CONTENT.get(level)
    return len(data["lessons"]) if data else 0
