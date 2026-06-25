"""
Seed script for exam preparation module.
Run once on the server:  python exam_seed.py

Creates demo content for Goethe A1:
  - Lesen: 3 tasks (richtig/falsch, multiple choice, richtig/falsch)
  - Schreiben: 2 tasks (form fill, free writing)

All content is original and for practice purposes only.
Not official Goethe-Institut examination materials.
"""
import sqlite3
import json
import os
import sys

# Allow running from any directory
sys.path.insert(0, os.path.dirname(__file__))
import exam_db

DB_PATH = os.environ.get("DB_PATH", "alman_bildung.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def run():
    print("Initializing exam DB tables...")
    exam_db.init_exam_db()
    conn = get_conn()

    # ── 1. Providers ──────────────────────────────────────────────────────────
    providers = [
        {
            "name": "goethe",
            "title": "Goethe-Zertifikat",
            "logo_emoji": "🏛️",
            "description_ru": "Официальный экзамен Гёте-Института. Признаётся по всему миру. Требуется для визы на воссоединение семьи.",
            "description_uz": "Goethe-Institut rasmiy imtihoni. Butun dunyoda tan olinadi. Oila birlashuviga viza uchun talab qilinadi.",
            "description_de": "Offizielles Sprachzertifikat des Goethe-Instituts. Weltweit anerkannt.",
        },
        {
            "name": "telc",
            "title": "telc Deutsch",
            "logo_emoji": "📋",
            "description_ru": "Европейский языковой сертификат. Признаётся в системе образования и на рынке труда Германии и Австрии.",
            "description_uz": "Yevropa til sertifikati. Germaniya va Avstriyada ta'lim va ish bozorida tan olinadi.",
            "description_de": "Europäisches Sprachenzertifikat. In Bildung und Beruf in Deutschland und Österreich anerkannt.",
        },
        {
            "name": "osd",
            "title": "ÖSD Zertifikat",
            "logo_emoji": "🇦🇹",
            "description_ru": "Австрийский языковой диплом. Особенно ценится для получения австрийской визы и гражданства.",
            "description_uz": "Avstriya til diplomasi. Avstriya vizasi va fuqaroligi uchun ayniqsa qadrlanadi.",
            "description_de": "Österreichisches Sprachdiplom. Besonders wertvoll für österreichische Visa und Staatsbürgerschaft.",
        },
    ]

    provider_ids = {}
    for p in providers:
        existing = conn.execute("SELECT id FROM exam_providers WHERE name=?", (p["name"],)).fetchone()
        if existing:
            provider_ids[p["name"]] = existing["id"]
            print(f"  Provider '{p['name']}' already exists — skipping")
            continue
        cur = conn.execute("""
            INSERT INTO exam_providers (name, title, logo_emoji, description_ru, description_uz, description_de)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (p["name"], p["title"], p["logo_emoji"], p["description_ru"], p["description_uz"], p["description_de"]))
        conn.commit()
        provider_ids[p["name"]] = cur.lastrowid
        print(f"  Created provider: {p['name']}")

    # ── 2. Levels for all providers ───────────────────────────────────────────
    level_configs = {
        "A1": {
            "title": "A1 — Anfänger",
            "description_ru": "Базовый уровень. Понимание и использование знакомых выражений повседневной жизни.",
            "description_uz": "Boshlang'ich daraja. Kundalik hayotdagi tanish iboralarni tushunish va ishlatish.",
            "target_audience_ru": "Для тех, кто хочет пройти тест для визы воссоединения семьи (А1) или просто начать учить немецкий.",
            "target_audience_uz": "Oila birlashuviga viza (A1) yoki shunchaki nemis tilini o'rganishni boshlamoqchi bo'lganlar uchun.",
            "duration_total": "65 мин",
            "pass_score": 60,
            "exam_parts": [
                {"name": "Lesen", "name_ru": "Чтение", "duration": "20 мин", "points": 25},
                {"name": "Hören", "name_ru": "Аудирование", "duration": "20 мин", "points": 25},
                {"name": "Schreiben", "name_ru": "Письмо", "duration": "10 мин", "points": 25},
                {"name": "Sprechen", "name_ru": "Говорение", "duration": "15 мин", "points": 25},
            ],
            "tips_ru": "На экзамене А1 читайте задание внимательно. Для Lesen: читайте сначала вопросы, потом текст. Для Schreiben: пишите простыми предложениями, избегайте сложных конструкций.",
            "tips_uz": "A1 imtihonida topshiriqni diqqat bilan o'qing. Lesen uchun: avval savollarni, keyin matnni o'qing. Schreiben uchun: oddiy jumlalar yozing.",
        },
        "A2": {
            "title": "A2 — Grundstufe",
            "description_ru": "Уровень выживания. Общение в типичных ситуациях (путешествия, покупки, здоровье).",
            "description_uz": "Omon qolish darajasi. Odatiy vaziyatlarda muloqot (sayohat, xarid, sog'liq).",
            "target_audience_ru": "Для тех, кто хочет сдать экзамен A2 для работы, учёбы или интеграции в Германии.",
            "target_audience_uz": "Germaniyada ishlash, o'qish yoki integratsiya uchun A2 imtihonini topshirmoqchi bo'lganlar uchun.",
            "duration_total": "75 мин",
            "pass_score": 60,
            "exam_parts": [
                {"name": "Lesen", "name_ru": "Чтение", "duration": "25 мин", "points": 25},
                {"name": "Hören", "name_ru": "Аудирование", "duration": "20 мин", "points": 25},
                {"name": "Schreiben", "name_ru": "Письмо", "duration": "15 мин", "points": 25},
                {"name": "Sprechen", "name_ru": "Говорение", "duration": "15 мин", "points": 25},
            ],
            "tips_ru": "Уровень A2: активно пополняйте словарный запас по темам «работа», «здоровье», «путешествия». Тренируйте написание коротких писем.",
            "tips_uz": "A2 darajasi: 'ish', 'sog'liq', 'sayohat' mavzularida so'z boyligini faol to'ldiring. Qisqa xatlar yozishni mashq qiling.",
        },
        "B1": {
            "title": "B1 — Mittelstufe",
            "description_ru": "Порог самостоятельности. Необходим для немецкого гражданства, многих вакансий и Ausbildung.",
            "description_uz": "Mustaqillik bo'sag'asi. Nemis fuqaroligi, ko'p ish o'rinlari va Ausbildung uchun zarur.",
            "target_audience_ru": "Для оформления немецкого гражданства, Ausbildung и работы в Германии. Международно признанный уровень.",
            "target_audience_uz": "Nemis fuqaroligi, Ausbildung va Germaniyada ishlash uchun. Xalqaro tan olingan daraja.",
            "duration_total": "160 мин",
            "pass_score": 60,
            "exam_parts": [
                {"name": "Lesen", "name_ru": "Чтение", "duration": "45 мин", "points": 25},
                {"name": "Hören", "name_ru": "Аудирование", "duration": "40 мин", "points": 25},
                {"name": "Schreiben", "name_ru": "Письмо", "duration": "30 мин", "points": 25},
                {"name": "Sprechen", "name_ru": "Говорение", "duration": "15 мин", "points": 25},
            ],
            "tips_ru": "B1 — сложный экзамен. Уделите особое внимание Schreiben: нужно написать письмо 100–150 слов. Тренируйте Relativsätze и Konjunktiv II.",
            "tips_uz": "B1 — murakkab imtihon. Schreibenga alohida e'tibor bering: 100-150 so'zlik xat yozish kerak. Relativsätze va Konjunktiv II ni mashq qiling.",
        },
        "B2": {
            "title": "B2 — Obere Mittelstufe",
            "description_ru": "Уровень для академических и профессиональных целей. Требуется для поступления в немецкий университет.",
            "description_uz": "Akademik va kasbiy maqsadlar uchun daraja. Nemis universitetiga kirish uchun talab qilinadi.",
            "target_audience_ru": "Для поступления в университет, высококвалифицированной работы или академической деятельности в Германии.",
            "target_audience_uz": "Universitega kirish, yuqori malakali ish yoki Germaniyada akademik faoliyat uchun.",
            "duration_total": "190 мин",
            "pass_score": 60,
            "exam_parts": [
                {"name": "Lesen", "name_ru": "Чтение", "duration": "65 мин", "points": 25},
                {"name": "Hören", "name_ru": "Аудирование", "duration": "40 мин", "points": 25},
                {"name": "Schreiben", "name_ru": "Письмо", "duration": "60 мин", "points": 25},
                {"name": "Sprechen", "name_ru": "Говорение", "duration": "25 мин", "points": 25},
            ],
            "tips_ru": "B2: особое внимание сложным грамматическим конструкциям (Partizipialkonstruktionen, Nominalisierungen). Читайте немецкие газеты (Der Spiegel, Zeit).",
            "tips_uz": "B2: murakkab grammatik konstruktsiyalarga alohida e'tibor bering. Nemis gazetalarini o'qing (Der Spiegel, Zeit).",
        },
    }

    level_ids = {}   # (provider_name, level) -> level_id
    for pname, pid in provider_ids.items():
        for lname, lcfg in level_configs.items():
            existing = conn.execute("""
                SELECT id FROM exam_levels WHERE provider_id=? AND level=?
            """, (pid, lname)).fetchone()
            if existing:
                level_ids[(pname, lname)] = existing["id"]
                continue
            cur = conn.execute("""
                INSERT INTO exam_levels
                  (provider_id, level, title, description_ru, description_uz,
                   target_audience_ru, target_audience_uz,
                   duration_total, pass_score, exam_parts_json, tips_ru, tips_uz)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                pid, lname, lcfg["title"],
                lcfg["description_ru"], lcfg["description_uz"],
                lcfg["target_audience_ru"], lcfg["target_audience_uz"],
                lcfg["duration_total"], lcfg["pass_score"],
                json.dumps(lcfg["exam_parts"], ensure_ascii=False),
                lcfg["tips_ru"], lcfg["tips_uz"],
            ))
            conn.commit()
            level_ids[(pname, lname)] = cur.lastrowid
            print(f"  Created level: {pname} {lname}")

    # ── 3. Sections for all providers × levels ─────────────────────────────────
    section_configs = [
        {"type": "lesen", "title_de": "Lesen", "title_ru": "Чтение", "title_uz": "O'qish",
         "description_ru": "Понимание письменных текстов: объявления, письма, статьи.",
         "description_uz": "Yozma matnlarni tushunish: e'lonlar, xatlar, maqolalar.",
         "sort_order": 1},
        {"type": "hoeren", "title_de": "Hören", "title_ru": "Аудирование", "title_uz": "Tinglash",
         "description_ru": "Понимание устной речи: диалоги, объявления, интервью.",
         "description_uz": "Og'zaki nutqni tushunish: dialoglar, e'lonlar, intervyular.",
         "sort_order": 2},
        {"type": "schreiben", "title_de": "Schreiben", "title_ru": "Письмо", "title_uz": "Yozish",
         "description_ru": "Написание текстов: заполнение форм, короткие сообщения, письма.",
         "description_uz": "Matn yozish: anketalarni to'ldirish, qisqa xabarlar, xatlar.",
         "sort_order": 3},
        {"type": "sprechen", "title_de": "Sprechen", "title_ru": "Говорение", "title_uz": "Gapirish",
         "description_ru": "Устная речь: представление себя, диалог, монолог.",
         "description_uz": "Og'zaki nutq: o'zini tanishtirish, dialog, monolog.",
         "sort_order": 4},
        {"type": "grammatik", "title_de": "Grammatik & Wortschatz", "title_ru": "Грамматика", "title_uz": "Grammatika",
         "description_ru": "Грамматические упражнения и словарный запас.",
         "description_uz": "Grammatik mashqlar va so'z boyligi.",
         "sort_order": 5},
    ]

    durations = {"A1": {"lesen": 20, "hoeren": 20, "schreiben": 10, "sprechen": 15, "grammatik": 20},
                 "A2": {"lesen": 25, "hoeren": 20, "schreiben": 15, "sprechen": 15, "grammatik": 25},
                 "B1": {"lesen": 45, "hoeren": 40, "schreiben": 30, "sprechen": 15, "grammatik": 30},
                 "B2": {"lesen": 65, "hoeren": 40, "schreiben": 60, "sprechen": 25, "grammatik": 40}}

    section_ids = {}   # (provider_name, level, type) -> section_id
    for (pname, lname), lid in level_ids.items():
        for scfg in section_configs:
            existing = conn.execute(
                "SELECT id FROM exam_sections WHERE level_id=? AND type=?",
                (lid, scfg["type"])
            ).fetchone()
            if existing:
                section_ids[(pname, lname, scfg["type"])] = existing["id"]
                continue
            dur = durations.get(lname, {}).get(scfg["type"], 20)
            cur = conn.execute("""
                INSERT INTO exam_sections
                  (level_id, type, title_de, title_ru, title_uz,
                   description_ru, description_uz, duration_minutes, sort_order)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (lid, scfg["type"], scfg["title_de"], scfg["title_ru"], scfg["title_uz"],
                  scfg["description_ru"], scfg["description_uz"], dur, scfg["sort_order"]))
            conn.commit()
            section_ids[(pname, lname, scfg["type"])] = cur.lastrowid

    print("  All sections created.")

    # ── 4. Demo content: Goethe A1 Lesen ─────────────────────────────────────
    lesen_sid = section_ids.get(("goethe", "A1", "lesen"))
    if not lesen_sid:
        print("ERROR: Goethe A1 Lesen section not found")
        return

    existing_tasks = conn.execute(
        "SELECT COUNT(*) as cnt FROM exam_tasks WHERE section_id=?", (lesen_sid,)
    ).fetchone()["cnt"]

    if existing_tasks > 0:
        print(f"  Goethe A1 Lesen already has {existing_tasks} tasks — skipping.")
    else:
        # ── Task 1: Anzeigen lesen (richtig/falsch) ───────────────────────────
        t1 = conn.execute("""
            INSERT INTO exam_tasks
              (section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz,
               text_content, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            lesen_sid,
            "Teil 1 — Anzeigen lesen",
            "Часть 1 — Читаем объявления",
            "truefalse",
            "Lesen Sie die Anzeigen. Sind die Aussagen richtig oder falsch?",
            "Прочитайте объявления. Утверждения верны или нет?",
            "E'lonlarni o'qing. Quyidagi gaplar to'g'rimi yoki noto'g'rimi?",
            """A
Supermarkt Frisch & Gut
Montag–Freitag: 08:00–20:00 Uhr
Samstag: 08:00–18:00 Uhr
Sonntags geschlossen.

B
Deutschkurs für Anfänger
Jeden Montag, 18:00–20:00 Uhr
Anmeldung: info@sprachschule-berlin.de
Tel.: 030-2345678

C
Fahrrad zu verkaufen
Zustand: sehr gut | Preis: 75 Euro
Kontakt: fahrrad@mail.de

D
Stadtbibliothek Mitte
Wegen Renovierungsarbeiten
vom 10. bis 28. Februar geschlossen.
Wir bitten um Entschuldigung!""",
            1
        )).lastrowid
        conn.commit()

        t1_questions = [
            ("Der Supermarkt ist sonntags geöffnet.", "Falsch",
             "В объявлении написано: «Sonntags geschlossen» — по воскресеньям закрыто.",
             "E'londa yozilgan: «Sonntags geschlossen» — yakshanba kuni yopiq."),
            ("Der Deutschkurs findet montags statt.", "Richtig",
             "В объявлении: «Jeden Montag» — каждый понедельник.",
             "E'londa: «Jeden Montag» — har dushanba."),
            ("Das Fahrrad kostet 75 Euro.", "Richtig",
             "В объявлении о велосипеде написано: «Preis: 75 Euro».",
             "Velosiped e'lonida: «Preis: 75 Euro» yozilgan."),
            ("Die Bibliothek ist jetzt geöffnet.", "Falsch",
             "Библиотека закрыта на ремонт с 10 по 28 февраля.",
             "Kutubxona ta'mirlash uchun 10 fevraldan 28 fevralga qadar yopiq."),
            ("Der Deutschkurs beginnt um 18 Uhr.", "Richtig",
             "В объявлении: «18:00–20:00 Uhr» — начало в 18:00.",
             "E'londa: «18:00–20:00 Uhr» — boshlanish 18:00 da."),
        ]

        for i, (qtxt, correct, exp_ru, exp_uz) in enumerate(t1_questions):
            qid = conn.execute("""
                INSERT INTO exam_questions
                  (task_id, question_text, question_type, correct_answer,
                   explanation_ru, explanation_uz, points, sort_order)
                VALUES (?, ?, 'truefalse', ?, ?, ?, 1, ?)
            """, (t1, qtxt, correct, exp_ru, exp_uz, i)).lastrowid
            conn.commit()
            for opt_text in ["Richtig", "Falsch"]:
                conn.execute("""
                    INSERT INTO exam_answer_options (question_id, option_text, is_correct)
                    VALUES (?, ?, ?)
                """, (qid, opt_text, 1 if opt_text == correct else 0))
            conn.commit()

        # ── Task 2: E-Mail lesen (multiple choice) ────────────────────────────
        t2 = conn.execute("""
            INSERT INTO exam_tasks
              (section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz,
               text_content, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            lesen_sid,
            "Teil 2 — Eine E-Mail lesen",
            "Часть 2 — Читаем электронное письмо",
            "choice",
            "Lesen Sie die E-Mail und beantworten Sie die Fragen.",
            "Прочитайте электронное письмо и ответьте на вопросы.",
            "Elektron xatni o'qing va savollarga javob bering.",
            """Von: anna.mueller@privat.de
An: petra.fischer@privat.de
Betreff: Meine neue Wohnung!

Hallo Petra!

Ich habe jetzt eine neue Wohnung in Hamburg. Sie ist im dritten Stock und hat drei Zimmer: ein Wohnzimmer, ein Schlafzimmer und ein Arbeitszimmer. Die Küche ist groß und modern. Ich habe auch einen kleinen Balkon — super für den Sommer!

Die Wohnung kostet 950 Euro im Monat. Das ist nicht billig, aber Hamburg ist teuer. Mein Büro ist nur 15 Minuten mit der U-Bahn entfernt. Das ist praktisch!

Am nächsten Samstag mache ich eine kleine Einzugsparty. Kannst du kommen?

Liebe Grüße,
Anna""",
            2
        )).lastrowid
        conn.commit()

        t2_questions = [
            ("Wo wohnt Anna jetzt?",
             [("In Berlin", False), ("In Hamburg", True), ("In München", False), ("In Frankfurt", False)],
             "В письме написано: «eine neue Wohnung in Hamburg».",
             "Xatda yozilgan: «eine neue Wohnung in Hamburg»."),
            ("Im wievielten Stock wohnt Anna?",
             [("Im ersten Stock", False), ("Im zweiten Stock", False), ("Im dritten Stock", True), ("Im vierten Stock", False)],
             "«Sie ist im dritten Stock» — на третьем этаже.",
             "«Sie ist im dritten Stock» — uchinchi qavatda."),
            ("Wie viele Zimmer hat Annas Wohnung?",
             [("Zwei", False), ("Drei", True), ("Vier", False), ("Fünf", False)],
             "«hat drei Zimmer: ein Wohnzimmer, ein Schlafzimmer und ein Arbeitszimmer» — три комнаты.",
             "«hat drei Zimmer» — uchta xona."),
            ("Was hat Anna auch in der Wohnung?",
             [("Einen Garten", False), ("Eine Terrasse", False), ("Einen Keller", False), ("Einen Balkon", True)],
             "«Ich habe auch einen kleinen Balkon».",
             "«Ich habe auch einen kleinen Balkon»."),
            ("Wie kommt Anna zur Arbeit?",
             [("Mit dem Bus", False), ("Mit der U-Bahn", True), ("Mit dem Auto", False), ("Zu Fuß", False)],
             "«15 Minuten mit der U-Bahn entfernt» — 15 минут на метро.",
             "«15 Minuten mit der U-Bahn entfernt» — metro bilan 15 daqiqa."),
        ]

        for i, (qtxt, opts, exp_ru, exp_uz) in enumerate(t2_questions):
            correct_text = next(o[0] for o in opts if o[1])
            qid = conn.execute("""
                INSERT INTO exam_questions
                  (task_id, question_text, question_type, correct_answer,
                   explanation_ru, explanation_uz, points, sort_order)
                VALUES (?, ?, 'choice', ?, ?, ?, 1, ?)
            """, (t2, qtxt, correct_text, exp_ru, exp_uz, i)).lastrowid
            conn.commit()
            for j, (opt_text, is_corr) in enumerate(opts):
                conn.execute("""
                    INSERT INTO exam_answer_options (question_id, option_text, is_correct, sort_order)
                    VALUES (?, ?, ?, ?)
                """, (qid, opt_text, 1 if is_corr else 0, j))
            conn.commit()

        # ── Task 3: Gästehaus-Information (richtig/falsch) ───────────────────
        t3 = conn.execute("""
            INSERT INTO exam_tasks
              (section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz,
               text_content, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            lesen_sid,
            "Teil 3 — Informationen verstehen",
            "Часть 3 — Понимаем информацию",
            "truefalse",
            "Lesen Sie den Text. Sind die Sätze richtig oder falsch?",
            "Прочитайте текст. Предложения верны или нет?",
            "Matnni o'qing. Gaplar to'g'rimi yoki noto'g'rimi?",
            """Willkommen im Gästehaus Sonnenschein!

Check-in: ab 15:00 Uhr
Check-out: bis 11:00 Uhr

Frühstück: täglich von 7:00 bis 10:00 Uhr (Erdgeschoss, Raum 1)
WLAN: kostenlos im ganzen Haus | Passwort: Gast2024
Parkplätze: hinter dem Haus, für unsere Gäste kostenlos
Rezeption: 24 Stunden geöffnet
Rauchen: nur im Außenbereich erlaubt — bitte nicht im Zimmer!

Bei Fragen wenden Sie sich bitte an die Rezeption.""",
            3
        )).lastrowid
        conn.commit()

        t3_questions = [
            ("Das Frühstück beginnt um 7 Uhr morgens.", "Richtig",
             "«Frühstück: täglich von 7:00 bis 10:00 Uhr» — с 7 утра.",
             "«Frühstück: täglich von 7:00 bis 10:00 Uhr» — ertalab 7 dan."),
            ("Das WLAN im Gästehaus ist kostenpflichtig.", "Falsch",
             "«WLAN: kostenlos im ganzen Haus» — бесплатный Wi-Fi.",
             "«WLAN: kostenlos im ganzen Haus» — bepul Wi-Fi."),
            ("Der Check-in ist ab 15 Uhr möglich.", "Richtig",
             "«Check-in: ab 15:00 Uhr» — заезд с 15:00.",
             "«Check-in: ab 15:00 Uhr» — kirish 15:00 dan."),
            ("Die Rezeption ist nachts geschlossen.", "Falsch",
             "«Rezeption: 24 Stunden geöffnet» — ресепшн открыт круглосуточно.",
             "«Rezeption: 24 Stunden geöffnet» — qabul 24 soat ochiq."),
            ("Man darf im Zimmer rauchen.", "Falsch",
             "«Rauchen: nur im Außenbereich erlaubt» — курить разрешено только на улице.",
             "«Rauchen: nur im Außenbereich erlaubt» — chekish faqat tashqarida ruxsat etiladi."),
        ]

        for i, (qtxt, correct, exp_ru, exp_uz) in enumerate(t3_questions):
            qid = conn.execute("""
                INSERT INTO exam_questions
                  (task_id, question_text, question_type, correct_answer,
                   explanation_ru, explanation_uz, points, sort_order)
                VALUES (?, ?, 'truefalse', ?, ?, ?, 1, ?)
            """, (t3, qtxt, correct, exp_ru, exp_uz, i)).lastrowid
            conn.commit()
            for opt_text in ["Richtig", "Falsch"]:
                conn.execute("""
                    INSERT INTO exam_answer_options (question_id, option_text, is_correct)
                    VALUES (?, ?, ?)
                """, (qid, opt_text, 1 if opt_text == correct else 0))
            conn.commit()

        print("  Goethe A1 Lesen: 3 tasks created.")

    # ── 5. Demo content: Goethe A1 Schreiben ─────────────────────────────────
    schreiben_sid = section_ids.get(("goethe", "A1", "schreiben"))
    if not schreiben_sid:
        print("ERROR: Goethe A1 Schreiben section not found")
        return

    existing_sw = conn.execute(
        "SELECT COUNT(*) as cnt FROM exam_tasks WHERE section_id=?", (schreiben_sid,)
    ).fetchone()["cnt"]

    if existing_sw > 0:
        print(f"  Goethe A1 Schreiben already has {existing_sw} tasks — skipping.")
    else:
        # ── Schreiben Task 1: Formular ausfüllen ──────────────────────────────
        extra1 = {
            "model_answer": "Vorname: Lena\nFamilienname: Braun\nGeburtsdatum: 05.07.1995\nNationalität: Deutsch\nE-Mail: lena.braun@mail.de\nTelefon: 0162-7654321",
            "checklist": [
                "Alle Felder ausgefüllt?",
                "Geburtsdatum im Format TT.MM.JJJJ?",
                "E-Mail korrekt geschrieben?",
                "Keine Abkürzungen verwendet?",
            ],
            "redemittel": [],
            "form_fields": ["Vorname", "Familienname", "Geburtsdatum", "Nationalität", "E-Mail", "Telefon"],
        }

        conn.execute("""
            INSERT INTO exam_tasks
              (section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz,
               text_content, extra_data, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            schreiben_sid,
            "Teil 1 — Formular ausfüllen",
            "Часть 1 — Заполнение формуляра",
            "writing_form",
            "Lesen Sie die Informationen und füllen Sie das Anmeldeformular aus.",
            "Прочитайте информацию и заполните регистрационную форму.",
            "Ma'lumotlarni o'qing va ro'yxatdan o'tish shaklini to'ldiring.",
            "Lena Braun möchte sich für einen Deutschkurs anmelden.\nSie ist am 5. Juli 1995 in Deutschland geboren.\nSie wohnt in Berlin und ist Deutsche.\nIhre E-Mail-Adresse ist: lena.braun@mail.de\nIhre Handynummer ist: 0162-7654321",
            json.dumps(extra1, ensure_ascii=False),
            1
        ))
        conn.commit()

        # ── Schreiben Task 2: Kurzmitteilung schreiben ────────────────────────
        extra2 = {
            "model_answer": "Hallo Lisa!\n\nDanke für deine Einladung! Ich komme gerne.\nIch bringe Salat mit. Wann beginnt die Party?\n\nBis Samstag!\nThomas",
            "checklist": [
                "Hast du Lisa angesprochen (z.B. 'Hallo Lisa!')?",
                "Hast du geschrieben, dass du kommst?",
                "Hast du etwas mitbringen wollen erwähnt?",
                "Hast du dich verabschiedet?",
                "Sind die Sätze verständlich?",
            ],
            "redemittel": [
                "Hallo [Name]! / Liebe/r [Name]!",
                "Vielen Dank für ... / Danke für ...",
                "Ich komme gerne. / Ich kann leider nicht kommen.",
                "Ich bringe ... mit.",
                "Wann beginnt ...? / Um wie viel Uhr ...?",
                "Bis [Tag]! / Liebe Grüße, [Name]",
            ],
            "word_count_min": 20,
            "word_count_max": 40,
        }

        conn.execute("""
            INSERT INTO exam_tasks
              (section_id, title_de, title_ru, task_type, instruction_de, instruction_ru, instruction_uz,
               text_content, extra_data, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            schreiben_sid,
            "Teil 2 — Eine Kurzmitteilung schreiben",
            "Часть 2 — Пишем короткое сообщение",
            "writing_free",
            "Schreiben Sie eine kurze Nachricht (20–40 Wörter) an Ihre Freundin/Ihren Freund.",
            "Напишите короткое сообщение (20–40 слов) другу или подруге.",
            "Do'stingizga qisqa xabar yozing (20–40 so'z).",
            "Ihre Freundin Lisa lädt Sie zu einer Party am Samstag ein.\nSie wollen:\n• zusagen (ja sagen)\n• etwas mitbringen\n• fragen, wann die Party beginnt",
            json.dumps(extra2, ensure_ascii=False),
            2
        ))
        conn.commit()
        print("  Goethe A1 Schreiben: 2 tasks created.")

    conn.close()
    print("\n✅ Seed complete! Run the app and navigate to /exam to test.")


if __name__ == "__main__":
    run()
