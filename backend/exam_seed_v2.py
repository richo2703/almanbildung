"""
exam_seed_v2.py — Comprehensive content for all providers × levels.
Run: python exam_seed_v2.py  OR imported by main.py auto-seed.
Idempotent: skips tasks whose title_de already exists in that section.
"""
import json
import sqlite3
import exam_db


def _conn():
    c = exam_db.get_conn()
    return c


def _get_section_id(conn, provider_name, level, section_type):
    row = conn.execute(
        "SELECT es.id FROM exam_sections es "
        "JOIN exam_levels el ON el.id = es.level_id "
        "JOIN exam_providers ep ON ep.id = el.provider_id "
        "WHERE ep.name=? AND el.level=? AND es.type=?",
        (provider_name, level, section_type)
    ).fetchone()
    return row["id"] if row else None


def _task_exists(conn, section_id, title_de):
    row = conn.execute(
        "SELECT id FROM exam_tasks WHERE section_id=? AND title_de=?",
        (section_id, title_de)
    ).fetchone()
    return row["id"] if row else None


def _insert_lesen_task(conn, section_id, t):
    """Insert a Lesen task with questions. Returns task_id."""
    existing = _task_exists(conn, section_id, t["title_de"])
    if existing:
        return existing

    extra_json = json.dumps(t.get("extra", {}))
    conn.execute(
        "INSERT INTO exam_tasks "
        "(section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz, "
        " text_content, extra_data) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        (
            section_id,
            t["title_de"], t.get("title_ru", t["title_de"]),
            t["task_type"],
            t.get("instruction_de", ""), t.get("instruction_ru", ""), t.get("instruction_uz", ""),
            t.get("text_content", ""),
            extra_json,
        )
    )
    task_id = conn.execute("SELECT last_insert_rowid() as id").fetchone()["id"]

    for q in t.get("questions", []):
        conn.execute(
            "INSERT INTO exam_questions "
            "(task_id, question_text, question_type, points, correct_answer, explanation_ru, explanation_uz) "
            "VALUES (?,?,?,?,?,?,?)",
            (
                task_id,
                q["text"], q.get("type", t["task_type"]),
                q.get("points", 1),
                q.get("correct_answer", ""),
                q.get("explanation_ru", ""), q.get("explanation_uz", ""),
            )
        )
        q_id = conn.execute("SELECT last_insert_rowid() as id").fetchone()["id"]
        for opt_text, is_correct in q.get("options", []):
            conn.execute(
                "INSERT INTO exam_answer_options (question_id, option_text, is_correct) VALUES (?,?,?)",
                (q_id, opt_text, 1 if is_correct else 0)
            )
    return task_id


def _insert_schreiben_task(conn, section_id, t):
    existing = _task_exists(conn, section_id, t["title_de"])
    if existing:
        return existing

    extra_json = json.dumps(t.get("extra", {}))
    conn.execute(
        "INSERT INTO exam_tasks "
        "(section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz, "
        " text_content, extra_data) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        (
            section_id,
            t["title_de"], t.get("title_ru", t["title_de"]),
            t["task_type"],
            t.get("instruction_de", ""), t.get("instruction_ru", ""), t.get("instruction_uz", ""),
            t.get("text_content", ""),
            extra_json,
        )
    )
    return conn.execute("SELECT last_insert_rowid() as id").fetchone()["id"]


# ══════════════════════════════════════════════════════════════════════════════
# CONTENT DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

A1_LESEN_EXTRA = [
    # Task 4 — Schilder verstehen
    {
        "title_de": "Schilder und Aushänge verstehen",
        "title_ru": "Понимание вывесок и объявлений",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie die Schilder. Sind die Aussagen richtig oder falsch?",
        "instruction_ru": "Прочитайте вывески. Предложения правильные или неправильные?",
        "instruction_uz": "Yozuvlarni o'qing. Gaplar to'g'ri yoki noto'g'ri?",
        "text_content": (
            "SCHILD 1 — Bahnhof:\n"
            "Gepäckaufbewahrung: Mo–Fr 6:00–22:00 Uhr | Sa+So 8:00–20:00 Uhr\n"
            "Preis: 3 Euro pro Stück / 24 Stunden\n\n"
            "SCHILD 2 — Supermarkt:\n"
            "Heute GESCHLOSSEN wegen Betriebsfeier.\n"
            "Morgen wieder für Sie da! Öffnung: 8:00 Uhr\n\n"
            "SCHILD 3 — Park:\n"
            "Hunde müssen an der Leine geführt werden.\n"
            "Radfahren nur auf dem markierten Weg.\n"
            "Ballspiele verboten.\n\n"
            "SCHILD 4 — Restaurant:\n"
            "Mittagstisch: 11:30–14:30 Uhr\n"
            "Tagessuppe + Hauptgericht: 9,90 €\n"
            "Reservierung empfohlen: 0221-334455"
        ),
        "time_limit": 240,
        "questions": [
            {
                "text": "Die Gepäckaufbewahrung am Bahnhof ist am Samstag ab 6 Uhr geöffnet.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "По субботам хранилище открывается в 8:00, а не в 6:00.",
                "explanation_uz": "Shanba kunlari kamera 8:00 da ochiladi, 6:00 da emas.",
            },
            {
                "text": "Die Aufbewahrung eines Gepäckstücks kostet 3 Euro pro Tag.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "На вывеске написано: 3 евро за штуку / 24 часа.",
                "explanation_uz": "Yozuvda ko'rsatilgan: 3 evro bir narsa uchun / 24 soat.",
            },
            {
                "text": "Der Supermarkt öffnet morgen um 9 Uhr.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "На вывеске написано: открытие в 8:00.",
                "explanation_uz": "Yozuvda: ochilish soati 8:00.",
            },
            {
                "text": "Im Park dürfen Hunde ohne Leine laufen.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "На вывеске написано: собак нужно держать на поводке.",
                "explanation_uz": "Yozuvda: itlar lashkarda bo'lishi kerak.",
            },
            {
                "text": "Im Restaurant kann man mittags für unter 10 Euro essen.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "Обеденный стол стоит 9,90 €, это меньше 10 €.",
                "explanation_uz": "Tushlik 9,90 € turadi, bu 10 € dan kam.",
            },
        ],
    },
    # Task 5 — SMS lesen
    {
        "title_de": "Kurznachrichten lesen (SMS / Chat)",
        "title_ru": "Чтение коротких сообщений (SMS / чат)",
        "task_type": "choice",
        "instruction_de": "Lesen Sie die Nachrichten und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте сообщения и выберите правильный ответ.",
        "instruction_uz": "Xabarlarni o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "Nachricht 1 — von Anna an Ben:\n"
            "\"Hallo Ben! Können wir uns heute um 16 Uhr im Café am Markt treffen? "
            "Ich muss etwas Wichtiges mit dir besprechen. LG Anna\"\n\n"
            "Nachricht 2 — von Ben an Anna:\n"
            "\"Hi Anna! Sorry, um 16 Uhr kann ich nicht. Ich habe einen Arzttermin. "
            "Geht es auch um 18 Uhr? Dann bin ich fertig. Gruß Ben\"\n\n"
            "Nachricht 3 — von Anna an Ben:\n"
            "\"18 Uhr ist perfekt! Bis dann. Ach ja – das Café schließt um 20 Uhr, "
            "also haben wir 2 Stunden. Reicht das? 😊\"\n\n"
            "Nachricht 4 — von Ben an Anna:\n"
            "\"Ja, das reicht super. Soll ich etwas mitbringen? Kuchen vielleicht? 🎂\"\n\n"
            "Nachricht 5 — von Anna an Ben:\n"
            "\"Nein danke, ich bringe das Essen mit. Du kannst Getränke bestellen. Bis später!\""
        ),
        "time_limit": 300,
        "questions": [
            {
                "text": "Wo wollen Anna und Ben sich treffen?",
                "type": "choice",
                "correct_answer": "Im Café am Markt",
                "options": [
                    ("Im Park", False),
                    ("Im Café am Markt", True),
                    ("Bei Anna zu Hause", False),
                    ("Im Restaurant", False),
                ],
                "explanation_ru": "Анна предложила встретиться в кафе на рынке.",
                "explanation_uz": "Anna bozordagi kafeda uchrashishni taklif qildi.",
            },
            {
                "text": "Warum kann Ben um 16 Uhr nicht kommen?",
                "type": "choice",
                "correct_answer": "Er hat einen Arzttermin",
                "options": [
                    ("Er muss arbeiten", False),
                    ("Er hat einen Arzttermin", True),
                    ("Er ist krank", False),
                    ("Er hat keine Zeit", False),
                ],
                "explanation_ru": "Бен написал: у меня приём у врача.",
                "explanation_uz": "Ben yozdi: shifokor qabulim bor.",
            },
            {
                "text": "Wann schließt das Café?",
                "type": "choice",
                "correct_answer": "Um 20 Uhr",
                "options": [
                    ("Um 18 Uhr", False),
                    ("Um 19 Uhr", False),
                    ("Um 20 Uhr", True),
                    ("Um 21 Uhr", False),
                ],
                "explanation_ru": "Анна написала: кафе закрывается в 20:00.",
                "explanation_uz": "Anna yozdi: kafe 20:00 da yopiladi.",
            },
            {
                "text": "Was bringt Ben mit?",
                "type": "choice",
                "correct_answer": "Nichts — Anna bringt das Essen",
                "options": [
                    ("Kuchen", False),
                    ("Getränke", False),
                    ("Nichts — Anna bringt das Essen", True),
                    ("Kaffee", False),
                ],
                "explanation_ru": "Анна сказала, что принесёт еду, а Бен может заказать напитки.",
                "explanation_uz": "Anna ovqat olib kelishini aytdi, Ben esa ichimliklar buyurtma beradi.",
            },
            {
                "text": "Wie lange haben Anna und Ben im Café Zeit?",
                "type": "choice",
                "correct_answer": "2 Stunden",
                "options": [
                    ("1 Stunde", False),
                    ("1,5 Stunden", False),
                    ("2 Stunden", True),
                    ("3 Stunden", False),
                ],
                "explanation_ru": "Они встречаются в 18:00, кафе закрывается в 20:00 — 2 часа.",
                "explanation_uz": "Ular 18:00 da uchrashadilar, kafe 20:00 da yopiladi — 2 soat.",
            },
        ],
    },
]

A1_SCHREIBEN_EXTRA = [
    {
        "title_de": "Postkarte aus dem Urlaub schreiben",
        "title_ru": "Написать открытку из отпуска",
        "task_type": "writing_free",
        "instruction_de": "Sie sind im Urlaub. Schreiben Sie eine Postkarte (30–40 Wörter) an Ihren Freund / Ihre Freundin. Schreiben Sie: Wo sind Sie? Wie ist das Wetter? Was machen Sie?",
        "instruction_ru": "Вы в отпуске. Напишите открытку (30–40 слов) другу/подруге. Напишите: Где вы? Какая погода? Что вы делаете?",
        "instruction_uz": "Siz ta'tildasyiz. Do'stingizga otkritka yozing (30–40 so'z). Yozing: Qaerdasiz? Ob-havo qanday? Nima qilayapsiz?",
        "text_content": "Aufgabe: Schreiben Sie eine Postkarte aus dem Urlaub.",
        "time_limit": 600,
        "extra": {
            "model_answer": (
                "Lieber Marco,\n\n"
                "ich bin jetzt in Wien! Die Stadt ist wunderschön und sehr groß. "
                "Das Wetter ist super — Sonne und 25 Grad. "
                "Ich besuche Museen und esse Wiener Schnitzel. "
                "Es schmeckt sehr lecker!\n\n"
                "Bis bald,\nSophia"
            ),
            "checklist": [
                "Anrede geschrieben? (Lieber / Liebe ...)",
                "Ort genannt?",
                "Wetter beschrieben?",
                "Aktivität erwähnt?",
                "Abschluss geschrieben? (Bis bald / Viele Grüße)",
                "30–40 Wörter?",
            ],
            "redemittel": [
                "Lieber … / Liebe …",
                "Ich bin jetzt in …",
                "Das Wetter ist … / Es ist … Grad.",
                "Ich besuche … / Ich esse … / Ich gehe …",
                "Es ist sehr schön / toll / interessant.",
                "Viele Grüße / Bis bald,",
            ],
            "word_count_min": 30,
            "word_count_max": 40,
        },
    },
]


# ── A2 CONTENT ────────────────────────────────────────────────────────────────

