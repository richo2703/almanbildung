"""B1.1 + B1.2 content"""

B1_1 = {
  "title_ru": "Пороговый — часть 1", "title_uz": "O'rta daraja — 1-qism",
  "lessons": [
    { "id":1, "title_de":"Persönlichkeit und Charakter", "title_ru":"Личность и характер", "title_uz":"Shaxsiyat va xarakter",
      "grammar_topic":"Nomen-Verb-Verbindungen | Устойчивые глагольно-именные сочетания",
      "grammar_ru":
        "🔷 Устойчивые сочетания (Funktionsverbgefüge):\n"
        "• eine Entscheidung *treffen* — принимать решение\n"
        "• einen Fehler *machen* — делать ошибку\n"
        "• Kritik *üben* — критиковать\n"
        "• in Frage *stellen* — ставить под сомнение\n"
        "• zur Verfügung *stehen* — быть в распоряжении\n\n"
        "Эти сочетания нельзя переводить дословно!",
      "grammar_uz":
        "🔷 Barqaror birikmaları:\n"
        "• eine Entscheidung *treffen* — qaror qabul qilmoq\n"
        "• einen Fehler *machen* — xato qilmoq\n"
        "• Kritik *üben* — tanqid qilmoq\n"
        "• in Frage *stellen* — shubha ostiga qo'ymoq\n"
        "• zur Verfügung *stehen* — ixtiyorida bo'lmoq\n\n"
        "Bu birikmalarni so'zma-so'z tarjima qilish mumkin emas!",
      "vocab":[
        {"de":"die Persönlichkeit","ru":"личность","uz":"shaxsiyat"},
        {"de":"der Charakter","ru":"характер","uz":"xarakter"},
        {"de":"zuverlässig","ru":"надёжный","uz":"ishonchli"},
        {"de":"ehrgeizig","ru":"амбициозный","uz":"ambitsiyali"},
        {"de":"einfühlsam","ru":"чуткий / эмпатичный","uz":"sezgir"},
        {"de":"kreativ","ru":"креативный","uz":"ijodiy"},
        {"de":"geduldig","ru":"терпеливый","uz":"sabr-toqatli"},
        {"de":"optimistisch","ru":"оптимистичный","uz":"optimist"},
        {"de":"pessimistisch","ru":"пессимистичный","uz":"pessimist"},
        {"de":"selbstbewusst","ru":"уверенный в себе","uz":"o'ziga ishongan"},
        {"de":"die Entscheidung","ru":"решение","uz":"qaror"},
        {"de":"der Fehler","ru":"ошибка","uz":"xato"},
      ],
      "dialogue":[
        ("A","Was sind deine stärksten Charaktereigenschaften?"),
        ("B","Ich bin zuverlässig und einfühlsam. Ich stehe meinen Kollegen zur Verfügung."),
        ("A","Machst du manchmal Fehler?"),
        ("B","Ja, aber ich treffe dann schnell eine Entscheidung, wie ich sie korrigiere."),
        ("A","Bist du eher Optimist oder Pessimist?"),
        ("B","Definitiv Optimist — ich stelle selten etwas in Frage, ohne Lösungen zu suchen."),
      ],
      "exercises":[
        {"type":"choice","q":"Er trifft immer gute ___. (решения)",
         "opts":["Fehler","Entscheidungen","Kritik","Fragen"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'zuverlässig'?",
         "opts":["амбициозный","творческий","надёжный","терпеливый"],"ans":2},
        {"type":"fill","q":"Sie ___ Kritik an der Situation. (критикует — üben)",
         "opts":["macht","trifft","übt","stellt"],"ans":2},
      ]
    },
    { "id":2, "title_de":"Globalisierung und Wirtschaft", "title_ru":"Глобализация и экономика", "title_uz":"Globallashuv va iqtisodiyot",
      "grammar_topic":"Konzessivsätze: obwohl, obgleich, trotzdem | Уступительные придаточные",
      "grammar_ru":
        "🔷 Уступка:\n"
        "• *obwohl* + Nebensatz (глагол в конец):\n"
        "  Obwohl es teuer ist, kaufe ich es.\n"
        "• *trotzdem* + Hauptsatz (инвертированный порядок):\n"
        "  Es ist teuer. *Trotzdem* kaufe ich es.\n"
        "• *obgleich* = obwohl (более формальное)\n\n"
        "Разница: obwohl — союз, trotzdem — наречие",
      "grammar_uz":
        "🔷 Yon gaplar:\n"
        "• *obwohl* + Nebensatz (fe'l oxirga):\n"
        "  Obwohl es teuer ist, kaufe ich es.\n"
        "• *trotzdem* + Hauptsatz (teskari tartib):\n"
        "  Es ist teuer. *Trotzdem* kaufe ich es.\n"
        "• *obgleich* = obwohl (rasmiyroq)",
      "vocab":[
        {"de":"die Globalisierung","ru":"глобализация","uz":"globallashuv"},
        {"de":"die Wirtschaft","ru":"экономика","uz":"iqtisodiyot"},
        {"de":"der Handel","ru":"торговля","uz":"savdo"},
        {"de":"importieren","ru":"импортировать","uz":"import qilmoq"},
        {"de":"exportieren","ru":"экспортировать","uz":"eksport qilmoq"},
        {"de":"der Markt","ru":"рынок","uz":"bozor"},
        {"de":"die Inflation","ru":"инфляция","uz":"inflyatsiya"},
        {"de":"die Währung","ru":"валюта","uz":"valyuta"},
        {"de":"der Konzern","ru":"концерн / корпорация","uz":"korporatsiya"},
        {"de":"multinationale Unternehmen","ru":"транснациональные компании","uz":"transmilliy kompaniyalar"},
        {"de":"die Arbeitslosigkeit","ru":"безработица","uz":"ishsizlik"},
        {"de":"das Wirtschaftswachstum","ru":"экономический рост","uz":"iqtisodiy o'sish"},
      ],
      "dialogue":[
        ("A","Wie beeinflusst die Globalisierung uns?"),
        ("B","Obwohl sie Chancen schafft, gibt es auch Probleme."),
        ("A","Zum Beispiel?"),
        ("B","Die Arbeitslosigkeit steigt in manchen Ländern, trotzdem wächst die Gesamtwirtschaft."),
        ("A","Hilft der internationale Handel wirklich?"),
        ("B","Ja, obgleich nicht alle Länder gleich davon profitieren."),
      ],
      "exercises":[
        {"type":"choice","q":"___ es teuer ist, kaufe ich es. (хотя — союз)",
         "opts":["Trotzdem","Obwohl","Aber","Jedoch"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'die Arbeitslosigkeit'?",
         "opts":["экономический рост","инфляция","безработица","торговля"],"ans":2},
        {"type":"fill","q":"Es ist schwer. ___ versuchen wir es. (тем не менее — наречие)",
         "opts":["Obwohl","Obgleich","Trotzdem","Weil"],"ans":2},
      ]
    },
    { "id":3, "title_de":"Sprache und Literatur", "title_ru":"Язык и литература", "title_uz":"Til va adabiyot",
      "grammar_topic":"Konjunktiv I (indirekte Rede) | Косвенная речь",
      "grammar_ru":
        "🔷 Konjunktiv I — косвенная речь (журналистика, репортажи)\n"
        "sein: er sei, wir seien\n"
        "haben: er habe\n"
        "Обычные глаголы: er komm*e*, er fahr*e*, er sag*e*\n\n"
        "• Er sagt, er *sei* krank. — Он говорит, что болен.\n"
        "• Sie erklärt, sie *habe* das gelesen.\n"
        "• Die Zeitung schreibt, das Buch *erscheine* bald.",
      "grammar_uz":
        "🔷 Konjunktiv I — bilvosita nutq (jurnalistika)\n"
        "sein: er sei, wir seien\n"
        "haben: er habe\n"
        "Oddiy fe'llar: er komm*e*, er fahr*e*, er sag*e*\n\n"
        "• Er sagt, er *sei* krank. — U kasal deydi.\n"
        "• Sie erklärt, sie *habe* das gelesen.\n"
        "• Die Zeitung schreibt, das Buch *erscheine* bald.",
      "vocab":[
        {"de":"die Literatur","ru":"литература","uz":"adabiyot"},
        {"de":"der Roman","ru":"роман","uz":"roman"},
        {"de":"die Kurzgeschichte","ru":"рассказ","uz":"qissa"},
        {"de":"der Autor","ru":"автор","uz":"muallif"},
        {"de":"erscheinen","ru":"выходить (о книге)","uz":"chiqmoq (kitob haqida)"},
        {"de":"interpretieren","ru":"интерпретировать","uz":"talqin qilmoq"},
        {"de":"die Metapher","ru":"метафора","uz":"metafora"},
        {"de":"die Handlung","ru":"сюжет / действие","uz":"syujet"},
        {"de":"der Protagonist","ru":"главный герой","uz":"bosh qahramon"},
        {"de":"beschreiben","ru":"описывать","uz":"tasvirlamoq"},
        {"de":"analysieren","ru":"анализировать","uz":"tahlil qilmoq"},
        {"de":"das Werk","ru":"произведение","uz":"asar"},
      ],
      "dialogue":[
        ("A","Hast du das neue Buch gelesen?"),
        ("B","Ja! Die Zeitung schreibt, das Werk sei ein Meisterwerk."),
        ("A","Was sagt der Autor dazu?"),
        ("B","Er erklärt, er habe zwei Jahre daran gearbeitet."),
        ("A","Wie ist die Handlung?"),
        ("B","Der Kritiker schreibt, der Protagonist durchlebe eine komplexe Reise — voller Metaphern."),
      ],
      "exercises":[
        {"type":"choice","q":"Er sagt, er ___ krank. (Konjunktiv I von 'sein')",
         "opts":["ist","war","sei","wäre"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'die Handlung'?",
         "opts":["метафора","автор","сюжет","произведение"],"ans":2},
        {"type":"fill","q":"Die Zeitung schreibt, das Buch ___ bald. (выходит, Konj. I von erscheinen)",
         "opts":["erscheint","erscheine","erschienen","erschien"],"ans":1},
      ]
    },
    { "id":4, "title_de":"Wissenschaft und Forschung", "title_ru":"Наука и исследования", "title_uz":"Fan va tadqiqotlar",
      "grammar_topic":"Passiv mit Modalverben | Пассив с модальными глаголами",
      "grammar_ru":
        "🔷 Пассив + модальный глагол:\n"
        "Modalverb + Partizip II + werden (Infinitiv)\n\n"
        "• Das *muss* erforscht *werden*. — Это должно быть исследовано.\n"
        "• Das Experiment *kann* wiederholt *werden*. — Эксперимент может быть повторён.\n"
        "• Die Daten *sollen* analysiert *werden*. — Данные должны быть проанализированы.",
      "grammar_uz":
        "🔷 Modal fe'l bilan passiv:\n"
        "Modal fe'l + Partizip II + werden (Infinitiv)\n\n"
        "• Das *muss* erforscht *werden*. — Bu tadqiq qilinishi kerak.\n"
        "• Das Experiment *kann* wiederholt *werden*. — Tajriba takrorlanishi mumkin.\n"
        "• Die Daten *sollen* analysiert *werden*. — Ma'lumotlar tahlil qilinishi kerak.",
      "vocab":[
        {"de":"die Wissenschaft","ru":"наука","uz":"fan"},
        {"de":"die Forschung","ru":"исследование","uz":"tadqiqot"},
        {"de":"das Experiment","ru":"эксперимент","uz":"tajriba"},
        {"de":"die Hypothese","ru":"гипотеза","uz":"faraz"},
        {"de":"beweisen","ru":"доказывать","uz":"isbotlamoq"},
        {"de":"die Entdeckung","ru":"открытие","uz":"kashfiyot"},
        {"de":"erforschen","ru":"исследовать","uz":"o'rganmoq"},
        {"de":"das Labor","ru":"лаборатория","uz":"laboratoriya"},
        {"de":"die Studie","ru":"исследование / работа","uz":"tadqiqot"},
        {"de":"veröffentlichen","ru":"публиковать","uz":"nashr qilmoq"},
        {"de":"die Erkenntnis","ru":"знание / открытие","uz":"bilim / kashfiyot"},
        {"de":"technologisch","ru":"технологический","uz":"texnologik"},
      ],
      "dialogue":[
        ("A","Woran forschen Sie gerade?"),
        ("B","Wir untersuchen, wie Energie effizienter genutzt werden kann."),
        ("A","Muss das alles im Labor gemacht werden?"),
        ("B","Nicht alles. Einige Daten können auch digital analysiert werden."),
        ("A","Wann sollen die Ergebnisse veröffentlicht werden?"),
        ("B","Die Studie soll bis Ende des Jahres fertiggestellt werden."),
      ],
      "exercises":[
        {"type":"choice","q":"Die Daten ___ analysiert werden. (должны, Modal+Passiv)",
         "opts":["können","sollen","werden","müssten"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'die Entdeckung'?",
         "opts":["гипотеза","открытие","лаборатория","исследование"],"ans":1},
        {"type":"fill","q":"Das Experiment ___ wiederholt werden. (может быть)",
         "opts":["muss","soll","kann","darf"],"ans":2},
      ]
    },
    { "id":5, "title_de":"Medien und Journalismus", "title_ru":"Медиа и журналистика", "title_uz":"Media va jurnalistika",
      "grammar_topic":"Gerundiv (zu + Partizip I als Adjektiv) | Герундив",
      "grammar_ru":
        "🔷 Герундив = zu + Partizip I в функции прилагательного\n"
        "Означает: что нужно/должно быть сделано\n\n"
        "• das *zu lösende* Problem — проблема, которую нужно решить\n"
        "• die *zu prüfenden* Daten — данные, которые нужно проверить\n"
        "• ein *nicht zu unterschätzendes* Risiko\n"
        "  — риск, который нельзя недооценивать\n\n"
        "💡 Часто заменяется пассивом с müssen/sollen",
      "grammar_uz":
        "🔷 Gerundiv = zu + Partizip I sifat sifatida\n"
        "Mazmun: qilinishi kerak bo'lgan narsa\n\n"
        "• das *zu lösende* Problem — hal qilinishi kerak bo'lgan muammo\n"
        "• die *zu prüfenden* Daten — tekshirilishi kerak bo'lgan ma'lumotlar\n"
        "• ein *nicht zu unterschätzendes* Risiko — kamaytirib bo'lmaydigan xavf",
      "vocab":[
        {"de":"der Journalismus","ru":"журналистика","uz":"jurnalistika"},
        {"de":"der Journalist","ru":"журналист","uz":"jurnalist"},
        {"de":"berichten","ru":"сообщать / репортировать","uz":"xabar bermoq"},
        {"de":"die Quelle","ru":"источник","uz":"manba"},
        {"de":"recherchieren","ru":"исследовать / изучать","uz":"tadqiqot o'tkazmoq"},
        {"de":"objektiv","ru":"объективный","uz":"ob'ektiv"},
        {"de":"subjektiv","ru":"субъективный","uz":"sub'ektiv"},
        {"de":"die Zensur","ru":"цензура","uz":"tsenzura"},
        {"de":"die Pressefreiheit","ru":"свобода прессы","uz":"matbuot erkinligi"},
        {"de":"das Interview","ru":"интервью","uz":"intervyu"},
        {"de":"die Schlagzeile","ru":"заголовок","uz":"sarlavha"},
        {"de":"glaubwürdig","ru":"заслуживающий доверия","uz":"ishonchli"},
      ],
      "dialogue":[
        ("A","Wie recherchierst du für deine Artikel?"),
        ("B","Ich nutze glaubwürdige Quellen. Die zu prüfenden Fakten werden immer verifiziert."),
        ("A","Ist Pressefreiheit wichtig?"),
        ("B","Absolut! Ein nicht zu unterschätzendes Problem ist Zensur."),
        ("A","Wie bleibst du objektiv?"),
        ("B","Ich berichte über die zu lösenden Fragen ohne persönliche Meinung."),
      ],
      "exercises":[
        {"type":"choice","q":"Das ___ Problem muss gelöst werden. (которое нужно решить — Gerundiv)",
         "opts":["gelöste","lösende","zu lösende","löslich"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'glaubwürdig'?",
         "opts":["субъективный","заслуживающий доверия","объективный","свободный"],"ans":1},
        {"type":"fill","q":"Die ___ Daten werden geprüft. (которые нужно проверить)",
         "opts":["geprüften","zu prüfenden","prüfenden","prüfbar"],"ans":1},
      ]
    },
    { "id":6, "title_de":"Interkulturelles und Reisen", "title_ru":"Межкультурное общение", "title_uz":"Madaniyatlararo muloqot",
      "grammar_topic":"Modalpartikeln in Wunsch/Ratschlag | Частицы в пожеланиях",
      "grammar_ru":
        "🔷 Частицы в Konjunktiv II:\n"
        "• *doch* + würde: Du *würdest* es *doch* schaffen! — Ты же справишься!\n"
        "• *eigentlich* + sollte: Er *sollte eigentlich* früher kommen.\n"
        "• *ruhig* + könnte: Du *könntest ruhig* mehr fragen.\n"
        "• *nur* + wäre: *Wäre* es *nur* wärmer! — Если бы было теплее!\n\n"
        "Придают вежливость и смягчают высказывание.",
      "grammar_uz":
        "🔷 Konjunktiv II dagi zarrachalar:\n"
        "• *doch* + würde: Du *würdest* es *doch* schaffen! — Baribir uddalaysiz!\n"
        "• *eigentlich* + sollte: Er *sollte eigentlich* früher kommen.\n"
        "• *ruhig* + könnte: Du *könntest ruhig* mehr fragen.\n"
        "• *nur* + wäre: *Wäre* es *nur* wärmer!",
      "vocab":[
        {"de":"interkulturell","ru":"межкультурный","uz":"madaniyatlararo"},
        {"de":"die Kultur","ru":"культура","uz":"madaniyat"},
        {"de":"der Brauch","ru":"обычай","uz":"odat"},
        {"de":"Missverständnis","ru":"недопонимание","uz":"noto'g'ri tushunish"},
        {"de":"respektieren","ru":"уважать","uz":"hurmat qilmoq"},
        {"de":"tolerieren","ru":"терпеть / принимать","uz":"bag'rikenglik ko'rsatmoq"},
        {"de":"sich anpassen","ru":"адаптироваться","uz":"moslashmoq"},
        {"de":"die Vielfalt","ru":"разнообразие","uz":"xilma-xillik"},
        {"de":"der Vorurteil","ru":"предрассудок","uz":"xurofot"},
        {"de":"aufgeschlossen","ru":"открытый / восприимчивый","uz":"ochiq fikrli"},
        {"de":"neugierig","ru":"любопытный","uz":"qiziquvchan"},
        {"de":"der Kulturschock","ru":"культурный шок","uz":"madaniyat shoki"},
      ],
      "dialogue":[
        ("A","Hattest du einen Kulturschock in Deutschland?"),
        ("B","Eigentlich ja. Ich sollte mich ruhig mehr informieren vorher."),
        ("A","Was war am schwierigsten?"),
        ("B","Missverständnisse wegen anderer Bräuche. Wäre ich nur früher aufgeschlossener gewesen!"),
        ("A","Wie hast du dich angepasst?"),
        ("B","Ich würde doch jedem empfehlen, neugierig und tolerant zu sein."),
      ],
      "exercises":[
        {"type":"choice","q":"Du ___ ruhig mehr fragen. (мог бы спокойно — Konj.II + Partikel)",
         "opts":["kannst","könntest","solltest","würdest"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'aufgeschlossen'?",
         "opts":["закрытый","предрассудочный","открытый/восприимчивый","любопытный"],"ans":2},
        {"type":"fill","q":"___ es nur wärmer! (если бы только — Wunsch)",
         "opts":["Würde","Wäre","Hätte","Könnte"],"ans":1},
      ]
    },
    { "id":7, "title_de":"Umwelt und Nachhaltigkeit", "title_ru":"Экология и устойчивое развитие", "title_uz":"Ekologiya va barqaror rivojlanish",
      "grammar_topic":"Nominalstil | Номинальный стиль",
      "grammar_ru":
        "🔷 Номинальный стиль — официальный/научный язык\n"
        "Глагол → Существительное:\n"
        "• *entwickeln* → die Entwicklung\n"
        "• *entscheiden* → die Entscheidung\n"
        "• *verbessern* → die Verbesserung\n\n"
        "Вместо: «Wir müssen die Umwelt schützen»\n"
        "→ «Der Schutz der Umwelt ist notwendig.»",
      "grammar_uz":
        "🔷 Nominal uslub — rasmiy/ilmiy til\n"
        "Fe'l → Ot:\n"
        "• *entwickeln* → die Entwicklung\n"
        "• *entscheiden* → die Entscheidung\n"
        "• *verbessern* → die Verbesserung\n\n"
        "O'rniga: «Wir müssen die Umwelt schützen»\n"
        "→ «Der Schutz der Umwelt ist notwendig.»",
      "vocab":[
        {"de":"die Nachhaltigkeit","ru":"устойчивость / экологичность","uz":"barqarorlik"},
        {"de":"erneuerbar","ru":"возобновляемый","uz":"qayta tiklanadigan"},
        {"de":"die Solarenergie","ru":"солнечная энергия","uz":"quyosh energiyasi"},
        {"de":"die Windkraft","ru":"ветровая энергия","uz":"shamol energiyasi"},
        {"de":"der CO2-Ausstoß","ru":"выброс CO2","uz":"CO2 chiqindisi"},
        {"de":"der Treibhauseffekt","ru":"парниковый эффект","uz":"issiqxona effekti"},
        {"de":"die Artenvielfalt","ru":"биоразнообразие","uz":"biologik xilma-xillik"},
        {"de":"das Recycling","ru":"переработка","uz":"qayta ishlash"},
        {"de":"die Energiewende","ru":"энергетический переход","uz":"energiya o'tishi"},
        {"de":"ressourcenschonend","ru":"ресурсосберегающий","uz":"resurs tejamkor"},
        {"de":"die Aufforstung","ru":"лесонасаждение","uz":"o'rmon ekish"},
        {"de":"klimaneutral","ru":"климатически нейтральный","uz":"iqlim neytral"},
      ],
      "dialogue":[
        ("A","Was halten Sie vom Thema Nachhaltigkeit?"),
        ("B","Die Entwicklung erneuerbarer Energien ist entscheidend für die Zukunft."),
        ("A","Reicht das aus?"),
        ("B","Nein. Die Reduzierung des CO2-Ausstoßes und die Verbesserung der Artenvielfalt sind ebenso wichtig."),
        ("A","Was können Einzelpersonen tun?"),
        ("B","Durch ressourcenschonendes Verhalten und die Unterstützung von Recycling-Initiativen."),
      ],
      "exercises":[
        {"type":"choice","q":"Der ___ der Umwelt ist notwendig. (защита — Nominalstil von 'schützen')",
         "opts":["Schutz","Schützen","Schützer","Schützung"],"ans":0},
        {"type":"choice","q":"Was bedeutet 'die Nachhaltigkeit'?",
         "opts":["загрязнение","устойчивость","переработка","биоразнообразие"],"ans":1},
        {"type":"fill","q":"Die ___ von Energie ist wichtig. (сбережение — Nominalstil von 'sparen')",
         "opts":["Sparung","Einsparung","Sparnis","Gesparte"],"ans":1},
      ]
    },
    { "id":8, "title_de":"Beruf und Soziales", "title_ru":"Профессия и социальная жизнь", "title_uz":"Kasb va ijtimoiy hayot",
      "grammar_topic":"Finalsätze mit damit/um...zu | Целевые предложения",
      "grammar_ru":
        "🔷 Цель — разные подлежащие → *damit*\n"
        "Цель — одно подлежащее → *um … zu*\n\n"
        "• Ich erkläre es, *damit* du es verstehst.\n"
        "  (Я объясняю, чтобы ты понял)\n"
        "• Ich lerne, *um* Erfolg *zu haben*.\n"
        "  (Я учусь, чтобы достичь успеха)\n\n"
        "НЕЛЬЗЯ: Ich lerne, *damit* ich Erfolg zu haben. ❌",
      "grammar_uz":
        "🔷 Maqsad — har xil ega → *damit*\n"
        "Maqsad — bir ega → *um … zu*\n\n"
        "• Ich erkläre es, *damit* du es verstehst.\n"
        "  (Tushunishing uchun tushuntiraman)\n"
        "• Ich lerne, *um* Erfolg *zu haben*.\n"
        "  (Muvaffaqiyatga erishish uchun o'rganaman)\n\n"
        "NOTO'G'RI: Ich lerne, *damit* ich Erfolg zu haben. ❌",
      "vocab":[
        {"de":"das Sozialwesen","ru":"социальная сфера","uz":"ijtimoiy soha"},
        {"de":"die Rente","ru":"пенсия","uz":"pensiya"},
        {"de":"die Krankenversicherung","ru":"медицинская страховка","uz":"tibbiy sug'urta"},
        {"de":"die Steuer","ru":"налог","uz":"soliq"},
        {"de":"das Netzwerk","ru":"сеть / контакты","uz":"tarmoq / aloqalar"},
        {"de":"beruflich","ru":"профессиональный","uz":"professional"},
        {"de":"die Weiterbildung","ru":"дополнительное образование","uz":"qo'shimcha ta'lim"},
        {"de":"das Ehrenamt","ru":"волонтёрство","uz":"ixtiyoriy faoliyat"},
        {"de":"der Kollege","ru":"коллега","uz":"hamkasb"},
        {"de":"die Anerkennung","ru":"признание","uz":"tan olish"},
        {"de":"das Burnout","ru":"выгорание","uz":"charchash (psixologik)"},
        {"de":"die Work-Life-Balance","ru":"баланс работы и жизни","uz":"ish va hayot balansi"},
      ],
      "dialogue":[
        ("A","Warum engagierst du dich ehrenamtlich?"),
        ("B","Damit andere Menschen Hilfe bekommen, die ich geben kann."),
        ("A","Hast du auch berufliche Ziele?"),
        ("B","Ja, ich lerne ständig, um mich weiterzuentwickeln."),
        ("A","Wie vermeidest du Burnout?"),
        ("B","Ich achte auf Work-Life-Balance, damit ich langfristig gesund bleibe."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich erkläre es, ___ du es verstehst. (чтобы ты — разные субъекты)",
         "opts":["um zu","damit","weil","obwohl"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'das Ehrenamt'?",
         "opts":["пенсия","налог","волонтёрство","страховка"],"ans":2},
        {"type":"fill","q":"Ich lerne, ___ Erfolg zu haben. (чтобы — один субъект)",
         "opts":["damit","weil","um","dass"],"ans":2},
      ]
    },
  ]
}

B1_2 = {
  "title_ru": "Пороговый — часть 2", "title_uz": "O'rta daraja — 2-qism",
  "lessons": [
    { "id":1, "title_de":"Argumentieren und Diskutieren", "title_ru":"Аргументация и дискуссия", "title_uz":"Bahslashish va munozara",
      "grammar_topic":"Konzessive und adversative Konnektoren | Уступка и противопоставление",
      "grammar_ru":
        "🔷 Уступка/Противопоставление:\n"
        "• *während* = в то время как (контраст): Er schläft, *während* ich arbeite.\n"
        "• *wohingegen* = тогда как: Ich mag Kaffee, *wohingegen* er Tee bevorzugt.\n"
        "• *allerdings* = однако (Nachfeld): Das stimmt. *Allerdings* gibt es Ausnahmen.\n"
        "• *dennoch* = тем не менее: Es ist schwer, *dennoch* machen wir weiter.",
      "grammar_uz":
        "🔷 Yon va qarama-qarshi bog'lovchilar:\n"
        "• *während* = ayni paytda (kontrast)\n"
        "• *wohingegen* = esa\n"
        "• *allerdings* = biroq\n"
        "• *dennoch* = shunga qaramay",
      "vocab":[
        {"de":"das Argument","ru":"аргумент","uz":"argument"},
        {"de":"die These","ru":"тезис","uz":"tezis"},
        {"de":"behaupten","ru":"утверждать","uz":"da'vo qilmoq"},
        {"de":"widersprechen","ru":"возражать","uz":"e'tiroz bildirmoq"},
        {"de":"zustimmen","ru":"соглашаться","uz":"rozi bo'lmoq"},
        {"de":"belegen","ru":"подтверждать","uz":"isbotlamoq"},
        {"de":"das Gegenargument","ru":"контраргумент","uz":"qarshi argument"},
        {"de":"überzeugend","ru":"убедительный","uz":"ishontiruvchi"},
        {"de":"schlüssig","ru":"логичный","uz":"mantiqiy"},
        {"de":"die Debatte","ru":"дебаты","uz":"bahs"},
        {"de":"der Standpunkt","ru":"точка зрения","uz":"nuqtai nazar"},
        {"de":"kompromissbereit","ru":"готовый к компромиссу","uz":"kelishuvga tayyor"},
      ],
      "dialogue":[
        ("A","Ich behaupte, dass soziale Medien mehr schaden als nützen."),
        ("B","Dem widerspreche ich. Während sie Risiken haben, bieten sie auch große Chancen."),
        ("A","Kannst du das belegen?"),
        ("B","Ja. Wohingegen früher Kommunikation langsam war, ist sie heute sofort möglich."),
        ("A","Das stimmt, allerdings gibt es auch Falschinformationen."),
        ("B","Dennoch überwiegen die Vorteile, wenn man sie richtig nutzt."),
      ],
      "exercises":[
        {"type":"choice","q":"Er schläft, ___ ich arbeite. (в то время как — контраст)",
         "opts":["obwohl","weil","während","damit"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'widersprechen'?",
         "opts":["соглашаться","утверждать","возражать","подтверждать"],"ans":2},
        {"type":"fill","q":"Das Argument ist gut. ___ gibt es Ausnahmen. (однако)",
         "opts":["Dennoch","Allerdings","Wohingegen","Während"],"ans":1},
      ]
    },
    { "id":2, "title_de":"Geschichte und Erinnerungskultur", "title_ru":"История и культура памяти", "title_uz":"Tarix va xotira madaniyati",
      "grammar_topic":"Subjunktoren: je nachdem ob/wie/was | Субъюнкторы",
      "grammar_ru":
        "🔷 Субъюнкторы — вводят придаточные условия/обстоятельства:\n"
        "• *je nachdem ob/wie/was* — в зависимости от того, (ли/как/что)\n"
        "  Je nachdem, *wie* viel Zeit ich habe, komme ich.\n"
        "• *indem* — посредством того, что:\n"
        "  Man lernt Geschichte, *indem* man Dokumente liest.\n"
        "• *sodass* — так что (следствие):\n"
        "  Er lernte viel, *sodass* er alles verstand.",
      "grammar_uz":
        "🔷 Subjunktorlar:\n"
        "• *je nachdem ob/wie/was* — qanday/nima/qaysiligiga qarab\n"
        "• *indem* — ... qilish orqali\n"
        "• *sodass* — shunday qilib, shuning uchun",
      "vocab":[
        {"de":"die Geschichte","ru":"история","uz":"tarix"},
        {"de":"das Ereignis","ru":"событие","uz":"voqea"},
        {"de":"die Epoche","ru":"эпоха","uz":"davr"},
        {"de":"das Denkmal","ru":"памятник","uz":"yodgorlik"},
        {"de":"erinnern (sich an)","ru":"помнить","uz":"eslamoq"},
        {"de":"vergessen","ru":"забывать","uz":"unutmoq"},
        {"de":"das Dokument","ru":"документ","uz":"hujjat"},
        {"de":"die Quelle","ru":"источник","uz":"manba"},
        {"de":"interpretieren","ru":"интерпретировать","uz":"talqin qilmoq"},
        {"de":"der Zeuge","ru":"свидетель","uz":"guvoh"},
        {"de":"überliefern","ru":"передавать (традиции)","uz":"avloddan-avlodga o'tkazmoq"},
        {"de":"das Erbe","ru":"наследие","uz":"meros"},
      ],
      "dialogue":[
        ("A","Wie lernt man Geschichte am besten?"),
        ("B","Indem man Zeitzeugen zuhört und Dokumente liest."),
        ("A","Aber Dokumente können subjektiv sein."),
        ("B","Stimmt, je nachdem, wie man sie interpretiert, bekommt man verschiedene Bilder."),
        ("A","Ist es wichtig, Denkmäler zu erhalten?"),
        ("B","Ja, sodass zukünftige Generationen das Erbe kennen und nicht vergessen."),
      ],
      "exercises":[
        {"type":"choice","q":"Man lernt, ___ man Bücher liest. (посредством того что)",
         "opts":["indem","sodass","je nachdem","während"],"ans":0},
        {"type":"choice","q":"Was bedeutet 'das Erbe'?",
         "opts":["событие","свидетель","наследие","документ"],"ans":2},
        {"type":"fill","q":"Er lernte viel, ___ er alles verstand. (так что)",
         "opts":["indem","sodass","obwohl","weil"],"ans":1},
      ]
    },
    { "id":3, "title_de":"Digitale Zukunft", "title_ru":"Цифровое будущее", "title_uz":"Raqamli kelajak",
      "grammar_topic":"Erweiterte Infinitivkonstruktionen | Расширенные инфинитивные конструкции",
      "grammar_ru":
        "🔷 Расширенные инфинитивы:\n"
        "• *statt … zu*: Statt fernzusehen, lese ich.\n"
        "• *ohne … zu*: Er sprach, ohne zu pausieren.\n"
        "• *anstatt … zu*: Anstatt zu klagen, handeln wir.\n"
        "• *als ob* + Konjunktiv II (сравнение):\n"
        "  Er tut so, *als ob* er alles wüsste.\n"
        "  (Он ведёт себя так, как будто знает всё)",
      "grammar_uz":
        "🔷 Kengaytirilgan infinitiv konstruktsiyalar:\n"
        "• *statt … zu*: Statt fernzusehen, lese ich.\n"
        "• *ohne … zu*: Er sprach, ohne zu pausieren.\n"
        "• *anstatt … zu*: Anstatt zu klagen, handeln wir.\n"
        "• *als ob* + Konjunktiv II: Er tut so, *als ob* er alles wüsste.",
      "vocab":[
        {"de":"die künstliche Intelligenz","ru":"искусственный интеллект","uz":"sun'iy intellekt"},
        {"de":"die Digitalisierung","ru":"цифровизация","uz":"raqamlashtirish"},
        {"de":"der Algorithmus","ru":"алгоритм","uz":"algoritm"},
        {"de":"die Automatisierung","ru":"автоматизация","uz":"avtomatlashtirish"},
        {"de":"das Datenschutz","ru":"защита данных","uz":"ma'lumotlarni himoya qilish"},
        {"de":"vernetzen","ru":"соединять в сеть","uz":"tarmoqqa ulash"},
        {"de":"der Roboter","ru":"робот","uz":"robot"},
        {"de":"der Chip","ru":"чип","uz":"chip"},
        {"de":"die Cloud","ru":"облако (хранилище)","uz":"bulut (saqlash)"},
        {"de":"verschlüsseln","ru":"шифровать","uz":"shifrlash"},
        {"de":"die Cybersicherheit","ru":"кибербезопасность","uz":"kiber xavfsizlik"},
        {"de":"innovativ","ru":"инновационный","uz":"innovatsion"},
      ],
      "dialogue":[
        ("A","Wie verändert KI unsere Welt?"),
        ("B","Anstatt viele Aufgaben manuell zu erledigen, übernehmen Algorithmen die Arbeit."),
        ("A","Ist das nicht gefährlich?"),
        ("B","Er tut manchmal so, als ob KI alles selbst entscheide — aber der Mensch steuert sie."),
        ("A","Was ist mit Datenschutz?"),
        ("B","Ohne Daten zu verschlüsseln, ist Cybersicherheit nicht möglich."),
      ],
      "exercises":[
        {"type":"choice","q":"___ zu lernen, schaut er nur TV. (вместо того чтобы)",
         "opts":["Um","Ohne","Statt","Damit"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'die Automatisierung'?",
         "opts":["шифрование","кибербезопасность","автоматизация","алгоритм"],"ans":2},
        {"type":"fill","q":"Er tut so, als ___ er alles wüsste. (als ob, Konjunktiv II)",
         "opts":["wenn","ob","dass","ob er"],"ans":1},
      ]
    },
    { "id":4, "title_de":"Psychologie und Verhalten", "title_ru":"Психология и поведение", "title_uz":"Psixologiya va xulq",
      "grammar_topic":"Modalpartikeln im komplexen Satz | Частицы в сложных предложениях",
      "grammar_ru":
        "🔷 Частицы в разных контекстах:\n"
        "• *doch* в восклицании: Das ist *doch* unmöglich!\n"
        "• *halt* = просто, ну: Das ist *halt* so.\n"
        "• *eben* = именно так: Das ist *eben* das Problem.\n"
        "• *wohl* = наверно, видимо: Er ist *wohl* krank.\n"
        "• *schon* = уже/конечно: Das wird *schon* klappen.",
      "grammar_uz":
        "🔷 Murakkab gaplarda zarrachalar:\n"
        "• *doch* undov: Das ist *doch* unmöglich!\n"
        "• *halt* = shunchaki: Das ist *halt* so.\n"
        "• *eben* = aynan: Das ist *eben* das Problem.\n"
        "• *wohl* = ehtimol: Er ist *wohl* krank.\n"
        "• *schon* = allaqachon/albatta: Das wird *schon* klappen.",
      "vocab":[
        {"de":"die Psychologie","ru":"психология","uz":"psixologiya"},
        {"de":"das Verhalten","ru":"поведение","uz":"xulq-atvor"},
        {"de":"die Emotion","ru":"эмоция","uz":"his-tuyg'u"},
        {"de":"der Stress","ru":"стресс","uz":"stress"},
        {"de":"bewältigen","ru":"справляться","uz":"hal qilmoq"},
        {"de":"motivieren","ru":"мотивировать","uz":"motivatsiyalamoq"},
        {"de":"die Angst","ru":"страх / тревога","uz":"qo'rquv / tashvish"},
        {"de":"das Selbstbewusstsein","ru":"уверенность в себе","uz":"o'z-o'ziga ishonch"},
        {"de":"sich verhalten","ru":"вести себя","uz":"o'zini tutmoq"},
        {"de":"beeinflussen","ru":"влиять","uz":"ta'sir qilmoq"},
        {"de":"der Konflikt","ru":"конфликт","uz":"ziddiyat"},
        {"de":"lösen","ru":"решать","uz":"hal qilmoq"},
      ],
      "dialogue":[
        ("A","Warum reagieren Menschen so unterschiedlich auf Stress?"),
        ("B","Das ist halt die Psychologie — jeder hat eben andere Strategien."),
        ("A","Gibt es bessere Methoden?"),
        ("B","Doch! Man kann Ängste schon bewältigen, wenn man die richtigen Techniken kennt."),
        ("A","Was beeinflusst das Selbstbewusstsein am meisten?"),
        ("B","Er ist wohl durch frühe Erfahrungen geprägt — das ist eben der Kern des Problems."),
      ],
      "exercises":[
        {"type":"choice","q":"Das ist ___ das Problem. (именно это — Partikel)",
         "opts":["halt","wohl","eben","doch"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'bewältigen'?",
         "opts":["мотивировать","справляться","влиять","решать"],"ans":1},
        {"type":"fill","q":"Das wird ___ klappen. (получится, конечно — уверенность)",
         "opts":["halt","eben","wohl","schon"],"ans":3},
      ]
    },
    { "id":5, "title_de":"Stadtentwicklung und Wohnen", "title_ru":"Городское развитие", "title_uz":"Shahar rivojlanishi",
      "grammar_topic":"Präpositionen mit Genitiv (Wiederholung + neue) | Генитивные предлоги",
      "grammar_ru":
        "🔷 Предлоги с родительным падежом (расширение):\n"
        "• *aufgrund* = вследствие, из-за (офиц.)\n"
        "• *mithilfe* = с помощью\n"
        "• *angesichts* = ввиду\n"
        "• *im Hinblick auf* = с точки зрения\n"
        "• *hinsichtlich* = в отношении\n\n"
        "• *Aufgrund* des Lärms ziehen viele um.\n"
        "• *Mithilfe* moderner Technik wird gebaut.",
      "grammar_uz":
        "🔷 Genitiv bilan predloglar (kengaytirish):\n"
        "• *aufgrund* = sababli (rasmiy)\n"
        "• *mithilfe* = yordamida\n"
        "• *angesichts* = ko'zlayotgan\n"
        "• *im Hinblick auf* = nuqtai nazardan\n"
        "• *hinsichtlich* = ...ga nisbatan",
      "vocab":[
        {"de":"die Stadtentwicklung","ru":"городское развитие","uz":"shahar rivojlanishi"},
        {"de":"die Infrastruktur","ru":"инфраструктура","uz":"infratuzilma"},
        {"de":"der Wohnraum","ru":"жилплощадь","uz":"turar joy maydoni"},
        {"de":"das Viertel","ru":"квартал / район","uz":"kvartal / mahalla"},
        {"de":"die Sanierung","ru":"реновация","uz":"renovatsiya"},
        {"de":"nachhaltig","ru":"устойчивый / экологичный","uz":"barqaror"},
        {"de":"der Lärm","ru":"шум","uz":"shovqin"},
        {"de":"die Lebensqualität","ru":"качество жизни","uz":"hayot sifati"},
        {"de":"das Grünfläche","ru":"зелёная зона","uz":"yashil zona"},
        {"de":"verdichten","ru":"уплотнять (застройку)","uz":"zichlashmoq"},
        {"de":"suburbanisieren","ru":"субурбанизировать","uz":"suburbanizatsiya"},
        {"de":"barrierefreiheit","ru":"доступность для всех","uz":"hammaga qulay"},
      ],
      "dialogue":[
        ("A","Warum zieht die Bevölkerung in die Vororte?"),
        ("B","Aufgrund des Lärms und hoher Mieten in der Innenstadt."),
        ("A","Wie kann man die Lebensqualität in der Stadt verbessern?"),
        ("B","Mithilfe nachhaltiger Infrastruktur und mehr Grünflächen."),
        ("A","Angesichts des Klimawandels — welche Priorität hat das?"),
        ("B","Hinsichtlich der Zukunft ist nachhaltige Stadtplanung unverzichtbar."),
      ],
      "exercises":[
        {"type":"choice","q":"___ des Lärms ziehen viele um. (вследствие — Genitiv)",
         "opts":["Wegen","Aufgrund","Mithilfe","Trotz"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'die Lebensqualität'?",
         "opts":["инфраструктура","шум","качество жизни","реновация"],"ans":2},
        {"type":"fill","q":"___ moderner Technik wird die Stadt umgebaut. (с помощью)",
         "opts":["Aufgrund","Angesichts","Mithilfe","Hinsichtlich"],"ans":2},
      ]
    },
    { "id":6, "title_de":"Kunst und Kreativität", "title_ru":"Искусство и творчество", "title_uz":"San'at va ijodkorlik",
      "grammar_topic":"Attribute: Apposition und erweitertes Partizip | Аппозиция и распространённое причастие",
      "grammar_ru":
        "🔷 Аппозиция — дополнительное определение в том же падеже:\n"
        "• Picasso, *der bekannteste Künstler des 20. Jh.*, ...\n"
        "• Berlin, *die Hauptstadt Deutschlands*, ...\n\n"
        "🔷 Распространённое причастное определение (письм.стиль):\n"
        "• das *von Millionen bewunderte* Gemälde\n"
        "• der *im 19. Jahrhundert entstandene* Roman",
      "grammar_uz":
        "🔷 Appozitsiya — bir xil kelishikdagi qo'shimcha ta'rif:\n"
        "• Picasso, *der bekannteste Künstler des 20. Jh.*, ...\n"
        "• Berlin, *die Hauptstadt Deutschlands*, ...\n\n"
        "🔷 Kengaytirilgan sifatdosh ta'rif (yozma uslub):\n"
        "• das *von Millionen bewunderte* Gemälde\n"
        "• der *im 19. Jahrhundert entstandene* Roman",
      "vocab":[
        {"de":"das Gemälde","ru":"картина","uz":"rasm"},
        {"de":"die Skulptur","ru":"скульптура","uz":"haykaltaroshlik"},
        {"de":"der Künstler","ru":"художник","uz":"rassom"},
        {"de":"das Meisterwerk","ru":"шедевр","uz":"shoh asar"},
        {"de":"erschaffen","ru":"создавать","uz":"yaratmoq"},
        {"de":"inspirieren","ru":"вдохновлять","uz":"ilhomlantirmoq"},
        {"de":"ausdrücken","ru":"выражать","uz":"ifodalash"},
        {"de":"die Galerie","ru":"галерея","uz":"galereya"},
        {"de":"die Epoche","ru":"эпоха","uz":"davr"},
        {"de":"das Motiv","ru":"мотив","uz":"motiv"},
        {"de":"avantgardistisch","ru":"авангардный","uz":"avangard"},
        {"de":"zeitgenössisch","ru":"современный (об искусстве)","uz":"zamonaviy (san'at)"},
      ],
      "dialogue":[
        ("A","Was hältst du von zeitgenössischer Kunst?"),
        ("B","Das von vielen kritisierte Werk von heute ist das Meisterwerk von morgen."),
        ("A","Picasso, der bekannteste Künstler des 20. Jahrhunderts, war auch umstritten."),
        ("B","Stimmt! Kunst soll Emotionen ausdrücken und zum Denken inspirieren."),
        ("A","Was ist dein Lieblingskunstwerk?"),
        ("B","Das im Louvre ausgestellte Gemälde — die Mona Lisa. Einfach zeitlos."),
      ],
      "exercises":[
        {"type":"choice","q":"Das ___ Gemälde ist berühmt. (восхищаемое миллионами)",
         "opts":["bewundernde","bewunderte","von Millionen bewunderte","bewundernd"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'das Meisterwerk'?",
         "opts":["мотив","галерея","шедевр","скульптура"],"ans":2},
        {"type":"fill","q":"Picasso, ___ bekannteste Künstler, war genial. (Appositon, der)",
         "opts":["die","das","den","der"],"ans":3},
      ]
    },
    { "id":7, "title_de":"Gesundheitssystem und Soziales", "title_ru":"Система здравоохранения", "title_uz":"Sog'liqni saqlash tizimi",
      "grammar_topic":"Passiv mit Bedeutungsnuancen | Оттенки пассива",
      "grammar_ru":
        "🔷 Виды пассива:\n"
        "1. Vorgangspassiv (действие): Das Haus *wird gebaut*.\n"
        "2. Zustandspassiv (состояние): Das Haus *ist gebaut*.\n"
        "3. Bekommen-Passiv (разг.):\n"
        "   Ich *bekomme* das Formular *zugeschickt*.\n"
        "   (Мне присылают форму)\n\n"
        "Разница: «wird repariert» (процесс) vs «ist repariert» (готово)",
      "grammar_uz":
        "🔷 Passivning turlari:\n"
        "1. Vorgangspassiv (jarayon): Das Haus *wird gebaut*.\n"
        "2. Zustandspassiv (holat): Das Haus *ist gebaut*.\n"
        "3. Bekommen-Passiv (so'zlashuv):\n"
        "   Ich *bekomme* das Formular *zugeschickt*.",
      "vocab":[
        {"de":"das Gesundheitssystem","ru":"система здравоохранения","uz":"sog'liqni saqlash tizimi"},
        {"de":"die Krankenversicherung","ru":"медицинская страховка","uz":"tibbiy sug'urta"},
        {"de":"der Arzttermin","ru":"запись к врачу","uz":"shifokorga yozilish"},
        {"de":"die Notaufnahme","ru":"скорая помощь / приёмный покой","uz":"shoshilinch yordам"},
        {"de":"verschreiben","ru":"выписывать (рецепт)","uz":"retsept yozmoq"},
        {"de":"behandeln","ru":"лечить","uz":"davolash"},
        {"de":"die Diagnose","ru":"диагноз","uz":"tashxis"},
        {"de":"der Facharzt","ru":"специалист (врач)","uz":"mutaxassis shifokor"},
        {"de":"die Vorsorge","ru":"профилактика","uz":"profilaktika"},
        {"de":"die Rehabilitation","ru":"реабилитация","uz":"reabilitatsiya"},
        {"de":"der Zuzahlung","ru":"доплата","uz":"qo'shimcha to'lov"},
        {"de":"ambulant / stationär","ru":"амбулаторно / стационарно","uz":"ambulatoriya / statsionar"},
      ],
      "dialogue":[
        ("A","Wie funktioniert das Gesundheitssystem in Deutschland?"),
        ("B","Jeder ist krankenversichert. Wenn man krank ist, wird man behandelt."),
        ("A","Muss man lange auf einen Facharzttermin warten?"),
        ("B","Ja, das dauert manchmal Wochen. Zum Glück ist die Notaufnahme immer offen."),
        ("A","Bekommt man Medikamente verschrieben?"),
        ("B","Ja, mir wurde letztens ein Rezept zugeschickt — das Bekommen-Passiv im Alltag!"),
      ],
      "exercises":[
        {"type":"choice","q":"Das Auto ___ gerade repariert. (в процессе — Vorgangspassiv)",
         "opts":["ist","wird","wurde","war"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'die Vorsorge'?",
         "opts":["диагноз","реабилитация","профилактика","лечение"],"ans":2},
        {"type":"fill","q":"Das Auto ___ repariert. (уже готово — Zustandspassiv)",
         "opts":["wird","wurde","ist","war"],"ans":2},
      ]
    },
    { "id":8, "title_de":"Zukunftsvision und persönliche Ziele", "title_ru":"Будущее и личные цели", "title_uz":"Kelajak va shaxsiy maqsadlar",
      "grammar_topic":"Gesamtwiederholung — komplexe Strukturen | Итоговое повторение",
      "grammar_ru":
        "🔷 Итоговое повторение B1 — ключевые структуры:\n\n"
        "1. Konjunktiv II: Wenn ich Zeit hätte, würde ich mehr reisen.\n"
        "2. Passiv+Modal: Ziele müssen verfolgt werden.\n"
        "3. Relativsätze: Das Ziel, das ich verfolge, ist klar.\n"
        "4. Infinitivkonstruktionen: um Ziele zu erreichen\n"
        "5. Konzessiv: Obwohl es schwer ist, gebe ich nicht auf.\n"
        "6. Nominalstil: Die Verfolgung von Zielen erfordert Ausdauer.",
      "grammar_uz":
        "🔷 B1 yakuniy takrorlash — asosiy strukturalar:\n\n"
        "1. Konjunktiv II: Wenn ich Zeit hätte, würde ich mehr reisen.\n"
        "2. Passiv+Modal: Ziele müssen verfolgt werden.\n"
        "3. Relativsätze: Das Ziel, das ich verfolge, ist klar.\n"
        "4. Infinitivkonstruktionen: um Ziele zu erreichen\n"
        "5. Konzessiv: Obwohl es schwer ist, gebe ich nicht auf.\n"
        "6. Nominalstil: Die Verfolgung von Zielen erfordert Ausdauer.",
      "vocab":[
        {"de":"die Vision","ru":"видение / мечта","uz":"tasavvur / orzu"},
        {"de":"das Ziel","ru":"цель","uz":"maqsad"},
        {"de":"verfolgen","ru":"преследовать (цель)","uz":"maqsadga intilmoq"},
        {"de":"die Ausdauer","ru":"настойчивость","uz":"qat'iyat"},
        {"de":"der Rückschlag","ru":"неудача","uz":"muvaffaqiyatsizlik"},
        {"de":"überwinden","ru":"преодолевать","uz":"yengmoq"},
        {"de":"der Durchbruch","ru":"прорыв","uz":"yutuq"},
        {"de":"langfristig","ru":"долгосрочный","uz":"uzoq muddatli"},
        {"de":"kurzfristig","ru":"краткосрочный","uz":"qisqa muddatli"},
        {"de":"realistisch","ru":"реалистичный","uz":"realistik"},
        {"de":"die Motivation","ru":"мотивация","uz":"motivatsiya"},
        {"de":"Schritt für Schritt","ru":"шаг за шагом","uz":"qadam-baqadam"},
      ],
      "dialogue":[
        ("A","Was sind deine langfristigen Ziele?"),
        ("B","Wenn ich alles schaffen würde, wäre mein größtes Ziel, ein eigenes Unternehmen zu gründen."),
        ("A","Obwohl das schwer ist?"),
        ("B","Ja! Rückschläge müssen überwunden werden. Das ist normal."),
        ("A","Wie hältst du deine Motivation aufrecht?"),
        ("B","Schritt für Schritt. Das Ziel, das ich verfolge, gibt mir täglich Energie."),
      ],
      "exercises":[
        {"type":"choice","q":"Wenn ich Zeit ___, würde ich mehr reisen. (Konj.II von haben)",
         "opts":["habe","hatte","hätte","gehabt"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'überwinden'?",
         "opts":["достигать","преодолевать","мотивировать","отказываться"],"ans":1},
        {"type":"fill","q":"Ziele müssen ___ werden. (должны преследоваться — Passiv+Modal)",
         "opts":["verfolgen","verfolgt","verfolgend","zu verfolgen"],"ans":1},
      ]
    },
  ]
}