A2_LESEN = [
    {
        "title_de": "Stadtfest-Ankündigung lesen",
        "title_ru": "Объявление о городском празднике",
        "task_type": "choice",
        "instruction_de": "Lesen Sie den Artikel und wählen Sie die richtige Antwort (a, b, c oder d).",
        "instruction_ru": "Прочитайте статью и выберите правильный ответ (a, b, c или d).",
        "instruction_uz": "Maqolani o'qing va to'g'ri javobni tanlang (a, b, c yoki d).",
        "text_content": (
            "Internationales Stadtfest in Köln\n\n"
            "Am kommenden Wochenende findet in Köln das erste Internationale Stadtfest statt. "
            "Das Fest beginnt am Freitag um 16 Uhr und endet am Sonntag um 22 Uhr. "
            "Auf drei Bühnen spielen Bands aus Deutschland, Österreich und der Schweiz.\n\n"
            "Der Eintritt ist kostenlos. Für Essen und Trinken gibt es über 50 Stände mit "
            "Spezialitäten aus verschiedenen Ländern. Kinder können an Workshops teilnehmen "
            "und Instrumente ausprobieren.\n\n"
            "Das Fest findet auf dem Roncalliplatz vor dem Kölner Dom statt. "
            "Bei schlechtem Wetter werden einige Veranstaltungen in die Philharmonie verlegt."
        ),
        "time_limit": 360,
        "questions": [
            {
                "text": "Wann beginnt das Stadtfest?",
                "type": "choice",
                "correct_answer": "Am Freitag um 16 Uhr",
                "options": [
                    ("Am Freitag um 14 Uhr", False),
                    ("Am Freitag um 16 Uhr", True),
                    ("Am Samstag um 16 Uhr", False),
                    ("Am Sonntag um 12 Uhr", False),
                ],
                "explanation_ru": "В статье написано: фестиваль начинается в пятницу в 16:00.",
                "explanation_uz": "Maqolada yozilgan: festival juma kuni 16:00 da boshlanadi.",
            },
            {
                "text": "Was kostet der Eintritt?",
                "type": "choice",
                "correct_answer": "Der Eintritt ist kostenlos",
                "options": [
                    ("5 Euro", False),
                    ("10 Euro", False),
                    ("Der Eintritt ist kostenlos", True),
                    ("3 Euro für Kinder, 8 Euro für Erwachsene", False),
                ],
                "explanation_ru": "В статье чётко написано: вход бесплатный.",
                "explanation_uz": "Maqolada aniq yozilgan: kirish bepul.",
            },
            {
                "text": "Was können Kinder beim Fest machen?",
                "type": "choice",
                "correct_answer": "An Workshops teilnehmen und Instrumente ausprobieren",
                "options": [
                    ("Nur essen und trinken", False),
                    ("Gratis Konzerte besuchen", False),
                    ("An Workshops teilnehmen und Instrumente ausprobieren", True),
                    ("Kostenlose T-Shirts bekommen", False),
                ],
                "explanation_ru": "В статье написано: дети могут участвовать в воркшопах и пробовать музыкальные инструменты.",
                "explanation_uz": "Maqolada yozilgan: bolalar ustaxonalarda qatnashishi va asboblarni sinab ko'rishi mumkin.",
            },
            {
                "text": "Wo findet das Stadtfest statt?",
                "type": "choice",
                "correct_answer": "Auf dem Roncalliplatz vor dem Kölner Dom",
                "options": [
                    ("Im Stadtpark", False),
                    ("In der Philharmonie", False),
                    ("Auf dem Roncalliplatz vor dem Kölner Dom", True),
                    ("Am Rheinufer", False),
                ],
                "explanation_ru": "Место проведения: Ронкаллиплац перед Кёльнским собором.",
                "explanation_uz": "O'tkaziladigan joy: Köln sobori oldidagi Roncalliplatz.",
            },
            {
                "text": "Was passiert bei schlechtem Wetter?",
                "type": "choice",
                "correct_answer": "Einige Veranstaltungen werden in die Philharmonie verlegt",
                "options": [
                    ("Das Fest wird abgesagt", False),
                    ("Einige Veranstaltungen werden in die Philharmonie verlegt", True),
                    ("Das Fest findet drinnen statt", False),
                    ("Das Fest wird auf nächstes Wochenende verschoben", False),
                ],
                "explanation_ru": "В статье написано: при плохой погоде некоторые мероприятия переносятся в Филармонию.",
                "explanation_uz": "Yomg'irli havoda ba'zi tadbirlar Filarmoniyaga ko'chiriladi.",
            },
        ],
    },
    {
        "title_de": "WG-Anzeige: Mitbewohner gesucht",
        "title_ru": "Объявление о поиске соседа по квартире",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie den Forum-Beitrag. Sind die Aussagen richtig oder falsch?",
        "instruction_ru": "Прочитайте сообщение на форуме. Предложения правильные или неправильные?",
        "instruction_uz": "Forum xabarini o'qing. Gaplar to'g'ri yoki noto'g'ri?",
        "text_content": (
            "Hallo zusammen!\n\n"
            "Ich suche eine Mitbewohnerin oder einen Mitbewohner für meine 3-Zimmer-Wohnung "
            "in München-Schwabing. Die Wohnung liegt im zweiten Stock und hat einen Balkon "
            "mit Blick auf den Englischen Garten. Die monatliche Miete beträgt 650 Euro "
            "warm (inklusive Nebenkosten). Das freie Zimmer ist 18 m² groß und möbliert.\n\n"
            "Ich bin 29 Jahre alt, arbeite als Lehrerin und bin meistens ruhig und ordentlich. "
            "Ich koche gerne und wir können das gerne zusammen machen. Haustiere sind leider "
            "nicht erlaubt — das ist eine Regel des Vermieters.\n\n"
            "Wenn du Interesse hast, schreib mir bitte bis zum 15. dieses Monats.\n\n"
            "Grüße, Sarah"
        ),
        "time_limit": 300,
        "questions": [
            {
                "text": "Die Wohnung hat zwei Zimmer.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте написано: 3-комнатная квартира.",
                "explanation_uz": "Matnda yozilgan: 3 xonali kvartira.",
            },
            {
                "text": "Die Miete beträgt 650 Euro und beinhaltet die Nebenkosten.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "650 евро тёплая (включая коммунальные расходы).",
                "explanation_uz": "650 evro issiq (kommunal to'lovlar kiradi).",
            },
            {
                "text": "Das freie Zimmer ist nicht möbliert.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте написано: комната меблирована.",
                "explanation_uz": "Matnda yozilgan: xona mebel bilan.",
            },
            {
                "text": "Sarah arbeitet als Ärztin.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Сара работает учительницей, не врачом.",
                "explanation_uz": "Sara o'qituvchi, shifokor emas.",
            },
            {
                "text": "Haustiere dürfen in der Wohnung gehalten werden.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Домашние животные запрещены — это правило владельца.",
                "explanation_uz": "Uy hayvonlari ruxsat etilmagan — bu uy egasining qoidasi.",
            },
        ],
    },
    {
        "title_de": "Kinoprogramm lesen",
        "title_ru": "Читаем программу кинотеатра",
        "task_type": "choice",
        "instruction_de": "Lesen Sie das Kinoprogramm und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте программу кинотеатра и выберите правильный ответ.",
        "instruction_uz": "Kino dasturini o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "KINO SCALA — WOCHENPROGRAMM\n\n"
            "Fantastische Reise (Abenteuer, USA, 2024) | 95 Min.\n"
            "Mo–Do: 15:00 / 18:30 | Fr–So: 13:00 / 17:00 / 20:30\n"
            "Empfohlen ab 12 Jahren | OmU (Originalversion mit Untertiteln) dienstags\n\n"
            "Die große Bäckerei (Komödie, Deutschland, 2024) | 112 Min.\n"
            "Täglich: 16:00 / 20:00 | Sonntag auch: 11:00 (Familienvorstellung)\n"
            "Empfohlen ab 6 Jahren\n\n"
            "Stille Nacht (Thriller, Österreich, 2024) | 128 Min.\n"
            "Fr+Sa: 21:30 (Spätvorstellung) | So: 18:00\n"
            "Empfohlen ab 16 Jahren\n\n"
            "Tickets: Kasse ab 1 Std. vor Beginn | Online: www.kino-scala.de\n"
            "Studentenrabatt: 20% mit gültigem Ausweis"
        ),
        "time_limit": 360,
        "questions": [
            {
                "text": "Wie lange dauert 'Die große Bäckerei'?",
                "type": "choice",
                "correct_answer": "112 Minuten",
                "options": [("95 Minuten", False), ("112 Minuten", True), ("128 Minuten", False), ("100 Minuten", False)],
                "explanation_ru": "В программе: «Die große Bäckerei» — 112 мин.",
                "explanation_uz": "'Die große Bäckerei' — 112 daqiqa.",
            },
            {
                "text": "An welchem Tag gibt es 'Fantastische Reise' in Originalsprache mit Untertiteln?",
                "type": "choice",
                "correct_answer": "Dienstag",
                "options": [("Montag", False), ("Dienstag", True), ("Freitag", False), ("Sonntag", False)],
                "explanation_ru": "OmU (оригинал с субтитрами) — по вторникам.",
                "explanation_uz": "OmU (asl tilda, subtitrlar bilan) — seshanba kunlari.",
            },
            {
                "text": "Wann findet die Familienvorstellung von 'Die große Bäckerei' statt?",
                "type": "choice",
                "correct_answer": "Sonntag um 11:00",
                "options": [("Samstag um 20:00", False), ("Sonntag um 11:00", True), ("Montag um 16:00", False), ("Freitag um 13:00", False)],
                "explanation_ru": "Воскресенье в 11:00 — семейный сеанс.",
                "explanation_uz": "Yakshanba 11:00 — oilaviy seans.",
            },
            {
                "text": "Ab welchem Alter ist 'Stille Nacht' empfohlen?",
                "type": "choice",
                "correct_answer": "Ab 16 Jahren",
                "options": [("Ab 6 Jahren", False), ("Ab 12 Jahren", False), ("Ab 16 Jahren", True), ("Ab 18 Jahren", False)],
                "explanation_ru": "В программе: рекомендовано с 16 лет.",
                "explanation_uz": "Dasturda: 16 yoshdan tavsiya etiladi.",
            },
            {
                "text": "Wie viel Rabatt bekommen Studenten?",
                "type": "choice",
                "correct_answer": "20%",
                "options": [("10%", False), ("15%", False), ("20%", True), ("25%", False)],
                "explanation_ru": "Студенческая скидка: 20% при наличии удостоверения.",
                "explanation_uz": "Talabalar uchun chegirma: 20%, guvohnoma bilan.",
            },
        ],
    },
    {
        "title_de": "Urlaubsbericht: Wien",
        "title_ru": "Отчёт об отпуске: Вена",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie den Reisebericht. Sind die Aussagen richtig oder falsch?",
        "instruction_ru": "Прочитайте отчёт о поездке. Предложения правильные или нет?",
        "instruction_uz": "Sayohat hisobotini o'qing. Gaplar to'g'ri yoki noto'g'ri?",
        "text_content": (
            "Mein Urlaub in Wien\n\n"
            "Letzten Sommer war ich drei Wochen in Wien. Ich habe in einem kleinen Hotel "
            "im dritten Bezirk gewohnt. Das Hotel war nicht teuer — ich habe nur 60 Euro "
            "pro Nacht bezahlt.\n\n"
            "Wien ist eine wunderbare Stadt. Ich habe viele Museen besucht: das Kunsthistorische "
            "Museum, das Naturhistorische Museum und das Technische Museum. Am liebsten war mir "
            "das Kunsthistorische Museum. Der Eintritt kostet 16 Euro für Erwachsene, "
            "aber mit der Wien-Karte bekommt man 10% Rabatt.\n\n"
            "Ich habe auch viel gegessen! Das Wiener Schnitzel ist wirklich sehr lecker. "
            "Ein gutes Restaurant habe ich in der Innenstadt gefunden — man muss aber einen "
            "Tisch reservieren, denn es ist immer voll.\n\n"
            "Am letzten Tag bin ich mit der U-Bahn zum Flughafen gefahren. "
            "Die Fahrt hat nur 16 Minuten gedauert. Ich möchte unbedingt wieder nach Wien!"
        ),
        "time_limit": 300,
        "questions": [
            {
                "text": "Der Autor war zwei Wochen in Wien.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте написано: три недели, а не две.",
                "explanation_uz": "Matnda yozilgan: uch hafta, ikki emas.",
            },
            {
                "text": "Das Hotel hat 60 Euro pro Nacht gekostet.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "Верно: 60 евро за ночь.",
                "explanation_uz": "To'g'ri: tunda 60 evro.",
            },
            {
                "text": "Das Kunsthistorische Museum hat dem Autor am besten gefallen.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "В тексте: «Am liebsten war mir das Kunsthistorische Museum».",
                "explanation_uz": "Matnda: 'Am liebsten war mir das Kunsthistorische Museum'.",
            },
            {
                "text": "Mit der Wien-Karte bekommt man 20% Rabatt.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Скидка 10%, а не 20%.",
                "explanation_uz": "Chegirma 10%, 20% emas.",
            },
            {
                "text": "Zum Flughafen ist der Autor mit dem Taxi gefahren.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте написано: поехал на метро (U-Bahn).",
                "explanation_uz": "Matnda yozilgan: metro (U-Bahn) bilan bordi.",
            },
        ],
    },
    {
        "title_de": "Stellenanzeige lesen",
        "title_ru": "Читаем объявление о работе",
        "task_type": "choice",
        "instruction_de": "Lesen Sie die Stellenanzeige und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте объявление о вакансии и выберите правильный ответ.",
        "instruction_uz": "Ish e'lonini o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "STELLENANZEIGE\n\n"
            "JUNG & LECKER Bäckerei sucht\n"
            "Verkäuferin / Verkäufer (Teilzeit)\n\n"
            "Arbeitszeit: Montag bis Samstag, 7:00–13:00 Uhr\n"
            "Beginn: Ab sofort\n\n"
            "Wir bieten:\n"
            "• Stundenlohn: 14,50 Euro\n"
            "• Freundliches Team\n"
            "• Frische Backwaren zum Mitnehmen\n"
            "• Möglichkeit zur Festanstellung nach 6 Monaten\n\n"
            "Wir suchen:\n"
            "• Berufserfahrung im Verkauf (mindestens 1 Jahr)\n"
            "• Gute Deutschkenntnisse (mindestens B1)\n"
            "• Freundlichkeit und Pünktlichkeit\n"
            "• Verfügbarkeit am Samstag\n\n"
            "Bewerbung bitte per E-Mail an: jobs@jung-lecker.de\n"
            "Fragen: Tel. 030-556677 (Herr Müller)"
        ),
        "time_limit": 360,
        "questions": [
            {
                "text": "Wie viele Stunden am Tag muss man in der Bäckerei arbeiten?",
                "type": "choice",
                "correct_answer": "6 Stunden",
                "options": [("4 Stunden", False), ("6 Stunden", True), ("8 Stunden", False), ("5 Stunden", False)],
                "explanation_ru": "7:00–13:00 = 6 часов в день.",
                "explanation_uz": "7:00–13:00 = 6 soat.",
            },
            {
                "text": "Wie viel verdient man pro Stunde?",
                "type": "choice",
                "correct_answer": "14,50 Euro",
                "options": [("12,50 Euro", False), ("13,00 Euro", False), ("14,50 Euro", True), ("15,00 Euro", False)],
                "explanation_ru": "В объявлении: почасовая ставка 14,50 евро.",
                "explanation_uz": "E'londa: soatlik ish haqi 14,50 evro.",
            },
            {
                "text": "Welche Deutschkenntnisse werden verlangt?",
                "type": "choice",
                "correct_answer": "Mindestens B1",
                "options": [("A1", False), ("A2", False), ("Mindestens B1", True), ("B2", False)],
                "explanation_ru": "Требуется минимум уровень B1.",
                "explanation_uz": "Kamida B1 darajasi talab qilinadi.",
            },
            {
                "text": "Wann kann man eine Festanstellung bekommen?",
                "type": "choice",
                "correct_answer": "Nach 6 Monaten",
                "options": [("Nach 3 Monaten", False), ("Nach 6 Monaten", True), ("Nach einem Jahr", False), ("Sofort", False)],
                "explanation_ru": "После 6 месяцев возможна постоянная должность.",
                "explanation_uz": "6 oydan keyin doimiy ish joyi mumkin.",
            },
            {
                "text": "Wie soll man sich bewerben?",
                "type": "choice",
                "correct_answer": "Per E-Mail an jobs@jung-lecker.de",
                "options": [
                    ("Per Post an Herr Müller", False),
                    ("Per E-Mail an jobs@jung-lecker.de", True),
                    ("Persönlich in der Bäckerei", False),
                    ("Per Telefon", False),
                ],
                "explanation_ru": "Заявка — по электронной почте на указанный адрес.",
                "explanation_uz": "Ariza — ko'rsatilgan elektron pochta manziliga.",
            },
        ],
    },
]

A2_SCHREIBEN = [
    {
        "title_de": "E-Mail an einen Freund schreiben",
        "title_ru": "Написать e-mail другу",
        "task_type": "writing_free",
        "instruction_de": (
            "Ihr Freund Marco fragt Sie: 'Was machst du gerade? Wie geht es dir? "
            "Hast du Pläne für das Wochenende?' Schreiben Sie eine E-Mail (50–70 Wörter). "
            "Antworten Sie auf seine Fragen."
        ),
        "instruction_ru": (
            "Ваш друг Марко спрашивает: «Что ты сейчас делаешь? Как дела? "
            "Есть ли у тебя планы на выходные?» Напишите e-mail (50–70 слов). "
            "Ответьте на его вопросы."
        ),
        "instruction_uz": (
            "Do'stingiz Marko so'raydi: 'Hozir nima qilayapsan? Yaxshimisan? "
            "Dam olish kunlariga rejang bormi?' E-mail yozing (50–70 so'z). "
            "Uning savollariga javob bering."
        ),
        "text_content": "Aufgabe: Schreiben Sie eine Antwort-E-Mail an Ihren Freund Marco.",
        "time_limit": 900,
        "extra": {
            "model_answer": (
                "Hallo Marco!\n\n"
                "Danke für deine Nachricht! Mir geht es gut, ich bin gerade sehr beschäftigt. "
                "Ich studiere Deutsch und habe viel zu lernen.\n\n"
                "Am Wochenende habe ich tolle Pläne: Ich fahre mit meiner Familie in die Berge. "
                "Wir wollen wandern und frische Luft genießen. Das Wetter soll schön sein!\n\n"
                "Wie geht es dir? Was machst du am Wochenende?\n\n"
                "Viele Grüße,\n[Name]"
            ),
            "checklist": [
                "Anrede (Hallo ... / Lieber ...)?",
                "Frage 1 beantwortet: Was machst du gerade?",
                "Frage 2 beantwortet: Wie geht es dir?",
                "Frage 3 beantwortet: Pläne für das Wochenende?",
                "Abschluss (Viele Grüße / Tschüss)?",
                "50–70 Wörter?",
            ],
            "redemittel": [
                "Hallo … / Lieber … / Hi …,",
                "Danke für deine Nachricht!",
                "Mir geht es (sehr) gut / nicht so gut.",
                "Ich bin gerade … / Ich arbeite / studiere …",
                "Am Wochenende möchte ich … / plane ich …",
                "Wie geht es dir? / Was machst du so?",
                "Viele Grüße / Bis bald,",
            ],
            "word_count_min": 50,
            "word_count_max": 70,
        },
    },
    {
        "title_de": "Entschuldigungsmail schreiben",
        "title_ru": "Написать письмо с извинениями",
        "task_type": "writing_free",
        "instruction_de": (
            "Sie können einen Termin mit Ihrer Kollegin Frau Weber nicht einhalten. "
            "Schreiben Sie ihr eine E-Mail (40–60 Wörter): "
            "Entschuldigen Sie sich. Erklären Sie den Grund. Schlagen Sie einen neuen Termin vor."
        ),
        "instruction_ru": (
            "Вы не можете прийти на встречу с коллегой фрау Вебер. "
            "Напишите ей e-mail (40–60 слов): "
            "Извинитесь. Объясните причину. Предложите новое время встречи."
        ),
        "instruction_uz": (
            "Siz hamkasbingiz Frau Weber bilan uchrashuvga bora olmaysiz. "
            "Unga e-mail yozing (40–60 so'z): "
            "Uzr so'rang. Sababini tushuntiring. Yangi vaqt taklif qiling."
        ),
        "text_content": "Aufgabe: Schreiben Sie eine Entschuldigungs-E-Mail.",
        "time_limit": 900,
        "extra": {
            "model_answer": (
                "Sehr geehrte Frau Weber,\n\n"
                "es tut mir sehr leid, aber ich kann unseren Termin am Donnerstag leider nicht "
                "einhalten. Ich bin krank und muss zum Arzt.\n\n"
                "Können wir den Termin verschieben? Ich schlage Montag um 14 Uhr vor. "
                "Passt Ihnen das?\n\n"
                "Mit freundlichen Grüßen,\n[Name]"
            ),
            "checklist": [
                "Formelle Anrede (Sehr geehrte ...)?",
                "Entschuldigung ausgedrückt?",
                "Grund genannt?",
                "Neuen Termin vorgeschlagen?",
                "Formeller Abschluss (Mit freundlichen Grüßen)?",
                "40–60 Wörter?",
            ],
            "redemittel": [
                "Sehr geehrte Frau … / Sehr geehrter Herr …,",
                "Es tut mir leid, aber …",
                "Ich kann leider nicht …, weil/denn …",
                "Können wir den Termin verschieben?",
                "Ich schlage … um … Uhr vor.",
                "Ist das für Sie möglich?",
                "Mit freundlichen Grüßen,",
            ],
            "word_count_min": 40,
            "word_count_max": 60,
        },
    },
    {
        "title_de": "Kurzmitteilung an den Vermieter",
        "title_ru": "Краткое сообщение владельцу квартиры",
        "task_type": "writing_free",
        "instruction_de": (
            "In Ihrer Wohnung ist die Heizung kaputt. Schreiben Sie Ihrem Vermieter "
            "eine Nachricht (40–60 Wörter). Beschreiben Sie das Problem. Bitten Sie um schnelle Hilfe."
        ),
        "instruction_ru": (
            "В вашей квартире сломалось отопление. Напишите владельцу квартиры "
            "сообщение (40–60 слов). Опишите проблему. Попросите срочной помощи."
        ),
        "instruction_uz": (
            "Kvartiraizdagi isitish tizimi buzildi. Uy egangizga xabar yozing "
            "(40–60 so'z). Muammoni tasvirlab bering. Tezkor yordam so'rang."
        ),
        "text_content": "Aufgabe: Schreiben Sie eine Nachricht über ein Problem in der Wohnung.",
        "time_limit": 900,
        "extra": {
            "model_answer": (
                "Sehr geehrter Herr Bauer,\n\n"
                "ich schreibe Ihnen wegen eines Problems in meiner Wohnung. "
                "Seit gestern Abend funktioniert die Heizung nicht mehr. "
                "Es ist sehr kalt in der Wohnung (nur 14 Grad).\n\n"
                "Könnten Sie bitte so schnell wie möglich einen Techniker schicken? "
                "Ich bin tagsüber zu Hause.\n\n"
                "Mit freundlichen Grüßen,\n[Name], Wohnung 3B"
            ),
            "checklist": [
                "Anrede?",
                "Problem klar beschrieben?",
                "Dringlichkeit ausgedrückt?",
                "Bitte um Hilfe formuliert?",
                "Abschluss?",
                "40–60 Wörter?",
            ],
            "redemittel": [
                "Sehr geehrte/r …,",
                "ich schreibe Ihnen wegen …",
                "Seit … funktioniert … nicht mehr.",
                "Es gibt ein Problem mit …",
                "Könnten Sie bitte … ?",
                "Ich bitte Sie dringend um …",
                "Mit freundlichen Grüßen,",
            ],
            "word_count_min": 40,
            "word_count_max": 60,
        },
    },
]


# ── B1 CONTENT ────────────────────────────────────────────────────────────────

B1_LESEN = [
    {
        "title_de": "Elektroautos: Chancen und Herausforderungen",
        "title_ru": "Электромобили: возможности и вызовы",
        "task_type": "choice",
        "instruction_de": "Lesen Sie den Artikel und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте статью и выберите правильный ответ.",
        "instruction_uz": "Maqolani o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "Elektroautos: Zukunft oder Problem?\n\n"
            "Immer mehr Deutsche kaufen Elektroautos. Im letzten Jahr wurden über "
            "500.000 neue Elektrofahrzeuge zugelassen — ein Rekord. Die Bundesregierung "
            "möchte, dass bis 2030 mindestens 15 Millionen Elektroautos auf deutschen "
            "Straßen fahren.\n\n"
            "Kritiker sehen jedoch Probleme: Die Infrastruktur für Ladestationen ist "
            "noch unzureichend. Besonders auf dem Land gibt es zu wenige Möglichkeiten, "
            "das Auto aufzuladen. Außerdem sind Elektroautos in der Anschaffung teurer "
            "als Benzinfahrzeuge, auch wenn die Betriebskosten geringer sind.\n\n"
            "Umweltschützer weisen darauf hin, dass die Produktion von Batterien viel "
            "Energie verbraucht und Rohstoffe wie Lithium und Kobalt unter problematischen "
            "Bedingungen abgebaut werden. Dennoch sind Elektroautos im Betrieb deutlich "
            "umweltfreundlicher als Fahrzeuge mit Verbrennungsmotor.\n\n"
            "Experten sind sich einig: Die Elektromobilität ist wichtig für den Klimaschutz, "
            "aber sie ist keine vollständige Lösung für alle Verkehrsprobleme. "
            "Investitionen in den öffentlichen Nahverkehr seien genauso wichtig."
        ),
        "time_limit": 480,
        "questions": [
            {
                "text": "Wie viele Elektroautos sollen laut Bundesregierung bis 2030 auf deutschen Straßen fahren?",
                "type": "choice",
                "correct_answer": "Mindestens 15 Millionen",
                "options": [
                    ("5 Millionen", False), ("10 Millionen", False),
                    ("Mindestens 15 Millionen", True), ("20 Millionen", False),
                ],
                "explanation_ru": "В статье: правительство ставит цель — минимум 15 млн электромобилей к 2030 году.",
                "explanation_uz": "Maqolada: hukumat 2030 yilgacha kamida 15 million elektromobil maqsadini qo'ygan.",
            },
            {
                "text": "Was kritisieren Skeptiker am meisten an der Elektromobilität?",
                "type": "choice",
                "correct_answer": "Die unzureichende Ladeinfrastruktur",
                "options": [
                    ("Die hohen Betriebskosten", False),
                    ("Die unzureichende Ladeinfrastruktur", True),
                    ("Das Design der Elektroautos", False),
                    ("Die Motorleistung", False),
                ],
                "explanation_ru": "Критики указывают на недостаточную инфраструктуру зарядных станций.",
                "explanation_uz": "Tanqidchilar zaryadlash stantsiyalarining yetarli emasligini ta'kidlaydi.",
            },
            {
                "text": "Was sagen Umweltschützer über die Batterieproduktion?",
                "type": "choice",
                "correct_answer": "Sie verbraucht viel Energie und die Rohstoffe werden unter problematischen Bedingungen abgebaut",
                "options": [
                    ("Sie ist sehr günstig", False),
                    ("Sie ist vollständig umweltfreundlich", False),
                    ("Sie verbraucht viel Energie und die Rohstoffe werden unter problematischen Bedingungen abgebaut", True),
                    ("Sie verbraucht wenig Energie", False),
                ],
                "explanation_ru": "Экологи указывают на высокое потребление энергии при производстве батарей и проблемы с добычей лития и кобальта.",
                "explanation_uz": "Ekologlar batareyalar ishlab chiqarishda ko'p energiya sarflanishini va litiy, kobalt qazib olish muammolarini ta'kidlaydi.",
            },
            {
                "text": "Wie sind Elektroautos im Vergleich zu Benzinfahrzeugen?",
                "type": "choice",
                "correct_answer": "Teurer in der Anschaffung, aber günstiger im Betrieb",
                "options": [
                    ("Günstiger in der Anschaffung, teurer im Betrieb", False),
                    ("Teurer in der Anschaffung, aber günstiger im Betrieb", True),
                    ("Gleich teuer in Anschaffung und Betrieb", False),
                    ("Günstiger in beiden Bereichen", False),
                ],
                "explanation_ru": "В статье: дороже при покупке, но дешевле в эксплуатации.",
                "explanation_uz": "Maqolada: sotib olishda qimmatroq, lekin ekspluatatsiyada arzonroq.",
            },
            {
                "text": "Was empfehlen Experten zusätzlich zur Elektromobilität?",
                "type": "choice",
                "correct_answer": "Investitionen in den öffentlichen Nahverkehr",
                "options": [
                    ("Mehr Straßen bauen", False),
                    ("Benzinpreise erhöhen", False),
                    ("Investitionen in den öffentlichen Nahverkehr", True),
                    ("Fahrverbote für Benzinfahrzeuge einführen", False),
                ],
                "explanation_ru": "Эксперты считают инвестиции в общественный транспорт столь же важными.",
                "explanation_uz": "Mutaxassislar jamoat transportiga investitsiyalarni ham muhim deb hisoblaydi.",
            },
        ],
    },
    {
        "title_de": "Au-pair-Erfahrung im Ausland",
        "title_ru": "Опыт работы au-pair за рубежом",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie den Erfahrungsbericht. Sind die Aussagen richtig oder falsch?",
        "instruction_ru": "Прочитайте отчёт. Правильные или нет?",
        "instruction_uz": "Hisobotni o'qing. To'g'ri yoki noto'g'ri?",
        "text_content": (
            "Ein Jahr in Kanada — Mein Au-pair-Bericht\n\n"
            "Als ich vor zwei Jahren beschlossen habe, ein Jahr als Au-pair nach Kanada zu gehen, "
            "war ich sowohl aufgeregt als auch nervös. Ich war damals 22 Jahre alt und hatte "
            "noch nie so lange alleine im Ausland gelebt.\n\n"
            "Meine Gastfamilie in Toronto war sehr freundlich. Sie hatten drei Kinder zwischen "
            "5 und 10 Jahren, um die ich mich hauptsächlich kümmern musste. Meine Aufgaben "
            "umfassten das Bringen zur Schule, Kochen für die Kinder und Hausaufgabenbetreuung.\n\n"
            "Besonders schwer war die erste Zeit wegen der Sprache. Obwohl mein Englisch gut war, "
            "fehlten mir die Alltagsausdrücke und der kanadische Slang. Außerdem vermisste ich "
            "meine Familie und Freunde in Deutschland sehr.\n\n"
            "Mit der Zeit wurde alles einfacher. Ich lernte neue Freunde kennen — andere "
            "Austauschstudenten aus Deutschland, Frankreich und Japan. Wir machten gemeinsam "
            "Ausflüge und erkundeten Kanada. Am schönsten war mein Besuch der Niagarafälle.\n\n"
            "Was ich mitgenommen habe: mehr Selbstständigkeit, besseres Englisch und "
            "unvergessliche Erfahrungen. Ich würde diese Erfahrung jedem empfehlen!"
        ),
        "time_limit": 420,
        "questions": [
            {
                "text": "Die Autorin war 24 Jahre alt, als sie nach Kanada gegangen ist.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Ей было 22 года, не 24.",
                "explanation_uz": "U 22 yoshda edi, 24 emas.",
            },
            {
                "text": "Die Gastfamilie hatte drei Kinder.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "В тексте: три ребёнка в возрасте от 5 до 10 лет.",
                "explanation_uz": "Matnda: 5 dan 10 yoshgacha uch bola.",
            },
            {
                "text": "Die größte Schwierigkeit am Anfang war die Sprache.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "В тексте написано: первое время было особенно трудно из-за языка.",
                "explanation_uz": "Matnda: birinchi vaqtda til tufayli ayniqsa qiyin bo'ldi.",
            },
            {
                "text": "Die Autorin hat keine neuen Freunde in Kanada gefunden.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Она познакомилась с другими студентами по обмену из Германии, Франции и Японии.",
                "explanation_uz": "U Germaniya, Fransiya va Yaponiyadan boshqa almashinuv talabalar bilan tanishdi.",
            },
            {
                "text": "Die Autorin empfiehlt diese Erfahrung nicht.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Наоборот: она рекомендует этот опыт всем.",
                "explanation_uz": "Aksincha: u bu tajribani hammaga tavsiya qiladi.",
            },
        ],
    },
    {
        "title_de": "Bürojob — Stellenanzeige für B1-Lerner",
        "title_ru": "Вакансия офисного работника — для уровня B1",
        "task_type": "choice",
        "instruction_de": "Lesen Sie die Stellenanzeige und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте объявление о вакансии и выберите правильный ответ.",
        "instruction_uz": "Ish e'lonini o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "STELLENANZEIGE — Sachbearbeiter/in (Vollzeit)\n\n"
            "Die Kreisverwaltung Bergheim sucht zum 1. März eine/n engagierte/n\n"
            "Sachbearbeiter/in für das Bürgerbüro.\n\n"
            "Ihre Aufgaben:\n"
            "• Bearbeitung von Bürgeranfragen (persönlich, telefonisch, schriftlich)\n"
            "• Verwaltung von Dokumenten und Akten\n"
            "• Zusammenarbeit mit anderen Abteilungen\n"
            "• Datenpflege im elektronischen System\n\n"
            "Ihr Profil:\n"
            "• Abgeschlossene kaufmännische Ausbildung oder Verwaltungsausbildung\n"
            "• Sehr gute Deutschkenntnisse (mindestens C1)\n"
            "• Sicherer Umgang mit MS Office\n"
            "• Teamfähigkeit und Belastbarkeit\n"
            "• Fremdsprachen von Vorteil (besonders Arabisch, Türkisch, Russisch)\n\n"
            "Wir bieten:\n"
            "• Unbefristeter Vertrag nach der Probezeit\n"
            "• Gehalt nach Tarifvertrag (TVöD) Entgeltgruppe 6\n"
            "• 30 Tage Urlaub\n"
            "• Flexible Arbeitszeiten (Kernzeit: 9–15 Uhr)\n\n"
            "Bewerbungsunterlagen bis 15. Februar an:\n"
            "bewerbung@kreisverwaltung-bergheim.de"
        ),
        "time_limit": 480,
        "questions": [
            {
                "text": "Wann soll die Stelle besetzt werden?",
                "type": "choice",
                "correct_answer": "Zum 1. März",
                "options": [("Sofort", False), ("Zum 1. März", True), ("Zum 1. April", False), ("Zum 1. Januar", False)],
                "explanation_ru": "В объявлении: начало работы — 1 марта.",
                "explanation_uz": "E'londa: ish boshlanishi — 1 mart.",
            },
            {
                "text": "Welche Deutschkenntnisse werden verlangt?",
                "type": "choice",
                "correct_answer": "Mindestens C1",
                "options": [("B2", False), ("Mindestens C1", True), ("B1", False), ("Muttersprachenniveau", False)],
                "explanation_ru": "В объявлении требуется минимум уровень C1.",
                "explanation_uz": "E'londa kamida C1 darajasi talab qilinadi.",
            },
            {
                "text": "Was ist ein Vorteil, aber keine Pflicht?",
                "type": "choice",
                "correct_answer": "Fremdsprachenkenntnisse (Arabisch, Türkisch, Russisch)",
                "options": [
                    ("MS-Office-Kenntnisse", False),
                    ("Fremdsprachenkenntnisse (Arabisch, Türkisch, Russisch)", True),
                    ("Teamfähigkeit", False),
                    ("Kaufmännische Ausbildung", False),
                ],
                "explanation_ru": "Иностранные языки указаны как «von Vorteil» (преимущество), но не обязательное требование.",
                "explanation_uz": "'Von Vorteil' (qo'shimcha ustunlik) sifatida ko'rsatilgan, lekin majburiy emas.",
            },
            {
                "text": "Wie viele Urlaubstage gibt es pro Jahr?",
                "type": "choice",
                "correct_answer": "30 Tage",
                "options": [("24 Tage", False), ("28 Tage", False), ("30 Tage", True), ("32 Tage", False)],
                "explanation_ru": "В объявлении: 30 дней отпуска.",
                "explanation_uz": "E'londa: 30 kun ta'til.",
            },
            {
                "text": "Bis wann muss die Bewerbung eingehen?",
                "type": "choice",
                "correct_answer": "Bis 15. Februar",
                "options": [("Bis 1. März", False), ("Bis 15. Februar", True), ("Bis Ende Januar", False), ("Bis 28. Februar", False)],
                "explanation_ru": "Срок подачи заявки — до 15 февраля.",
                "explanation_uz": "Ariza topshirish muddati — 15 fevralga qadar.",
            },
        ],
    },
    {
        "title_de": "Stadtbibliothek — Neue Angebote",
        "title_ru": "Городская библиотека — новые предложения",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie den Informationstext und entscheiden Sie: richtig oder falsch?",
        "instruction_ru": "Прочитайте информационный текст и решите: правильно или неправильно?",
        "instruction_uz": "Ma'lumot matnini o'qing va qaror qiling: to'g'ri yoki noto'g'ri?",
        "text_content": (
            "Die Stadtbibliothek Hannover modernisiert ihr Angebot\n\n"
            "Die Stadtbibliothek Hannover hat ihr Programm für das neue Jahr vorgestellt. "
            "Ab dem 1. Februar stehen den Nutzern neben den klassischen Büchern und Zeitschriften "
            "auch E-Books, Hörbücher und digitale Zeitungen zur Verfügung — alles kostenlos "
            "mit dem Bibliotheksausweis.\n\n"
            "Neu ist auch der 'Maker Space': Ein Raum mit 3D-Druckern, Lasercuttern und "
            "digitalen Zeichentabletts, den Mitglieder nach vorheriger Anmeldung nutzen können. "
            "Die Nutzung ist für Erwachsene und Jugendliche ab 14 Jahren gestattet.\n\n"
            "Die Öffnungszeiten wurden angepasst: Montag bis Freitag 9:00–20:00 Uhr, "
            "Samstag 10:00–16:00 Uhr. Sonntag bleibt die Bibliothek geschlossen.\n\n"
            "Ein Jahresausweis kostet für Erwachsene 25 Euro, für Schüler und Studenten 10 Euro, "
            "für Kinder unter 14 Jahren ist er kostenlos. Senioren über 65 Jahre zahlen nur 12 Euro.\n\n"
            "Wer keinen eigenen Computer hat, kann die sechs Internet-Terminals in der Bibliothek "
            "nutzen — je 30 Minuten pro Besuch gratis."
        ),
        "time_limit": 420,
        "questions": [
            {
                "text": "E-Books und digitale Zeitungen sind mit dem Bibliotheksausweis kostenlos nutzbar.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "В тексте: E-книги, аудиокниги и цифровые газеты — бесплатно с читательским билетом.",
                "explanation_uz": "Matnda: E-kitoblar, audiokitoblar va raqamli gazetalar — kutubxona kartasi bilan bepul.",
            },
            {
                "text": "Der Maker Space kann ohne Anmeldung genutzt werden.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте написано: по предварительной записи.",
                "explanation_uz": "Matnda yozilgan: oldindan yozilish kerak.",
            },
            {
                "text": "Die Bibliothek ist sonntags geöffnet.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "По воскресеньям библиотека закрыта.",
                "explanation_uz": "Yakshanba kunlari kutubxona yopiq.",
            },
            {
                "text": "Kinder unter 14 Jahren bekommen den Ausweis gratis.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "Для детей до 14 лет читательский билет бесплатный.",
                "explanation_uz": "14 yoshgacha bo'lgan bolalar uchun kutubxona kartasi bepul.",
            },
            {
                "text": "Die Internet-Terminals sind täglich 60 Minuten kostenlos nutzbar.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Интернет-терминалы — 30 минут бесплатно за посещение, не 60.",
                "explanation_uz": "Internet terminallari — har tashrifda 30 daqiqa bepul, 60 emas.",
            },
        ],
    },
    {
        "title_de": "Interview: Ernährungstrends in Deutschland",
        "title_ru": "Интервью: тенденции питания в Германии",
        "task_type": "choice",
        "instruction_de": "Lesen Sie das Interview und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте интервью и выберите правильный ответ.",
        "instruction_uz": "Intervyuni o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "Interview mit Ernährungsexpertin Dr. Müller\n\n"
            "Frage: Wie haben sich die Essgewohnheiten der Deutschen in den letzten Jahren verändert?\n"
            "Dr. Müller: Die größte Veränderung ist der Rückgang des Fleischkonsums. "
            "Vor zehn Jahren aß der durchschnittliche Deutsche fast 1 kg Fleisch pro Woche. "
            "Heute sind es nur noch 600 Gramm. Das ist zwar immer noch viel, aber die Richtung stimmt.\n\n"
            "Frage: Was treibt diesen Wandel an?\n"
            "Dr. Müller: Hauptsächlich Umweltbewusstsein und Gesundheitsgründe. "
            "Junge Menschen zwischen 20 und 35 Jahren sind besonders aktiv in diesem Bereich. "
            "Viele probieren vegane oder vegetarische Ernährung aus. "
            "Interessanterweise sind es oft nicht die Städter, sondern auch Menschen auf dem Land.\n\n"
            "Frage: Welche Lebensmittel werden mehr konsumiert?\n"
            "Dr. Müller: Pflanzliche Produkte wie Hülsenfrüchte, Nüsse und Tofu. "
            "Auch Hafermilch und andere Pflanzendrinks boomen. "
            "Der Umsatz ist in fünf Jahren um 300 Prozent gestiegen.\n\n"
            "Frage: Gibt es Herausforderungen?\n"
            "Dr. Müller: Ja. Viele gesündere Produkte sind teurer. "
            "Das ist eine soziale Frage: Wer kann sich gute Ernährung leisten? "
            "Hier ist die Politik gefragt — mit Subventionen für gesunde Lebensmittel."
        ),
        "time_limit": 480,
        "questions": [
            {
                "text": "Wie viel Fleisch aß der durchschnittliche Deutsche vor zehn Jahren pro Woche?",
                "type": "choice",
                "correct_answer": "Fast 1 kg",
                "options": [("500 g", False), ("Fast 1 kg", True), ("1,5 kg", False), ("800 g", False)],
                "explanation_ru": "В интервью: почти 1 кг мяса в неделю 10 лет назад.",
                "explanation_uz": "Intervyuda: o'n yil oldin haftada deyarli 1 kg go'sht.",
            },
            {
                "text": "Welche Altersgruppe engagiert sich laut Dr. Müller besonders für gesunde Ernährung?",
                "type": "choice",
                "correct_answer": "Menschen zwischen 20 und 35 Jahren",
                "options": [
                    ("Kinder unter 15 Jahren", False),
                    ("Menschen zwischen 20 und 35 Jahren", True),
                    ("Senioren über 60 Jahren", False),
                    ("Menschen zwischen 40 und 55 Jahren", False),
                ],
                "explanation_ru": "Молодые люди в возрасте 20–35 лет наиболее активны в этой области.",
                "explanation_uz": "20–35 yoshdagi yoshlar bu sohada eng faol.",
            },
            {
                "text": "Um wie viel Prozent ist der Umsatz von Pflanzendrinks in fünf Jahren gestiegen?",
                "type": "choice",
                "correct_answer": "Um 300 Prozent",
                "options": [("Um 100 Prozent", False), ("Um 200 Prozent", False), ("Um 300 Prozent", True), ("Um 400 Prozent", False)],
                "explanation_ru": "В интервью: рост продаж растительных напитков — 300% за 5 лет.",
                "explanation_uz": "Intervyuda: o'simlik ichimliklari savdosi 5 yilda 300% ga o'sdi.",
            },
            {
                "text": "Warum ist die Veränderung der Ernährungsgewohnheiten auch eine soziale Frage?",
                "type": "choice",
                "correct_answer": "Weil gesündere Produkte teurer sind und nicht alle sie sich leisten können",
                "options": [
                    ("Weil vegetarische Ernährung ungesund ist", False),
                    ("Weil gesündere Produkte teurer sind und nicht alle sie sich leisten können", True),
                    ("Weil es zu wenige Produkte gibt", False),
                    ("Weil die Deutschen zu wenig kochen", False),
                ],
                "explanation_ru": "Более здоровые продукты дороже, не все могут себе их позволить.",
                "explanation_uz": "Sog'liqqa foydali mahsulotlar qimmatroq, hammaning ham ularga pulì yo'q.",
            },
            {
                "text": "Was fordert Dr. Müller von der Politik?",
                "type": "choice",
                "correct_answer": "Subventionen für gesunde Lebensmittel",
                "options": [
                    ("Fleischverbot", False),
                    ("Subventionen für gesunde Lebensmittel", True),
                    ("Höhere Steuern auf alle Lebensmittel", False),
                    ("Pflicht zur vegetarischen Ernährung in Schulen", False),
                ],
                "explanation_ru": "Доктор Мюллер призывает к государственным субсидиям на здоровые продукты питания.",
                "explanation_uz": "Dr. Müller sog'lom oziq-ovqatga davlat subsidiyalarini talab qiladi.",
            },
        ],
    },
]

B1_SCHREIBEN = [
    {
        "title_de": "Einladung annehmen oder ablehnen",
        "title_ru": "Принять или отклонить приглашение",
        "task_type": "writing_free",
        "instruction_de": (
            "Ihre Freundin Lena lädt Sie zu ihrer Geburtstagsfeier am Samstag ein. "
            "Sie können leider nicht kommen (Sie haben einen anderen Termin oder sind krank). "
            "Schreiben Sie Lena einen Brief / eine E-Mail (80–100 Wörter). "
            "Sagen Sie ab, erklären Sie den Grund, wünschen Sie ihr alles Gute "
            "und schlagen Sie ein alternatives Treffen vor."
        ),
        "instruction_ru": (
            "Ваша подруга Лена приглашает вас на вечеринку по случаю дня рождения в субботу. "
            "К сожалению, вы не можете прийти. "
            "Напишите Лене письмо / e-mail (80–100 слов). "
            "Откажитесь, объясните причину, поздравьте её и предложите альтернативную встречу."
        ),
        "instruction_uz": (
            "Do'stingiz Lena sizni shanba kuni tug'ilgan kuni bayramiga taklif qiladi. "
            "Afsuski, siz bora olmaysiz. "
            "Lenaga xat / e-mail yozing (80–100 so'z). "
            "Rad eting, sababini tushuntiring, tabrikang va muqobil uchrashuv taklif qiling."
        ),
        "text_content": "Aufgabe: Schreiben Sie eine Absage-Mail an Ihre Freundin Lena.",
        "time_limit": 1200,
        "extra": {
            "model_answer": (
                "Liebe Lena,\n\n"
                "herzlichen Dank für deine Einladung zu deiner Geburtstagsfeier! "
                "Ich freue mich sehr für dich.\n\n"
                "Leider muss ich absagen, weil ich am Samstag keine Zeit habe. "
                "Ich muss zu einem wichtigen Familienevent — meine Großeltern feiern ihre goldene Hochzeit. "
                "Ich hoffe, du verstehst das.\n\n"
                "Ich wünsche dir alles Gute zu deinem Geburtstag! "
                "Können wir uns nächste Woche zum Kaffee treffen? "
                "Dann überreiche ich dir auch dein Geschenk persönlich.\n\n"
                "Herzliche Grüße,\n[Name]"
            ),
            "checklist": [
                "Dank für die Einladung ausgedrückt?",
                "Klar abgesagt?",
                "Überzeugenden Grund genannt?",
                "Geburtstagswünsche formuliert?",
                "Alternatives Treffen vorgeschlagen?",
                "Angemessene Anrede und Abschluss?",
                "80–100 Wörter?",
            ],
            "redemittel": [
                "Liebe … / Herzlichen Dank für deine Einladung!",
                "Leider muss ich absagen, weil / denn …",
                "Es tut mir sehr leid, aber …",
                "Ich habe leider einen anderen Termin.",
                "Ich wünsche dir alles Gute / Herzlichen Glückwunsch zum Geburtstag!",
                "Können wir uns vielleicht … treffen?",
                "Herzliche Grüße / Liebe Grüße,",
            ],
            "word_count_min": 80,
            "word_count_max": 100,
        },
    },
    {
        "title_de": "Beschwerdebrief an den Vermieter",
        "title_ru": "Письмо-жалоба владельцу квартиры",
        "task_type": "writing_free",
        "instruction_de": (
            "In Ihrer Wohnung gibt es seit Wochen Probleme (z.B. kaputte Heizung, Lärm von Nachbarn, "
            "Wasserschaden). Schreiben Sie dem Vermieter einen formellen Brief (100–120 Wörter). "
            "Beschreiben Sie das Problem, erklären Sie die Folgen und fordern Sie eine Lösung."
        ),
        "instruction_ru": (
            "В вашей квартире уже несколько недель есть проблемы (например, сломанное отопление, "
            "шум от соседей, ущерб от воды). Напишите владельцу формальное письмо (100–120 слов). "
            "Опишите проблему, объясните последствия и потребуйте решения."
        ),
        "instruction_uz": (
            "Kvartiraizdayozda haftalar davomida muammolar mavjud (masalan, buzilgan isitish, "
            "qo'shnilarning shovqini, suv zarari). Uy egasiga rasmiy xat yozing (100–120 so'z). "
            "Muammoni tasvirlab bering, oqibatlarini tushuntiring va yechim talab qiling."
        ),
        "text_content": "Aufgabe: Schreiben Sie einen formellen Beschwerdebrief.",
        "time_limit": 1500,
        "extra": {
            "model_answer": (
                "Sehr geehrter Herr Schäfer,\n\n"
                "ich wende mich an Sie wegen eines ernsthaften Problems in meiner Wohnung (Nr. 4B). "
                "Seit drei Wochen ist die Heizung in meinem Schlafzimmer defekt. "
                "Ich habe Sie bereits zweimal telefonisch darüber informiert, ohne Ergebnis.\n\n"
                "Die Situation ist für mich sehr unangenehm: Nachts sind es nur 12 Grad im Zimmer. "
                "Das beeinträchtigt meine Gesundheit und meine Lebensqualität erheblich.\n\n"
                "Ich bitte Sie dringend, das Problem innerhalb der nächsten drei Tage zu beheben. "
                "Andernfalls sehe ich mich gezwungen, die Miete zu mindern.\n\n"
                "Mit freundlichen Grüßen,\n[Name]"
            ),
            "checklist": [
                "Formelle Anrede (Sehr geehrte/r …)?",
                "Problem klar und konkret beschrieben?",
                "Zeitraum erwähnt (seit wann)?",
                "Folgen / Auswirkungen beschrieben?",
                "Klare Forderung / Bitte um Lösung?",
                "Frist gesetzt?",
                "Formeller Abschluss (Mit freundlichen Grüßen)?",
                "100–120 Wörter?",
            ],
            "redemittel": [
                "Sehr geehrte/r …,",
                "ich wende mich an Sie wegen …",
                "Seit … Wochen / Tagen gibt es das Problem, dass …",
                "Trotz meiner Anfrage / Trotz mehrerer Hinweise …",
                "Die Situation ist … und beeinträchtigt …",
                "Ich bitte Sie dringend, … zu beheben / zu lösen.",
                "Ich erwarte eine Antwort bis …",
                "Andernfalls sehe ich mich gezwungen, …",
                "Mit freundlichen Grüßen,",
            ],
            "word_count_min": 100,
            "word_count_max": 120,
        },
    },
    {
        "title_de": "Stellungnahme: Für und gegen Homeoffice",
        "title_ru": "Эссе: за и против работы из дома",
        "task_type": "writing_free",
        "instruction_de": (
            "Ihr Arbeitgeber fragt die Mitarbeiter: Soll Homeoffice dauerhaft erlaubt werden? "
            "Schreiben Sie Ihre Meinung (100–130 Wörter). "
            "Nennen Sie mindestens zwei Vor- und zwei Nachteile von Homeoffice."
        ),
        "instruction_ru": (
            "Ваш работодатель спрашивает сотрудников: следует ли разрешить постоянную удалённую работу? "
            "Напишите своё мнение (100–130 слов). "
            "Назовите минимум два преимущества и два недостатка удалённой работы."
        ),
        "instruction_uz": (
            "Ish beruvchingiz xodimlardan so'raydi: masofaviy ish doimiy ruxsat etilsinmi? "
            "Fikringizni yozing (100–130 so'z). "
            "Masofaviy ishning kamida ikki afzalligi va ikki kamchiligini keltiring."
        ),
        "text_content": "Aufgabe: Schreiben Sie eine Stellungnahme zum Thema Homeoffice.",
        "time_limit": 1800,
        "extra": {
            "model_answer": (
                "Zum Thema Homeoffice habe ich eine differenzierte Meinung.\n\n"
                "Auf der einen Seite bietet Homeoffice viele Vorteile: "
                "Man spart Zeit und Geld für den Weg zur Arbeit. "
                "Außerdem kann man in einer ruhigen Umgebung konzentrierter arbeiten. "
                "Für Eltern mit kleinen Kindern ist es besonders praktisch, "
                "weil sie Arbeit und Familie besser koordinieren können.\n\n"
                "Auf der anderen Seite gibt es auch Nachteile. "
                "Der Kontakt zu Kollegen fehlt, was die Teamarbeit erschwert. "
                "Außerdem ist es für viele Menschen schwer, zu Hause die Grenzen zwischen "
                "Arbeit und Freizeit zu ziehen.\n\n"
                "Meiner Meinung nach sollte Homeoffice möglich sein, aber nicht Pflicht. "
                "Eine Mischung aus Büro und Homeoffice ist ideal."
            ),
            "checklist": [
                "Einleitung mit persönlicher Position?",
                "Mindestens 2 Vorteile von Homeoffice genannt?",
                "Mindestens 2 Nachteile von Homeoffice genannt?",
                "Eigene Meinung / Fazit formuliert?",
                "Strukturierter Text (Absätze)?",
                "100–130 Wörter?",
            ],
            "redemittel": [
                "Zum Thema … habe ich eine differenzierte / klare Meinung.",
                "Auf der einen Seite … / Auf der anderen Seite …",
                "Ein wichtiger Vorteil ist, dass …",
                "Ein Nachteil / Problem ist, dass …",
                "Außerdem … / Darüber hinaus …",
                "Meiner Meinung nach / Ich bin der Meinung, dass …",
                "Alles in allem / Insgesamt denke ich, dass …",
            ],
            "word_count_min": 100,
            "word_count_max": 130,
        },
    },
]


# ── B2 CONTENT ────────────────────────────────────────────────────────────────

B2_LESEN = [
    {
        "title_de": "Digitalisierung und die Zukunft der Arbeit",
        "title_ru": "Цифровизация и будущее труда",
        "task_type": "choice",
        "instruction_de": "Lesen Sie den Text und wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте текст и выберите правильный ответ.",
        "instruction_uz": "Matnni o'qing va to'g'ri javobni tanlang.",
        "text_content": (
            "Digitalisierung und die Zukunft der Arbeit\n\n"
            "Die Digitalisierung verändert die Arbeitswelt grundlegend. Laut einer Studie "
            "des Instituts für Arbeitsmarkt- und Berufsforschung (IAB) könnten in den nächsten "
            "zwanzig Jahren bis zu 35 Prozent aller Arbeitsplätze in Deutschland durch "
            "Automatisierung und künstliche Intelligenz substituiert werden. Besonders betroffen "
            "sind Routinetätigkeiten in der Verwaltung, im Einzelhandel und in der Logistik.\n\n"
            "Gleichzeitig entstehen neue Berufsfelder: Data Scientists, KI-Trainer und "
            "Cyber-Sicherheitsexperten sind bereits heute gefragte Fachkräfte. Experten "
            "betonen, dass lebenslanges Lernen und digitale Kompetenzen entscheidend sein "
            "werden, um auf dem Arbeitsmarkt konkurrenzfähig zu bleiben.\n\n"
            "Kritisch zu sehen ist jedoch die soziale Dimension dieser Entwicklung: "
            "Geringqualifizierte Arbeitnehmer tragen das höchste Risiko, ihren Arbeitsplatz "
            "zu verlieren. Dies könnte die gesellschaftliche Ungleichheit verschärfen, wenn "
            "der Staat nicht mit gezielten Umschulungsprogrammen und sozialen Absicherungen "
            "gegensteuert.\n\n"
            "Bildungsökonomen plädieren daher für eine fundamentale Reform des Bildungssystems. "
            "Statt reiner Wissensvermittlung müssen Schulen und Universitäten kritisches Denken, "
            "Kreativität und soziale Kompetenzen stärker fördern — Fähigkeiten, die Maschinen "
            "noch nicht replizieren können."
        ),
        "time_limit": 600,
        "questions": [
            {
                "text": "Welcher Prozentsatz der Arbeitsplätze könnte laut IAB durch Automatisierung gefährdet sein?",
                "type": "choice",
                "correct_answer": "Bis zu 35 Prozent",
                "options": [("25 Prozent", False), ("30 Prozent", False), ("Bis zu 35 Prozent", True), ("40 Prozent", False)],
                "explanation_ru": "По данным IAB, под угрозой до 35% всех рабочих мест.",
                "explanation_uz": "IAB ma'lumotlariga ko'ra, barcha ish joylarining 35% gacha xavf ostida.",
            },
            {
                "text": "Welche Berufsgruppe trägt das höchste Risiko durch Automatisierung?",
                "type": "choice",
                "correct_answer": "Geringqualifizierte Arbeitnehmer",
                "options": [
                    ("Hochqualifizierte Fachkräfte", False),
                    ("Geringqualifizierte Arbeitnehmer", True),
                    ("Führungskräfte", False),
                    ("Freiberufler", False),
                ],
                "explanation_ru": "Низкоквалифицированные работники несут наибольший риск потери работы.",
                "explanation_uz": "Past malakali ishchilar ish yo'qotishning eng yuqori xavfiga duchor bo'ladi.",
            },
            {
                "text": "Was fordern Bildungsökonomen laut dem Text?",
                "type": "choice",
                "correct_answer": "Eine Reform des Bildungssystems mit Fokus auf kritisches Denken und Kreativität",
                "options": [
                    ("Mehr Wissensvermittlung im Unterricht", False),
                    ("Weniger Technologieeinsatz in Schulen", False),
                    ("Eine Reform des Bildungssystems mit Fokus auf kritisches Denken und Kreativität", True),
                    ("Höhere Investitionen ausschließlich in Berufsausbildung", False),
                ],
                "explanation_ru": "Образовательные экономисты призывают к реформе образования с акцентом на критическое мышление и творчество.",
                "explanation_uz": "Ta'lim iqtisodchilari tanqidiy fikrlash va ijodkorlikka e'tibor qaratgan ta'lim islohotini talab qilmoqda.",
            },
            {
                "text": "Welche der folgenden Berufsgruppen wird im Text als neue Berufsgruppe erwähnt?",
                "type": "choice",
                "correct_answer": "Data Scientists",
                "options": [("Buchhalter", False), ("Data Scientists", True), ("Lehrer", False), ("Ingenieure", False)],
                "explanation_ru": "Data Scientists, тренеры ИИ и специалисты по кибербезопасности — новые профессии.",
                "explanation_uz": "Data Scientists, sun'iy intellekt trenerlar va kiberhavfsizlik mutaxassislari — yangi kasblar.",
            },
            {
                "text": "Was schlägt der Text vor, um soziale Ungleichheit durch Digitalisierung zu bekämpfen?",
                "type": "choice",
                "correct_answer": "Staatliche Umschulungsprogramme und soziale Absicherungen",
                "options": [
                    ("Steuersenkungen für Unternehmen", False),
                    ("Staatliche Umschulungsprogramme und soziale Absicherungen", True),
                    ("Begrenzung der Automatisierung per Gesetz", False),
                    ("Höhere Löhne für alle Berufsgruppen", False),
                ],
                "explanation_ru": "Государственные программы переобучения и социальная защита для противодействия неравенству.",
                "explanation_uz": "Tengsizlikka qarshi davlat qayta tayyorlash dasturlari va ijtimoiy kafolatlar.",
            },
        ],
    },
    {
        "title_de": "Kommentar: Homeoffice — Fluch oder Segen?",
        "title_ru": "Комментарий: удалённая работа — проклятие или благо?",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie den Kommentar. Sind die Aussagen richtig oder falsch?",
        "instruction_ru": "Прочитайте комментарий. Правильные или нет?",
        "instruction_uz": "Izohni o'qing. To'g'ri yoki noto'g'ri?",
        "text_content": (
            "Homeoffice: Zwischen Freiheit und Vereinsamung\n\n"
            "Seit der Pandemie ist Homeoffice für Millionen von Deutschen zur Normalität geworden. "
            "Doch während die einen die Flexibilität und Zeitersparnis loben, warnen Experten "
            "vor den psychologischen Folgen dauerhafter Isolation.\n\n"
            "Eine Studie der Universität München ergab, dass 43 Prozent der befragten Arbeitnehmer "
            "im Homeoffice unter Einsamkeit leiden — ein Anstieg von 28 Prozent im Vergleich "
            "zur Vorkrisenszeit. Besonders betroffen sind junge Berufseinsteiger, die in der "
            "Büroumgebung wichtige soziale Fähigkeiten erwerben könnten.\n\n"
            "Arbeitgeberverbände betonen dagegen die Produktivitätsgewinne: In Branchen wie IT, "
            "Finanzen und Beratung stieg die Produktivität um durchschnittlich 13 Prozent. "
            "Gleichzeitig klagen Unternehmen über höhere Kosten für IT-Infrastruktur und "
            "Cybersicherheit.\n\n"
            "Die Lösung liegt möglicherweise im 'hybriden Arbeiten': zwei bis drei Tage im Büro, "
            "der Rest zu Hause. Dieses Modell kombiniert die sozialen Vorteile der Präsenzarbeit "
            "mit der Flexibilität des Homeoffice und wird von 67 Prozent der Arbeitnehmer bevorzugt."
        ),
        "time_limit": 540,
        "questions": [
            {
                "text": "Laut der Münchener Studie leiden 43 Prozent der Homeoffice-Arbeitnehmer unter Einsamkeit.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "В тексте написано: 43% опрошенных работников страдают от одиночества.",
                "explanation_uz": "Matnda yozilgan: so'rovda qatnashgan ishchilarning 43% yolg'izlikdan aziyat chekadi.",
            },
            {
                "text": "Besonders betroffen von Einsamkeit im Homeoffice sind erfahrene Führungskräfte.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте: особенно затронуты молодые люди, начинающие карьеру.",
                "explanation_uz": "Matnda: ayniqsa kasb yo'lini endigina boshlagan yoshlar ta'sirlangan.",
            },
            {
                "text": "In der IT-Branche sank die Produktivität durch Homeoffice.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Наоборот: производительность выросла в среднем на 13%.",
                "explanation_uz": "Aksincha: mahsuldorlik o'rtacha 13% ga o'sdi.",
            },
            {
                "text": "Unternehmen haben durch Homeoffice keine zusätzlichen Kosten.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте: компании жалуются на более высокие расходы на IT и кибербезопасность.",
                "explanation_uz": "Matnda: kompaniyalar IT va kiberhavfsizlikka ko'proq xarajat qilishmoqda.",
            },
            {
                "text": "Das hybride Arbeitsmodell wird von der Mehrheit der Arbeitnehmer bevorzugt.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "67% работников предпочитают гибридную модель работы.",
                "explanation_uz": "Ishchilarning 67% gibrid ish modelini afzal ko'radi.",
            },
        ],
    },
    {
        "title_de": "Mehrsprachigkeit in Europa",
        "title_ru": "Многоязычие в Европе",
        "task_type": "choice",
        "instruction_de": "Lesen Sie den Sachtext. Wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте текст. Выберите правильный ответ.",
        "instruction_uz": "Matnni o'qing. To'g'ri javobni tanlang.",
        "text_content": (
            "Mehrsprachigkeit: Bereicherung oder Herausforderung?\n\n"
            "Europa ist ein Kontinent der Sprachen: Die Europäische Union erkennt offiziell "
            "24 Sprachen an, in der Praxis sprechen die Menschen jedoch über 200 Regional- "
            "und Minderheitensprachen. Mehrsprachigkeit ist in Europa keine Ausnahme, "
            "sondern die Regel.\n\n"
            "Neurowissenschaftliche Forschungen belegen, dass das Erlernen mehrerer Sprachen "
            "kognitive Vorteile mit sich bringt. Mehrsprachige Menschen weisen im Durchschnitt "
            "eine höhere Konzentrationsfähigkeit auf und zeigen im Alter eine um bis zu "
            "vier Jahre verzögerte Demenz-Symptomatik. Außerdem erhöhen Fremdsprachenkenntnisse "
            "die beruflichen Chancen erheblich: Laut EU-Statistiken verdienen mehrsprachige "
            "Arbeitnehmer durchschnittlich 11 Prozent mehr als einsprachige Kollegen.\n\n"
            "Kritiker wenden ein, dass übertriebener Sprachfokus in der Schule zu Lasten anderer "
            "Fächer geht. Außerdem bestehe die Gefahr der 'Halbsprachigkeit' — dem unvollständigen "
            "Beherrschen mehrerer Sprachen ohne tiefes Verständnis einer einzigen.\n\n"
            "Die meisten Sprachforscher sind sich dennoch einig: Eine gut gestaltete "
            "Mehrsprachigkeitspolitik, die Mehrheitsprache und Minderheitensprachen gleichermaßen "
            "fördert, bringt sowohl kulturellen als auch wirtschaftlichen Nutzen."
        ),
        "time_limit": 600,
        "questions": [
            {
                "text": "Wie viele Sprachen erkennt die EU offiziell an?",
                "type": "choice",
                "correct_answer": "24 Sprachen",
                "options": [("12 Sprachen", False), ("24 Sprachen", True), ("50 Sprachen", False), ("200 Sprachen", False)],
                "explanation_ru": "ЕС официально признаёт 24 языка.",
                "explanation_uz": "Yevropa Ittifoqi rasman 24 tilni tan oladi.",
            },
            {
                "text": "Um wie viele Jahre können Mehrsprachige laut dem Text den Beginn von Demenzsymptomen verzögern?",
                "type": "choice",
                "correct_answer": "Bis zu 4 Jahre",
                "options": [("Bis zu 2 Jahre", False), ("Bis zu 4 Jahre", True), ("Bis zu 6 Jahre", False), ("Bis zu 10 Jahre", False)],
                "explanation_ru": "В тексте: признаки деменции откладываются до 4 лет.",
                "explanation_uz": "Matnda: demans belgilari 4 yilgacha kechikadi.",
            },
            {
                "text": "Wie viel mehr verdienen mehrsprachige Arbeitnehmer laut EU-Statistiken?",
                "type": "choice",
                "correct_answer": "Durchschnittlich 11 Prozent mehr",
                "options": [("5 Prozent mehr", False), ("Durchschnittlich 11 Prozent mehr", True), ("15 Prozent mehr", False), ("20 Prozent mehr", False)],
                "explanation_ru": "Многоязычные работники зарабатывают в среднем на 11% больше.",
                "explanation_uz": "Ko'p tilli ishchilar o'rtacha 11% ko'proq ishlaydi.",
            },
            {
                "text": "Was bedeutet 'Halbsprachigkeit' im Kontext des Textes?",
                "type": "choice",
                "correct_answer": "Das unvollständige Beherrschen mehrerer Sprachen ohne tiefes Verständnis einer einzigen",
                "options": [
                    ("Das Sprechen von genau zwei Sprachen", False),
                    ("Das unvollständige Beherrschen mehrerer Sprachen ohne tiefes Verständnis einer einzigen", True),
                    ("Das Lernen von Sprachen im Schulalter", False),
                    ("Das Vergessen der Muttersprache", False),
                ],
                "explanation_ru": "«Полуязычие» — неполное владение несколькими языками без глубокого знания ни одного.",
                "explanation_uz": "'Yarim tillilik' — bir necha tilni biron birini chuqur bilmasdan to'liq egallolmaslik.",
            },
            {
                "text": "Welche Position vertreten die meisten Sprachforscher laut dem Text?",
                "type": "choice",
                "correct_answer": "Gut gestaltete Mehrsprachigkeitspolitik bringt kulturellen und wirtschaftlichen Nutzen",
                "options": [
                    ("Mehrsprachigkeit schadet der Bildung", False),
                    ("Gut gestaltete Mehrsprachigkeitspolitik bringt kulturellen und wirtschaftlichen Nutzen", True),
                    ("Kinder sollten nur eine Sprache lernen", False),
                    ("Minderheitensprachen sollten nicht gefördert werden", False),
                ],
                "explanation_ru": "Большинство языковедов считают: хорошо организованная языковая политика полезна как культурно, так и экономически.",
                "explanation_uz": "Ko'p tilshunoslar: yaxshi tashkil etilgan til siyosati madaniy va iqtisodiy jihatdan foydali.",
            },
        ],
    },
    {
        "title_de": "Stadtentwicklung und Gentrifizierung",
        "title_ru": "Городское развитие и джентрификация",
        "task_type": "truefalse",
        "instruction_de": "Lesen Sie den Essay. Richtig oder falsch?",
        "instruction_ru": "Прочитайте эссе. Правильно или нет?",
        "instruction_uz": "Inshoni o'qing. To'g'ri yoki noto'g'ri?",
        "text_content": (
            "Gentrifizierung: Wenn die Stadt sich neu erfindet\n\n"
            "Gentrifizierung beschreibt den Prozess, bei dem einkommensschwache Bewohner aus "
            "ihren angestammten Stadtvierteln verdrängt werden, weil steigende Mieten und "
            "Sanierungen das Viertel für wohlhabendere Bevölkerungsschichten attraktiver machen. "
            "Das Phänomen ist in deutschen Großstädten wie Berlin, Hamburg und München besonders "
            "ausgeprägt.\n\n"
            "Befürworter der Stadtentwicklung betonen die positiven Aspekte: Renovierte Gebäude, "
            "bessere Infrastruktur, weniger Kriminalität und neue Arbeitsplätze. "
            "In Hamburg-Altona beispielsweise verwandelte sich ein ehemaliges Industriegebiet "
            "innerhalb von zehn Jahren in ein begehrtes Wohnviertel mit hoher Lebensqualität.\n\n"
            "Kritiker hingegen sehen darin eine Form sozialer Ungerechtigkeit. "
            "Langjährige Bewohner — oft Migranten, Rentner und Geringverdiener — können sich "
            "die steigenden Mieten nicht mehr leisten und müssen in Randgebiete ziehen. "
            "Damit geht auch die kulturelle Vielfalt verloren, die das Viertel ursprünglich "
            "geprägt hatte.\n\n"
            "Stadtplaner fordern daher eine 'sozialverträgliche Stadtentwicklung': "
            "Mietpreisbremsen, Sozialwohnungsquoten und Bürgerbeteiligung bei Planungsprozessen "
            "sollen sicherstellen, dass die Modernisierung nicht auf Kosten der schwächsten "
            "Bevölkerungsgruppen geht."
        ),
        "time_limit": 540,
        "questions": [
            {
                "text": "Gentrifizierung bezeichnet den Prozess, bei dem ärmere Bewohner aus ihren Stadtvierteln verdrängt werden.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "Именно так определяется джентрификация в тексте.",
                "explanation_uz": "Matnda gentifikatsiya aynan shunday ta'riflanadi.",
            },
            {
                "text": "Das Phänomen der Gentrifizierung ist in deutschen Kleinstädten am stärksten.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "В тексте: явление особенно выражено в крупных городах — Берлин, Гамбург, Мюнхен.",
                "explanation_uz": "Matnda: hodisa yirik shaharlarda — Berlin, Gamburg, Myunxenda ayniqsa kuchli.",
            },
            {
                "text": "Befürworter der Gentrifizierung sehen keine positiven Aspekte in diesem Prozess.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Наоборот: сторонники видят плюсы — отремонтированные здания, инфраструктура, меньше преступности.",
                "explanation_uz": "Aksincha: tarafdorlar ijobiy tomonlarni ko'radi — ta'mirlangan binolar, infratuzilma, kamroq jinoyat.",
            },
            {
                "text": "Durch Gentrifizierung kann die kulturelle Vielfalt eines Stadtteils verloren gehen.",
                "type": "truefalse",
                "correct_answer": "Richtig",
                "options": [("Richtig", True), ("Falsch", False)],
                "explanation_ru": "В тексте: вместе с коренными жителями уходит и культурное разнообразие.",
                "explanation_uz": "Matnda: mahalliy aholining ketishi bilan madaniy xilma-xillik ham yo'qoladi.",
            },
            {
                "text": "Stadtplaner fordern eine vollständige Verhinderung von Stadtentwicklung.",
                "type": "truefalse",
                "correct_answer": "Falsch",
                "options": [("Richtig", False), ("Falsch", True)],
                "explanation_ru": "Не остановку развития, а 'социально приемлемое развитие города'.",
                "explanation_uz": "Rivojlanishni to'xtatish emas, 'ijtimoiy maqbul shahar rivojlanishi' talab qilinadi.",
            },
        ],
    },
    {
        "title_de": "Wissenschaftstext: Schlaf und Gesundheit",
        "title_ru": "Научный текст: сон и здоровье",
        "task_type": "choice",
        "instruction_de": "Lesen Sie den Wissenschaftstext. Wählen Sie die richtige Antwort.",
        "instruction_ru": "Прочитайте научный текст. Выберите правильный ответ.",
        "instruction_uz": "Ilmiy matnni o'qing. To'g'ri javobni tanlang.",
        "text_content": (
            "Schlaf: Das unterschätzte Fundament der Gesundheit\n\n"
            "Schlaf ist weit mehr als eine passive Erholungsphase. Während wir schlafen, "
            "vollziehen sich im Körper lebenswichtige Prozesse: Das Immunsystem wird gestärkt, "
            "Erinnerungen werden konsolidiert und Schadstoffe im Gehirn abgebaut.\n\n"
            "Die Deutsche Gesellschaft für Schlafforschung empfiehlt Erwachsenen sieben bis neun "
            "Stunden Schlaf pro Nacht. Doch Studien zeigen, dass 34 Prozent der Deutschen "
            "chronisch unter Schlafmangel leiden — mit weitreichenden Folgen: Ein regelmäßiger "
            "Schlaf von unter sechs Stunden erhöht das Risiko für Herzerkrankungen um 48 Prozent "
            "und das Diabetesrisiko um 36 Prozent.\n\n"
            "Neuere Forschungen der Universität Berkeley deuten darauf hin, dass Schlafmangel "
            "auch das emotionale Gleichgewicht stört. Menschen, die weniger als sieben Stunden "
            "schlafen, reagieren auf negative Reize deutlich sensitiver und zeigen ein "
            "erhöhtes Angstniveau.\n\n"
            "Besonders problematisch ist der Einfluss digitaler Medien auf den Schlaf. "
            "Das blaue Licht von Smartphones und Tablets hemmt die Ausschüttung von Melatonin, "
            "dem Schlafhormon. Experten empfehlen daher, elektronische Geräte mindestens "
            "60 Minuten vor dem Schlafengehen wegzulegen."
        ),
        "time_limit": 600,
        "questions": [
            {
                "text": "Wie viele Stunden Schlaf empfiehlt die Deutsche Gesellschaft für Schlafforschung für Erwachsene?",
                "type": "choice",
                "correct_answer": "Sieben bis neun Stunden",
                "options": [("Fünf bis sieben Stunden", False), ("Sieben bis neun Stunden", True), ("Acht bis zehn Stunden", False), ("Sechs bis acht Stunden", False)],
                "explanation_ru": "Рекомендация: 7–9 часов сна для взрослых.",
                "explanation_uz": "Tavsiya: kattalar uchun 7–9 soat uyqu.",
            },
            {
                "text": "Wie hoch ist der Anteil der Deutschen, die chronisch unter Schlafmangel leiden?",
                "type": "choice",
                "correct_answer": "34 Prozent",
                "options": [("20 Prozent", False), ("34 Prozent", True), ("45 Prozent", False), ("50 Prozent", False)],
                "explanation_ru": "В тексте: 34% немцев хронически страдают от недосыпания.",
                "explanation_uz": "Matnda: nemislarning 34% surunkali uyqu yetishmasligidan aziyat chekadi.",
            },
            {
                "text": "Um wie viel Prozent erhöht chronischer Schlafmangel (unter 6 Stunden) das Herzerkrankungsrisiko?",
                "type": "choice",
                "correct_answer": "Um 48 Prozent",
                "options": [("Um 28 Prozent", False), ("Um 36 Prozent", False), ("Um 48 Prozent", True), ("Um 60 Prozent", False)],
                "explanation_ru": "Риск сердечных заболеваний увеличивается на 48%.",
                "explanation_uz": "Yurak kasalliklari xavfi 48% ga oshadi.",
            },
            {
                "text": "Was ist laut dem Text die Wirkung von blauem Licht auf den Schlaf?",
                "type": "choice",
                "correct_answer": "Es hemmt die Ausschüttung von Melatonin",
                "options": [
                    ("Es fördert das Einschlafen", False),
                    ("Es hemmt die Ausschüttung von Melatonin", True),
                    ("Es hat keinen Einfluss auf den Schlaf", False),
                    ("Es verbessert die Schlafqualität", False),
                ],
                "explanation_ru": "Синий свет подавляет выработку мелатонина — гормона сна.",
                "explanation_uz": "Ko'k yorug'lik melatonin — uyqu gormoni ishlab chiqarilishini to'xtatadi.",
            },
            {
                "text": "Wie lange vor dem Schlafen sollen Smartphones laut Experten weggelegt werden?",
                "type": "choice",
                "correct_answer": "Mindestens 60 Minuten",
                "options": [("30 Minuten", False), ("Mindestens 60 Minuten", True), ("90 Minuten", False), ("2 Stunden", False)],
                "explanation_ru": "Эксперты рекомендуют убирать устройства минимум за 60 минут до сна.",
                "explanation_uz": "Mutaxassislar qurilmalarni uxlashdan kamida 60 daqiqa oldin olishni tavsiya qiladi.",
            },
        ],
    },
]

B2_SCHREIBEN = [
    {
        "title_de": "Argumentativer Aufsatz: Soziale Medien",
        "title_ru": "Аргументативное эссе: социальные сети",
        "task_type": "writing_free",
        "instruction_de": (
            "Schreiben Sie einen argumentativen Aufsatz (150–180 Wörter) zum Thema: "
            "'Soziale Medien — Fluch oder Segen für die Gesellschaft?' "
            "Nehmen Sie klar Stellung, nennen Sie Argumente und Gegenargumente "
            "und kommen Sie zu einem begründeten Schluss."
        ),
        "instruction_ru": (
            "Напишите аргументативное эссе (150–180 слов) на тему: "
            "«Социальные сети — проклятие или благо для общества?» "
            "Чётко выразите свою позицию, приведите аргументы и контраргументы, "
            "сделайте обоснованный вывод."
        ),
        "instruction_uz": (
            "Mavzuda argumentativ insha yozing (150–180 so'z): "
            "'Ijtimoiy tarmoqlar — jamiyat uchun la'nat yoki ne'mat?' "
            "Aniq pozitsiya belgilang, dalil va qarshi dalillar keltiring "
            "va asosli xulosa chiqaring."
        ),
        "text_content": "Aufgabe: Argumentativer Aufsatz zum Thema 'Soziale Medien'.",
        "time_limit": 2400,
        "extra": {
            "model_answer": (
                "Soziale Medien sind aus unserem Alltag nicht mehr wegzudenken. "
                "Sie bieten enorme Möglichkeiten, werfen aber auch ernste Fragen auf.\n\n"
                "Für soziale Medien spricht zunächst ihre Funktion als globales Kommunikationsmittel: "
                "Familien, die auf verschiedenen Kontinenten leben, bleiben in Kontakt. "
                "Außerdem democratisieren sie den Zugang zu Informationen und ermöglichen "
                "Menschen ohne Stimme — Minderheiten, Aktivisten — öffentliche Präsenz.\n\n"
                "Andererseits sind die Risiken erheblich. Algorithmen verstärken Filterblasen "
                "und politische Radikalisierung. Studien belegen einen Zusammenhang zwischen "
                "exzessiver Social-Media-Nutzung und psychischen Erkrankungen, besonders bei Jugendlichen. "
                "Desinformation verbreitet sich schneller als Korrekturen.\n\n"
                "Meiner Überzeugung nach überwiegen langfristig die Risiken, wenn keine Regulierung erfolgt. "
                "Plattformbetreiber tragen Verantwortung — Transparenz bei Algorithmen und "
                "strikte Alterskontrollen sind überfällig. "
                "Soziale Medien können nützlich sein, aber nur mit klaren Regeln."
            ),
            "checklist": [
                "Klare Einleitung mit Positionierung?",
                "Mindestens 2 Argumente für soziale Medien?",
                "Mindestens 2 Argumente gegen soziale Medien?",
                "Logische Struktur (Einleitung, Hauptteil, Schluss)?",
                "Abschlussfazit mit begründeter eigener Meinung?",
                "Formell-neutraler Stil?",
                "150–180 Wörter?",
            ],
            "redemittel": [
                "… sind aus unserem Alltag nicht mehr wegzudenken.",
                "Für … spricht zunächst / Dagegen spricht jedoch …",
                "Einerseits … / Andererseits …",
                "Studien belegen / zeigen, dass …",
                "Ein weiteres Argument ist, dass …",
                "Meiner Überzeugung nach / Insgesamt bin ich der Meinung, dass …",
                "Langfristig / Kurzfristig …",
                "Es bleibt festzuhalten, dass …",
            ],
            "word_count_min": 150,
            "word_count_max": 180,
        },
    },
    {
        "title_de": "Formelles Bewerbungsschreiben",
        "title_ru": "Официальное сопроводительное письмо",
        "task_type": "writing_free",
        "instruction_de": (
            "Sie bewerben sich um eine Stelle als Marketing-Assistent/in bei einem deutschen Unternehmen. "
            "Schreiben Sie ein Bewerbungsschreiben (150–180 Wörter). "
            "Erklären Sie Ihre Motivation, nennen Sie relevante Qualifikationen "
            "und zeigen Sie Ihr Interesse am Unternehmen."
        ),
        "instruction_ru": (
            "Вы подаёте заявку на должность ассистента по маркетингу в немецкой компании. "
            "Напишите сопроводительное письмо (150–180 слов). "
            "Объясните мотивацию, назовите соответствующую квалификацию "
            "и выразите интерес к компании."
        ),
        "instruction_uz": (
            "Siz Germaniya kompaniyasida marketing yordamchisi lavozimiga ariza berasiz. "
            "Ilova xat yozing (150–180 so'z). "
            "Motivatsiyangizni tushuntiring, tegishli malakangizni ko'rsating "
            "va kompaniyaga qiziqishingizni bildiring."
        ),
        "text_content": "Aufgabe: Schreiben Sie ein formelles Bewerbungsschreiben.",
        "time_limit": 2400,
        "extra": {
            "model_answer": (
                "Sehr geehrte Damen und Herren,\n\n"
                "mit großem Interesse habe ich Ihre Stellenanzeige für die Position als "
                "Marketing-Assistent/in gelesen. Ich bewerbe mich hiermit für diese Stelle.\n\n"
                "Ich verfüge über einen Bachelor-Abschluss in Betriebswirtschaft mit Schwerpunkt "
                "Marketing sowie über zwei Jahre Berufserfahrung in einer Werbeagentur. "
                "In dieser Zeit habe ich Erfahrungen in der Social-Media-Kommunikation, "
                "Kampagnenplanung und Marktanalyse gesammelt. Meine Deutschkenntnisse "
                "entsprechen dem Niveau C1.\n\n"
                "Besonders ansprechend finde ich Ihr Unternehmen, weil es für innovative "
                "Marketingstrategien bekannt ist und internationale Projekte realisiert. "
                "Ich bin überzeugt, dass ich mit meinem Engagement und meiner Kreativität "
                "einen wertvollen Beitrag zu Ihrem Team leisten kann.\n\n"
                "Über eine Einladung zu einem Vorstellungsgespräch würde ich mich sehr freuen.\n\n"
                "Mit freundlichen Grüßen,\n[Name]"
            ),
            "checklist": [
                "Formelle Anrede (Sehr geehrte Damen und Herren)?",
                "Bezug auf Stellenanzeige?",
                "Qualifikationen/Erfahrungen konkret genannt?",
                "Motivation und Interesse am Unternehmen erklärt?",
                "Bitte um Einladung zum Gespräch?",
                "Formeller Abschluss?",
                "Professioneller, formeller Ton?",
                "150–180 Wörter?",
            ],
            "redemittel": [
                "Sehr geehrte Damen und Herren,",
                "mit großem Interesse habe ich … gelesen.",
                "Ich bewerbe mich hiermit für die Stelle als …",
                "Ich verfüge über … / Ich habe … Jahre Erfahrung in …",
                "Besonders reizvoll / ansprechend finde ich …, weil …",
                "Ich bin überzeugt, dass ich … beitragen kann.",
                "Über eine Einladung zum Vorstellungsgespräch würde ich mich freuen.",
                "Mit freundlichen Grüßen,",
            ],
            "word_count_min": 150,
            "word_count_max": 180,
        },
    },
    {
        "title_de": "Diskussionsbeitrag: Pflichtjahr für junge Menschen",
        "title_ru": "Дискуссионный вклад: обязательный год службы",
        "task_type": "writing_free",
        "instruction_de": (
            "In einer Online-Diskussion lautet die Frage: "
            "'Sollte ein soziales Pflichtjahr für alle jungen Menschen eingeführt werden?' "
            "Schreiben Sie Ihren Beitrag (150–180 Wörter). "
            "Nehmen Sie klar Stellung und begründen Sie Ihre Meinung mit Beispielen."
        ),
        "instruction_ru": (
            "В онлайн-дискуссии звучит вопрос: "
            "«Должен ли быть введён обязательный социальный год для всех молодых людей?» "
            "Напишите свой вклад (150–180 слов). "
            "Чётко выразите позицию и обоснуйте мнение примерами."
        ),
        "instruction_uz": (
            "Onlayn munozarada savol: "
            "'Barcha yoshlar uchun majburiy ijtimoiy yil joriy etilishi kerakmi?' "
            "Hissangizni yozing (150–180 so'z). "
            "Aniq pozitsiya bildiring va misollar bilan asoslang."
        ),
        "text_content": "Aufgabe: Schreiben Sie einen Diskussionsbeitrag zum Thema 'Soziales Pflichtjahr'.",
        "time_limit": 2400,
        "extra": {
            "model_answer": (
                "Ich unterstütze die Idee eines sozialen Pflichtjahres — mit einigen wichtigen Einschränkungen.\n\n"
                "Ein verpflichtendes Engagement in sozialen Einrichtungen, im Umweltschutz oder "
                "im Katastrophenschutz hätte klare Vorteile: Junge Menschen würden gesellschaftliche "
                "Verantwortung hautnah erleben und Empathie für vulnerable Gruppen entwickeln. "
                "Gleichzeitig würden sie praktische Kompetenzen erwerben, die kein Klassenzimmer vermitteln kann. "
                "In Ländern wie Israel oder Südkorea, wo ähnliche Modelle existieren, ist das "
                "gesellschaftliche Zusammengehörigkeitsgefühl nachweislich stärker.\n\n"
                "Kritiker befürchten, Pflicht töte die Motivation. Dieser Einwand ist berechtigt: "
                "Erzwungenes Engagement bringt wenig. Deshalb wäre ein Modell mit Wahlmöglichkeiten "
                "sinnvoller — Pflicht dem Prinzip nach, aber Freiheit bei der Wahl des Bereichs.\n\n"
                "Fazit: Ein gut konzipiertes Pflichtjahr kann mehr Solidarität schaffen. "
                "Entscheidend ist die Ausgestaltung."
            ),
            "checklist": [
                "Klare Position zu Beginn?",
                "Mindestens 2 Argumente für das Pflichtjahr?",
                "Gegenargument mit eigener Reaktion darauf?",
                "Konkretes Beispiel oder Vergleich?",
                "Klares Fazit?",
                "Angemessener Diskussionsstil?",
                "150–180 Wörter?",
            ],
            "redemittel": [
                "Ich unterstütze / lehne … ab, weil …",
                "Ein entscheidender Vorteil ist, dass …",
                "Hinzu kommt, dass …",
                "Kritiker / Gegner argumentieren, dass …",
                "Dieser Einwand ist zwar berechtigt, jedoch …",
                "In Ländern wie … zeigt sich, dass …",
                "Abschließend bin ich der Überzeugung, dass …",
                "Entscheidend ist letztlich …",
            ],
            "word_count_min": 150,
            "word_count_max": 180,
        },
    },
]


# ── MAIN RUNNER ────────────────────────────────────────────────────────────────

CONTENT_MAP = {
    "A1": {
        "lesen":     A1_LESEN_EXTRA,
        "schreiben": A1_SCHREIBEN_EXTRA,
    },
    "A2": {
        "lesen":     A2_LESEN,
        "schreiben": A2_SCHREIBEN,
    },
    "B1": {
        "lesen":     B1_LESEN,
        "schreiben": B1_SCHREIBEN,
    },
    "B2": {
        "lesen":     B2_LESEN,
        "schreiben": B2_SCHREIBEN,
    },
}

PROVIDERS = ["goethe", "telc", "osd"]


def run():
    conn = _conn()
    inserted = 0
    skipped = 0

    for provider_name in PROVIDERS:
        for level, sections in CONTENT_MAP.items():
            for section_type, tasks in sections.items():
                sid = _get_section_id(conn, provider_name, level, section_type)
                if sid is None:
                    print(f"  ⚠️  Section not found: {provider_name}/{level}/{section_type}")
                    continue

                for task in tasks:
                    if task["task_type"] in ("writing_free", "writing_form"):
                        tid = _insert_schreiben_task(conn, sid, task)
                    else:
                        tid = _insert_lesen_task(conn, sid, task)

                    existing = _task_exists(conn, sid, task["title_de"])
                    # if tid returned was an existing id, it was skipped
                    # We'll count by checking if the id was just inserted
                    inserted += 1

    conn.commit()
    conn.close()
    print(f"✅ exam_seed_v2: done — {inserted} task operations across {len(PROVIDERS)} providers.")


if __name__ == "__main__":
    run()
