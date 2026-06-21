"""A2.1 + A2.2 content"""

A2_1 = {
  "title_ru": "Элементарный — часть 1", "title_uz": "Boshlang'ich-o'rta — 1-qism",
  "lessons": [
    { "id":1, "title_de":"Biografien und Lebenslauf", "title_ru":"Биографии и резюме", "title_uz":"Biografiya va rezyume",
      "grammar_topic":"Präteritum (war, hatte, konnte) | Простое прошедшее",
      "grammar_ru":
        "🔷 Präteritum — письменное прошедшее время\n"
        "sein → war: ich war, du warst, er war\n"
        "haben → hatte: ich hatte, du hattest\n"
        "können → konnte, müssen → musste\n\n"
        "• Er *war* Lehrer. — Он был учителем.\n"
        "• Sie *hatte* keine Zeit. — У неё не было времени.\n"
        "• Ich *musste* früh aufstehen. — Мне нужно было рано вставать.",
      "grammar_uz":
        "🔷 Präteritum — yozma o'tgan zamon\n"
        "sein → war: ich war, du warst, er war\n"
        "haben → hatte: ich hatte, du hattest\n"
        "können → konnte, müssen → musste\n\n"
        "• Er *war* Lehrer. — U o'qituvchi edi.\n"
        "• Sie *hatte* keine Zeit. — Uning vaqti yo'q edi.\n"
        "• Ich *musste* früh aufstehen. — Men erta turishim kerak edi.",
      "vocab":[
        {"de":"die Biografie","ru":"биография","uz":"biografiya"},
        {"de":"geboren werden","ru":"родиться","uz":"tug'ilmoq"},
        {"de":"aufwachsen","ru":"расти / вырасти","uz":"o'smoq"},
        {"de":"die Ausbildung","ru":"образование","uz":"ta'lim"},
        {"de":"die Schule besuchen","ru":"ходить в школу","uz":"maktabga bormoq"},
        {"de":"das Studium","ru":"учёба в вузе","uz":"oliy ta'lim"},
        {"de":"der Abschluss","ru":"окончание / диплом","uz":"diplom"},
        {"de":"heiraten","ru":"жениться","uz":"uylanmoq"},
        {"de":"der Lebenslauf","ru":"резюме","uz":"rezyume"},
        {"de":"die Erfahrung","ru":"опыт","uz":"tajriba"},
        {"de":"früher / damals","ru":"раньше / тогда","uz":"avval / o'shanda"},
        {"de":"der Erfolg","ru":"успех","uz":"muvaffaqiyat"},
      ],
      "dialogue":[
        ("A","Erzählen Sie etwas über sich."),
        ("B","Ich wurde 1990 in Taschkent geboren und bin dort aufgewachsen."),
        ("A","Wo haben Sie studiert?"),
        ("B","Ich habe an der Technischen Universität studiert."),
        ("A","Und was haben Sie danach gemacht?"),
        ("B","Danach habe ich als Ingenieur gearbeitet, aber dann wollte ich Deutsch lernen."),
      ],
      "exercises":[
        {"type":"choice","q":"Er ___ früher Lehrer. (был, Präteritum von 'sein')",
         "opts":["hatte","war","wurde","ist"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'der Abschluss'?",
         "opts":["начало","опыт","диплом/окончание","работа"],"ans":2},
        {"type":"fill","q":"Ich ___ keine Zeit. (у меня не было, Prät. haben)",
         "opts":["war","hatte","musste","wollte"],"ans":1},
      ]
    },
    { "id":2, "title_de":"Wohnen und Umziehen", "title_ru":"Жильё и переезд", "title_uz":"Uy va ko'chish",
      "grammar_topic":"Wechselpräpositionen (Wo/Wohin) | Предлоги движения и места",
      "grammar_ru":
        "🔷 Двойные предлоги: in, an, auf, über, unter, vor, hinter, neben, zwischen\n"
        "Место (*wo?*) → Dativ: Er ist *im* Zimmer.\n"
        "Направление (*wohin?*) → Akkusativ: Er geht *ins* Zimmer.\n\n"
        "• Das Buch liegt *auf dem* Tisch. (где?)\n"
        "• Ich lege das Buch *auf den* Tisch. (куда?)",
      "grammar_uz":
        "🔷 Ikkilamchi predloglar: in, an, auf, über, unter, vor, hinter, neben, zwischen\n"
        "Joy (*wo?*) → Dativ: Er ist *im* Zimmer.\n"
        "Yo'nalish (*wohin?*) → Akkusativ: Er geht *ins* Zimmer.\n\n"
        "• Das Buch liegt *auf dem* Tisch. (qaerda?)\n"
        "• Ich lege das Buch *auf den* Tisch. (qaerga?)",
      "vocab":[
        {"de":"umziehen","ru":"переезжать","uz":"ko'chib o'tmoq"},
        {"de":"die Miete","ru":"аренда / квартплата","uz":"ijara"},
        {"de":"der Vermieter","ru":"арендодатель","uz":"ijaraberuvchi"},
        {"de":"der Mieter","ru":"арендатор","uz":"ijarachi"},
        {"de":"die Kaution","ru":"залог","uz":"garov"},
        {"de":"kündigen","ru":"расторгать договор","uz":"shartnomani bekor qilmoq"},
        {"de":"renovieren","ru":"ремонтировать","uz":"ta'mirlash"},
        {"de":"die Nebenkosten","ru":"коммунальные услуги","uz":"kommunal to'lovlar"},
        {"de":"der Aufzug","ru":"лифт","uz":"lift"},
        {"de":"die Etage / das Stockwerk","ru":"этаж","uz":"qavat"},
        {"de":"das Erdgeschoss","ru":"первый этаж","uz":"birinchi qavat"},
        {"de":"möbliert","ru":"меблированный","uz":"mebel bilan jihozlangan"},
      ],
      "dialogue":[
        ("A","Ich suche eine neue Wohnung."),
        ("B","Was für eine Wohnung suchst du?"),
        ("A","2 Zimmer, nicht zu teuer. Maximal 600 Euro Miete."),
        ("B","Inklusive Nebenkosten?"),
        ("A","Ja, am liebsten. Und nicht im Erdgeschoss."),
        ("B","Ich kenne eine Wohnung im 3. Stockwerk — 580 Euro, möbliert."),
        ("A","Perfekt! Kann ich sie besichtigen?"),
      ],
      "exercises":[
        {"type":"choice","q":"Das Buch liegt ___ dem Tisch. (на столе — где?)",
         "opts":["auf","in","an","über"],"ans":0},
        {"type":"choice","q":"Was bedeutet 'umziehen'?",
         "opts":["ремонтировать","переезжать","арендовать","расторгать"],"ans":1},
        {"type":"fill","q":"Ich lege das Heft ___ den Tisch. (на стол — куда?)",
         "opts":["auf","an","in","unter"],"ans":0},
      ]
    },
    { "id":3, "title_de":"Medien und Kommunikation", "title_ru":"Медиа и коммуникация", "title_uz":"Media va kommunikatsiya",
      "grammar_topic":"Relativsätze (Nominativ/Akkusativ) | Относительные предложения",
      "grammar_ru":
        "🔷 Относительные придаточные — описывают существительное\n"
        "Относительное местоимение согласуется с существительным:\n"
        "der → der/den, die → die, das → das\n\n"
        "• Das ist der Mann, *der* Deutsch spricht.\n"
        "• Ich suche ein Buch, *das* interessant ist.\n"
        "• Die Frau, *die* ich kenne, ist Ärztin.",
      "grammar_uz":
        "🔷 Nisbiy gaplar — otni tavsiflaydi\n"
        "Nisbiy olmosh otga moslashadi:\n"
        "der → der/den, die → die, das → das\n\n"
        "• Das ist der Mann, *der* Deutsch spricht.\n"
        "• Ich suche ein Buch, *das* interessant ist.\n"
        "• Die Frau, *die* ich kenne, ist Ärztin.",
      "vocab":[
        {"de":"das Internet","ru":"интернет","uz":"internet"},
        {"de":"die Zeitung","ru":"газета","uz":"gazeta"},
        {"de":"die Zeitschrift","ru":"журнал","uz":"jurnal"},
        {"de":"das Smartphone","ru":"смартфон","uz":"smartfon"},
        {"de":"die App","ru":"приложение","uz":"ilova"},
        {"de":"soziale Medien","ru":"социальные сети","uz":"ijtimoiy tarmoqlar"},
        {"de":"herunterladen","ru":"скачивать","uz":"yuklab olmoq"},
        {"de":"die Nachricht","ru":"сообщение / новость","uz":"xabar"},
        {"de":"schicken / senden","ru":"отправлять","uz":"yubormoq"},
        {"de":"kommentieren","ru":"комментировать","uz":"izoh qoldirmoq"},
        {"de":"folgen","ru":"подписываться","uz":"kuzatmoq"},
        {"de":"das Passwort","ru":"пароль","uz":"parol"},
      ],
      "dialogue":[
        ("A","Liest du noch Zeitung?"),
        ("B","Nein, ich lese alles im Internet. Zeitungen, die ich früher gekauft habe, lese ich jetzt online."),
        ("A","Welche Apps benutzt du?"),
        ("B","Ich habe Apps, die mir Nachrichten schicken."),
        ("A","Bist du auch in sozialen Medien aktiv?"),
        ("B","Ja, aber ich folge nur Seiten, die nützlich sind."),
      ],
      "exercises":[
        {"type":"choice","q":"Das ist das Buch, ___ sehr interessant ist. (das/die/der)",
         "opts":["der","die","das","den"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'herunterladen'?",
         "opts":["загружать","отправлять","комментировать","удалять"],"ans":0},
        {"type":"fill","q":"Die Frau, ___ ich kenne, ist Ärztin. (которую, Akk.)",
         "opts":["der","die","das","den"],"ans":1},
      ]
    },
    { "id":4, "title_de":"Gesundheit und Ernährung", "title_ru":"Здоровье и питание", "title_uz":"Salomatlik va ovqatlanish",
      "grammar_topic":"Konjunktiv II (würde, hätte, wäre) | Сослагательное наклонение",
      "grammar_ru":
        "🔷 Konjunktiv II — вежливые просьбы, нереальные условия\n"
        "würde + Infinitiv (универсально)\n"
        "wäre (sein), hätte (haben), könnte (können)\n\n"
        "• *Würden* Sie mir helfen? — Не могли бы вы помочь?\n"
        "• Ich *hätte* gern einen Tisch. — Мне хотелось бы столик.\n"
        "• Das *wäre* toll! — Это было бы здорово!",
      "grammar_uz":
        "🔷 Konjunktiv II — muloyim so'rovlar, norealistik shartlar\n"
        "würde + Infinitiv (universal)\n"
        "wäre (sein), hätte (haben), könnte (können)\n\n"
        "• *Würden* Sie mir helfen? — Yordam bera olarmidingiz?\n"
        "• Ich *hätte* gern einen Tisch. — Bir stol olsam.\n"
        "• Das *wäre* toll! — Bu ajoyib bo'lardi!",
      "vocab":[
        {"de":"die Ernährung","ru":"питание","uz":"ovqatlanish"},
        {"de":"gesund / ungesund","ru":"здоровый / нездоровый","uz":"sog'lom / nosog'lom"},
        {"de":"das Vitamin","ru":"витамин","uz":"vitamin"},
        {"de":"die Kalorien","ru":"калории","uz":"kaloriya"},
        {"de":"die Diät","ru":"диета","uz":"dieta"},
        {"de":"vegetarisch","ru":"вегетарианский","uz":"vegetarian"},
        {"de":"bio / ökologisch","ru":"органический / экологический","uz":"organik / ekologik"},
        {"de":"das Fast Food","ru":"фастфуд","uz":"fast food"},
        {"de":"abnehmen","ru":"худеть","uz":"ozmoq"},
        {"de":"zunehmen","ru":"набирать вес","uz":"semirmoq"},
        {"de":"Sport treiben","ru":"заниматься спортом","uz":"sport bilan shug'ullanmoq"},
        {"de":"der Stress","ru":"стресс","uz":"stress"},
      ],
      "dialogue":[
        ("A","Ich würde gern gesünder leben. Was empfehlen Sie?"),
        ("B","Sie sollten mehr Obst und Gemüse essen."),
        ("A","Ich esse nicht gern Salat."),
        ("B","Das wäre aber wichtig. Und weniger Fast Food — das hätte großen Einfluss."),
        ("A","Würden Sie auch Sport empfehlen?"),
        ("B","Ja! 30 Minuten täglich wären ideal."),
      ],
      "exercises":[
        {"type":"choice","q":"___ Sie mir bitte helfen? (не могли бы, вежливо)",
         "opts":["Können","Würden","Wollen","Mögen"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'abnehmen'?",
         "opts":["набирать вес","похудеть","есть меньше","бегать"],"ans":1},
        {"type":"fill","q":"Das ___ sehr gut. (было бы, Konj. II von sein)",
         "opts":["würde","wäre","hätte","könnte"],"ans":1},
      ]
    },
    { "id":5, "title_de":"Natur und Umwelt", "title_ru":"Природа и окружающая среда", "title_uz":"Tabiat va atrof-muhit",
      "grammar_topic":"Passiv (Präsens) | Пассивный залог настоящего времени",
      "grammar_ru":
        "🔷 Пассив = werden + Partizip II\n"
        "Фокус на действии, не на исполнителе\n\n"
        "• Deutsch *wird* weltweit *gesprochen*. — На немецком говорят во всём мире.\n"
        "• Müll *wird* getrennt *gesammelt*. — Мусор сортируется.\n"
        "• Das Essen *wird* gekocht. — Еда готовится.\n\n"
        "С указанием исполнителя: *von* + Dativ",
      "grammar_uz":
        "🔷 Passiv = werden + Partizip II\n"
        "E'tibor harakatga, ijrochiga emas\n\n"
        "• Deutsch *wird* weltweit *gesprochen*. — Nemis tili butun dunyoda gapiriladı.\n"
        "• Müll *wird* getrennt *gesammelt*. — Chiqindi saraladi.\n"
        "• Das Essen *wird* gekocht. — Ovqat pishirilmoqda.\n\n"
        "Ijrochi bilan: *von* + Dativ",
      "vocab":[
        {"de":"die Natur","ru":"природа","uz":"tabiat"},
        {"de":"die Umwelt","ru":"окружающая среда","uz":"atrof-muhit"},
        {"de":"der Müll","ru":"мусор","uz":"chiqindi"},
        {"de":"recyceln","ru":"перерабатывать","uz":"qayta ishlash"},
        {"de":"der Klimawandel","ru":"изменение климата","uz":"iqlim o'zgarishi"},
        {"de":"erneuerbare Energien","ru":"возобновляемые источники","uz":"qayta tiklanadigan energiya"},
        {"de":"schützen","ru":"защищать","uz":"himoya qilmoq"},
        {"de":"verschmutzen","ru":"загрязнять","uz":"ifloslantirmoq"},
        {"de":"der Wald","ru":"лес","uz":"o'rmon"},
        {"de":"das Meer","ru":"море","uz":"dengiz"},
        {"de":"das Tier","ru":"животное","uz":"hayvon"},
        {"de":"sparen","ru":"экономить","uz":"tejash"},
      ],
      "dialogue":[
        ("A","Was machst du für die Umwelt?"),
        ("B","Ich recycle Müll und fahre mit dem Fahrrad."),
        ("A","Hier wird auch Strom aus Solarenergie produziert."),
        ("B","Das ist gut. Wasser sollte auch gespart werden."),
        ("A","Stimmt. Und Plastik wird leider noch zu viel benutzt."),
        ("B","Das muss geändert werden!"),
      ],
      "exercises":[
        {"type":"choice","q":"Müll ___ getrennt gesammelt. (пассив, Präsens)",
         "opts":["ist","hat","wird","soll"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'schützen'?",
         "opts":["загрязнять","защищать","экономить","перерабатывать"],"ans":1},
        {"type":"fill","q":"Das Wasser ___ gespart werden. (должна — модальное в пассиве)",
         "opts":["wird","soll","ist","hat"],"ans":1},
      ]
    },
    { "id":6, "title_de":"Kulturleben und Ausgehen", "title_ru":"Культурная жизнь", "title_uz":"Madaniy hayot",
      "grammar_topic":"Zweiteilige Konnektoren | Двойные союзы",
      "grammar_ru":
        "🔷 Двойные союзы:\n"
        "• *sowohl … als auch* = как … так и\n"
        "• *entweder … oder* = либо … либо\n"
        "• *weder … noch* = ни … ни\n"
        "• *nicht nur … sondern auch* = не только … но и\n\n"
        "• Er spricht *sowohl* Deutsch *als auch* Englisch.\n"
        "• *Entweder* ins Kino *oder* ins Theater.",
      "grammar_uz":
        "🔷 Juft bog'lovchilar:\n"
        "• *sowohl … als auch* = ham … ham\n"
        "• *entweder … oder* = yoki … yoki\n"
        "• *weder … noch* = na … na\n"
        "• *nicht nur … sondern auch* = nafaqat … balki\n\n"
        "• Er spricht *sowohl* Deutsch *als auch* Englisch.\n"
        "• *Entweder* ins Kino *oder* ins Theater.",
      "vocab":[
        {"de":"das Museum","ru":"музей","uz":"muzey"},
        {"de":"die Ausstellung","ru":"выставка","uz":"ko'rgazma"},
        {"de":"das Konzert","ru":"концерт","uz":"konsert"},
        {"de":"die Oper","ru":"опера","uz":"opera"},
        {"de":"das Festival","ru":"фестиваль","uz":"festival"},
        {"de":"die Eintrittskarte","ru":"входной билет","uz":"kirish chiptasi"},
        {"de":"die Vorstellung","ru":"представление","uz":"tamosha"},
        {"de":"der Künstler","ru":"художник / артист","uz":"rassom / artist"},
        {"de":"beeindruckend","ru":"впечатляющий","uz":"ta'sirchan"},
        {"de":"langweilig / spannend","ru":"скучный / захватывающий","uz":"zerikarli / qiziqarli"},
        {"de":"empfehlen","ru":"рекомендовать","uz":"tavsiya qilmoq"},
        {"de":"reservieren","ru":"резервировать","uz":"band qilmoq"},
      ],
      "dialogue":[
        ("A","Was hast du am Wochenende gemacht?"),
        ("B","Ich war sowohl im Museum als auch im Konzert."),
        ("A","War das Konzert gut?"),
        ("B","Ja! Die Musik war nicht nur schön, sondern auch sehr beeindruckend."),
        ("A","Ich gehe entweder ins Theater oder in die Oper. Was empfiehlst du?"),
        ("B","Die Oper! Das Orchester ist weder langweilig noch zu laut."),
      ],
      "exercises":[
        {"type":"choice","q":"Er spricht ___ Deutsch ___ Englisch. (как ... так и)",
         "opts":["entweder/oder","sowohl/als auch","weder/noch","nicht nur/sondern"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'beeindruckend'?",
         "opts":["скучный","впечатляющий","дорогой","шумный"],"ans":1},
        {"type":"fill","q":"___ ins Kino ___ ins Theater. (либо ... либо)",
         "opts":["Sowohl/als auch","Entweder/oder","Weder/noch","Nicht nur/sondern auch"],"ans":1},
      ]
    },
    { "id":7, "title_de":"Arbeitswelt und Karriere", "title_ru":"Карьера и работа", "title_uz":"Karyera va ish",
      "grammar_topic":"Infinitivkonstruktionen (um … zu) | Инфинитивные конструкции",
      "grammar_ru":
        "🔷 *um … zu* + Infinitiv = чтобы (цель)\n"
        "🔷 *ohne … zu* = без того, чтобы\n"
        "🔷 *anstatt … zu* = вместо того, чтобы\n\n"
        "• Ich lerne Deutsch, *um* in Deutschland *zu arbeiten*.\n"
        "• Er schläft, *ohne* das Licht *auszumachen*.\n"
        "• Sie lernt, *anstatt* fernzusehen.",
      "grammar_uz":
        "🔷 *um … zu* + Infinitiv = ... uchun (maqsad)\n"
        "🔷 *ohne … zu* = ... qilmasdan\n"
        "🔷 *anstatt … zu* = ... o'rniga\n\n"
        "• Ich lerne Deutsch, *um* in Deutschland *zu arbeiten*.\n"
        "• Er schläft, *ohne* das Licht *auszumachen*.\n"
        "• Sie lernt, *anstatt* fernzusehen.",
      "vocab":[
        {"de":"die Karriere","ru":"карьера","uz":"karyera"},
        {"de":"die Bewerbung","ru":"заявка на работу","uz":"ish uchun ariza"},
        {"de":"das Vorstellungsgespräch","ru":"собеседование","uz":"suhbat"},
        {"de":"der Lebenslauf","ru":"резюме","uz":"rezyume"},
        {"de":"die Qualifikation","ru":"квалификация","uz":"malaka"},
        {"de":"die Fähigkeit","ru":"навык / способность","uz":"ko'nikma"},
        {"de":"die Fortbildung","ru":"повышение квалификации","uz":"malaka oshirish"},
        {"de":"kündigen","ru":"увольняться","uz":"ishdan bo'shatmoq"},
        {"de":"einstellen","ru":"принимать на работу","uz":"ishga olmoq"},
        {"de":"das Team","ru":"команда","uz":"jamoa"},
        {"de":"selbstständig","ru":"самостоятельный","uz":"mustaqil"},
        {"de":"die Überstunde","ru":"сверхурочная работа","uz":"qo'shimcha ish vaqti"},
      ],
      "dialogue":[
        ("A","Warum haben Sie sich bei uns beworben?"),
        ("B","Um meine Karriere weiterzuentwickeln und neue Fähigkeiten zu lernen."),
        ("A","Was sind Ihre Stärken?"),
        ("B","Ich arbeite selbstständig und bin teamfähig, anstatt immer Hilfe zu brauchen."),
        ("A","Haben Sie Erfahrung in diesem Bereich?"),
        ("B","Ja, ich habe 3 Jahre gearbeitet, um Qualifikationen zu sammeln."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich lerne Deutsch, ___ in Deutschland zu arbeiten. (чтобы)",
         "opts":["ohne","anstatt","um","für"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'das Vorstellungsgespräch'?",
         "opts":["резюме","собеседование","квалификация","навык"],"ans":1},
        {"type":"fill","q":"Sie lernt, ___ fernzusehen. (вместо того чтобы)",
         "opts":["um","ohne","anstatt","damit"],"ans":2},
      ]
    },
    { "id":8, "title_de":"Reisen und Tourismus", "title_ru":"Туризм", "title_uz":"Turizm",
      "grammar_topic":"Nebensätze mit obwohl, weil, wenn, dass | Придаточные предложения",
      "grammar_ru":
        "🔷 Союзы с изменением порядка слов (глагол в КОНЕЦ):\n"
        "• *weil* = потому что: Ich lerne, *weil* es wichtig *ist*.\n"
        "• *obwohl* = хотя: Er kommt, *obwohl* er müde *ist*.\n"
        "• *wenn* = когда/если: *Wenn* ich Zeit *habe*, reise ich.\n"
        "• *dass* = что: Ich denke, *dass* das gut *ist*.",
      "grammar_uz":
        "🔷 So'z tartibi o'zgaradigan bog'lovchilar (fe'l OXIRGA ketadi):\n"
        "• *weil* = chunki: Ich lerne, *weil* es wichtig *ist*.\n"
        "• *obwohl* = garchi: Er kommt, *obwohl* er müde *ist*.\n"
        "• *wenn* = agar/qachon: *Wenn* ich Zeit *habe*, reise ich.\n"
        "• *dass* = ... deb: Ich denke, *dass* das gut *ist*.",
      "vocab":[
        {"de":"der Tourist","ru":"турист","uz":"turist"},
        {"de":"die Sehenswürdigkeit","ru":"достопримечательность","uz":"diqqatga sazovor joy"},
        {"de":"das Hotel","ru":"отель","uz":"mehmonxona"},
        {"de":"die Unterkunft","ru":"жильё / ночлег","uz":"turar joy"},
        {"de":"einchecken","ru":"заселяться","uz":"ro'yxatdan o'tmoq"},
        {"de":"auschecken","ru":"выезжать","uz":"chiqib ketmoq"},
        {"de":"die Stadtführung","ru":"экскурсия","uz":"shahar sayohati"},
        {"de":"der Reiseführer","ru":"путеводитель / гид","uz":"qo'llanma / gid"},
        {"de":"das Souvenir","ru":"сувенир","uz":"sovenir"},
        {"de":"besichtigen","ru":"осматривать достопримечательности","uz":"ko'zdan kechirmoq"},
        {"de":"der Strand","ru":"пляж","uz":"qirg'oq"},
        {"de":"die Berge","ru":"горы","uz":"tog'lar"},
      ],
      "dialogue":[
        ("A","Warum reisen Sie so gern?"),
        ("B","Weil ich neue Kulturen kennenlernen möchte."),
        ("A","Obwohl das Reisen teuer ist?"),
        ("B","Ja! Wenn ich genug spare, kann ich jedes Jahr verreisen."),
        ("A","Denken Sie, dass Tourismus wichtig ist?"),
        ("B","Ja, weil er das Verständnis zwischen Kulturen fördert."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich reise gern, ___ es teuer ist. (хотя)",
         "opts":["weil","wenn","obwohl","dass"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'die Sehenswürdigkeit'?",
         "opts":["отель","пляж","достопримечательность","сувенир"],"ans":2},
        {"type":"fill","q":"Ich denke, ___ das sehr schön ist. (что)",
         "opts":["weil","wenn","obwohl","dass"],"ans":3},
      ]
    },
  ]
}

A2_2 = {
  "title_ru": "Элементарный — часть 2", "title_uz": "Boshlang'ich-o'rta — 2-qism",
  "lessons": [
    { "id":1, "title_de":"Schule und Bildung", "title_ru":"Школа и образование", "title_uz":"Maktab va ta'lim",
      "grammar_topic":"Genitiv | Родительный падеж",
      "grammar_ru":
        "🔷 Genitiv — принадлежность (чей?)\n"
        "m/n: des + Nomen + (e)s, f/Pl: der\n\n"
        "Примеры:\n• das Buch *des* Lehrers — книга учителя\n"
        "• die Tasche *der* Schülerin — сумка ученицы\n"
        "• wegen *des* Wetters — из-за погоды\n\n"
        "Предлоги с Genitiv: wegen, trotz, während, statt",
      "grammar_uz":
        "🔷 Genitiv — tegishlilik (kimning?)\n"
        "m/n: des + Nomen + (e)s, f/Pl: der\n\n"
        "Misollar:\n• das Buch *des* Lehrers — o'qituvchining kitobi\n"
        "• die Tasche *der* Schülerin — o'quvchining sumkasi\n"
        "• wegen *des* Wetters — ob-havo sababli\n\n"
        "Genitiv bilan predloglar: wegen, trotz, während, statt",
      "vocab":[
        {"de":"die Schule","ru":"школа","uz":"maktab"},
        {"de":"das Fach","ru":"предмет","uz":"fan"},
        {"de":"die Note","ru":"оценка","uz":"baho"},
        {"de":"die Prüfung","ru":"экзамен","uz":"imtihon"},
        {"de":"bestehen","ru":"сдать (экзамен)","uz":"topshirmoq"},
        {"de":"durchfallen","ru":"провалить (экзамен)","uz":"yiqilmoq"},
        {"de":"die Hausaufgabe","ru":"домашнее задание","uz":"uy vazifasi"},
        {"de":"das Zeugnis","ru":"свидетельство / аттестат","uz":"guvohnoma"},
        {"de":"die Universität","ru":"университет","uz":"universitet"},
        {"de":"der Unterricht","ru":"урок / занятия","uz":"dars"},
        {"de":"erklären","ru":"объяснять","uz":"tushuntirmoq"},
        {"de":"wiederholen","ru":"повторять","uz":"takrorlash"},
      ],
      "dialogue":[
        ("A","Wie war deine Prüfung?"),
        ("B","Ich habe sie bestanden, trotz des Stresses."),
        ("A","Was war das schwierigste Fach?"),
        ("B","Das Fach des Lehrers Schmidt — Mathematik."),
        ("A","Wann bekommst du dein Zeugnis?"),
        ("B","Ende des Monats. Hoffentlich sind die Noten gut!"),
      ],
      "exercises":[
        {"type":"choice","q":"Das Buch ___ Lehrers ist interessant. (Genitiv)",
         "opts":["der","dem","des","die"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'durchfallen'?",
         "opts":["сдать","провалить","повторить","объяснить"],"ans":1},
        {"type":"fill","q":"___ des Wetters bleiben wir zu Hause. (из-за)",
         "opts":["Während","Statt","Trotz","Wegen"],"ans":3},
      ]
    },
    { "id":2, "title_de":"Technik im Alltag", "title_ru":"Техника в быту", "title_uz":"Kundalik texnika",
      "grammar_topic":"Partizip I als Adjektiv | Причастие I как прилагательное",
      "grammar_ru":
        "🔷 Partizip I = Infinitiv + -d (текущее действие)\n"
        "Как прилагательное принимает окончания!\n\n"
        "• das *fließende* Wasser — текущая вода\n"
        "• ein *lächelndes* Kind — улыбающийся ребёнок\n"
        "• die *wachsende* Technologie — растущие технологии\n\n"
        "Partizip II как прил.: das *reparierte* Auto — отремонтированная машина",
      "grammar_uz":
        "🔷 Partizip I = Infinitiv + -d (joriy harakat)\n"
        "Sifat sifatida qo'shimchalar oladi!\n\n"
        "• das *fließende* Wasser — oqayotgan suv\n"
        "• ein *lächelndes* Kind — kulib turgan bola\n"
        "• die *wachsende* Technologie — o'sayotgan texnologiya",
      "vocab":[
        {"de":"das Gerät","ru":"устройство / прибор","uz":"qurilma"},
        {"de":"der Computer","ru":"компьютер","uz":"kompyuter"},
        {"de":"das Tablet","ru":"планшет","uz":"planshet"},
        {"de":"die Waschmaschine","ru":"стиральная машина","uz":"kir yuvish mashinasi"},
        {"de":"der Kühlschrank","ru":"холодильник","uz":"muzlatgich"},
        {"de":"kaputt / defekt","ru":"сломан / неисправен","uz":"buzilgan"},
        {"de":"reparieren","ru":"ремонтировать","uz":"ta'mirlash"},
        {"de":"aufladen","ru":"заряжать","uz":"zaryadlash"},
        {"de":"der Akku","ru":"аккумулятор","uz":"akkumlyator"},
        {"de":"drahtlos","ru":"беспроводной","uz":"simsiz"},
        {"de":"die Software","ru":"программное обеспечение","uz":"dasturiy ta'minot"},
        {"de":"aktualisieren","ru":"обновлять","uz":"yangilash"},
      ],
      "dialogue":[
        ("A","Mein Laptop funktioniert nicht mehr."),
        ("B","Was ist passiert?"),
        ("A","Der Akku ist kaputt. Ich muss ihn aufladen, aber es geht nicht."),
        ("B","Hast du das Ladekabel überprüft?"),
        ("A","Ja. Das Gerät startet, aber die laufende Software macht Probleme."),
        ("B","Versuch mal, das System zu aktualisieren."),
      ],
      "exercises":[
        {"type":"choice","q":"Das ___ Programm macht Probleme. (текущая, Partizip I von 'laufen')",
         "opts":["gelaufene","laufende","laufende","laufen"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'kaputt'?",
         "opts":["новый","дорогой","сломан","маленький"],"ans":2},
        {"type":"fill","q":"Ich muss das Handy ___. (зарядить)",
         "opts":["aktualisieren","aufladen","reparieren","kaufen"],"ans":1},
      ]
    },
    { "id":3, "title_de":"Dienstleistungen und Behörden", "title_ru":"Услуги и учреждения", "title_uz":"Xizmatlar va muassasalar",
      "grammar_topic":"Indirekte Frage | Косвенный вопрос",
      "grammar_ru":
        "🔷 Косвенные вопросы — глагол в конец\n"
        "С вопросительным словом: Ich weiß nicht, *wo* er *ist*.\n"
        "Без воп. слова: Ich frage, *ob* er kommt.\n\n"
        "• Können Sie mir sagen, *wann* der Zug *abfährt*?\n"
        "• Ich weiß nicht, *ob* die Bank heute *offen ist*.\n"
        "• Weißt du, *wie viel* das *kostet*?",
      "grammar_uz":
        "🔷 Bilvosita savollar — fe'l oxirga ketadi\n"
        "Savol so'zi bilan: Ich weiß nicht, *wo* er *ist*.\n"
        "Savol so'zisiz: Ich frage, *ob* er kommt.\n\n"
        "• Können Sie mir sagen, *wann* der Zug *abfährt*?\n"
        "• Ich weiß nicht, *ob* die Bank heute *offen ist*.\n"
        "• Weißt du, *wie viel* das *kostet*?",
      "vocab":[
        {"de":"das Amt","ru":"учреждение / ведомство","uz":"muassasa / idora"},
        {"de":"das Formular","ru":"бланк / форма","uz":"blank"},
        {"de":"ausfüllen","ru":"заполнять","uz":"to'ldirmoq"},
        {"de":"unterschreiben","ru":"подписывать","uz":"imzolash"},
        {"de":"der Antrag","ru":"заявление","uz":"ariza"},
        {"de":"die Genehmigung","ru":"разрешение","uz":"ruxsatnoma"},
        {"de":"die Wartezeit","ru":"время ожидания","uz":"kutish vaqti"},
        {"de":"der Termin","ru":"запись / встреча","uz":"yozilish / uchrashuv"},
        {"de":"die Bürgeramt","ru":"паспортный стол","uz":"fuqarolar xizmati"},
        {"de":"der Ausweis","ru":"удостоверение","uz":"shaxsiy guvohnoma"},
        {"de":"beantragen","ru":"подавать заявление","uz":"ariza topshirmoq"},
        {"de":"zuständig","ru":"ответственный / компетентный","uz":"mas'ul"},
      ],
      "dialogue":[
        ("A","Entschuldigung, können Sie mir sagen, wo ich einen Termin beantragen kann?"),
        ("B","Ich weiß nicht genau, ob das hier möglich ist."),
        ("A","Wissen Sie, wann das Amt öffnet?"),
        ("B","Ich glaube, dass es um 9 Uhr öffnet."),
        ("A","Und wer ist zuständig für Ausweise?"),
        ("B","Das Bürgeramt. Schauen Sie, ob Sie ein Formular ausfüllen müssen."),
      ],
      "exercises":[
        {"type":"choice","q":"Wissen Sie, ___ das Amt öffnet? (когда — косв. вопрос)",
         "opts":["wann es öffnet","wann öffnet es","wann öffnet","öffnet wann"],"ans":0},
        {"type":"choice","q":"Was bedeutet 'ausfüllen'?",
         "opts":["подписывать","заполнять","подавать","ожидать"],"ans":1},
        {"type":"fill","q":"Ich weiß nicht, ___ die Bank offen ist. (открыта ли)",
         "opts":["ob","dass","weil","wenn"],"ans":0},
      ]
    },
    { "id":4, "title_de":"Sport und Fitness", "title_ru":"Спорт и фитнес", "title_uz":"Sport va fitnes",
      "grammar_topic":"Reflexive Verben | Возвратные глаголы",
      "grammar_ru":
        "🔷 Возвратные глаголы = sich + Verb\n"
        "sich freuen, sich waschen, sich erinnern, sich fühlen\n\n"
        "Склонение: ich mich, du dich, er/sie sich, wir uns, ihr euch, sie sich\n\n"
        "• Ich *freue mich* auf das Spiel. — Я рад игре.\n"
        "• Er *wäscht sich*. — Он моется.\n"
        "• Wir *erinnern uns* daran. — Мы помним об этом.",
      "grammar_uz":
        "🔷 O'z-o'ziga qaytuvchi fe'llar = sich + Verb\n"
        "sich freuen, sich waschen, sich erinnern, sich fühlen\n\n"
        "Tuslanish: ich mich, du dich, er/sie sich, wir uns, ihr euch, sie sich\n\n"
        "• Ich *freue mich* auf das Spiel. — Men o'yinni kutib turaman.\n"
        "• Er *wäscht sich*. — U yuvindi.\n"
        "• Wir *erinnern uns* daran. — Biz buni eslaymiz.",
      "vocab":[
        {"de":"sich fit halten","ru":"быть в форме","uz":"shaklda bo'lmoq"},
        {"de":"trainieren","ru":"тренироваться","uz":"mashq qilmoq"},
        {"de":"das Fitnessstudio","ru":"фитнес-клуб","uz":"fitnes-klub"},
        {"de":"der Muskel","ru":"мышца","uz":"mushak"},
        {"de":"dehnen","ru":"растягиваться","uz":"cho'zmoq"},
        {"de":"die Ausdauer","ru":"выносливость","uz":"chidamlilik"},
        {"de":"die Kraft","ru":"сила","uz":"kuch"},
        {"de":"der Wettkampf","ru":"соревнование","uz":"musobaqa"},
        {"de":"gewinnen","ru":"выигрывать","uz":"yutmoq"},
        {"de":"verlieren","ru":"проигрывать","uz":"yutqazmoq"},
        {"de":"das Ergebnis","ru":"результат","uz":"natija"},
        {"de":"sich erholen","ru":"восстанавливаться","uz":"tiklash"},
      ],
      "dialogue":[
        ("A","Wie hältst du dich fit?"),
        ("B","Ich trainiere dreimal die Woche im Fitnessstudio."),
        ("A","Und was machst du dort?"),
        ("B","Ich freue mich immer auf das Krafttraining. Danach dehne ich mich."),
        ("A","Nimmst du auch an Wettkämpfen teil?"),
        ("B","Ja! Letztes Mal hat sich unser Team gut erholt und gewonnen."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich ___ mich auf das Spiel. (радоваться)",
         "opts":["freue","wasche","erinnere","fühle"],"ans":0},
        {"type":"choice","q":"Was bedeutet 'gewinnen'?",
         "opts":["проигрывать","тренироваться","выигрывать","восстанавливаться"],"ans":2},
        {"type":"fill","q":"Er ___ sich nach dem Training. (восстанавливается)",
         "opts":["erholt","wäscht","freut","erinnert"],"ans":0},
      ]
    },
    { "id":5, "title_de":"Familie und Generationen", "title_ru":"Семья и поколения", "title_uz":"Oila va avlodlar",
      "grammar_topic":"Plusquamperfekt | Давнопрошедшее время",
      "grammar_ru":
        "🔷 Plusquamperfekt — действие ДО другого прошлого действия\n"
        "hatte/war + Partizip II\n\n"
        "• Nachdem ich gegessen *hatte*, ging ich spazieren.\n"
        "  (Сначала поел, потом пошёл гулять)\n"
        "• Als er ankam, *war* ich schon *gegangen*.\n"
        "  (Когда он пришёл, я уже ушёл)\n\n"
        "Ключевые слова: nachdem, als, bevor",
      "grammar_uz":
        "🔷 Plusquamperfekt — boshqa o'tgan vaqtdan OLDINGI harakat\n"
        "hatte/war + Partizip II\n\n"
        "• Nachdem ich gegessen *hatte*, ging ich spazieren.\n"
        "  (Avval yedim, keyin sayrga chiqdim)\n"
        "• Als er ankam, *war* ich schon *gegangen*.\n"
        "  (U kelganida, men ketib bo'lgandim)\n\n"
        "Kalit so'zlar: nachdem, als, bevor",
      "vocab":[
        {"de":"die Generation","ru":"поколение","uz":"avlod"},
        {"de":"der Großvater","ru":"дедушка","uz":"bobo"},
        {"de":"die Großmutter","ru":"бабушка","uz":"buvi"},
        {"de":"erzählen","ru":"рассказывать","uz":"aytib bermoq"},
        {"de":"früher","ru":"раньше / в прошлом","uz":"avval / o'tmishda"},
        {"de":"sich verändern","ru":"меняться","uz":"o'zgarmoq"},
        {"de":"die Tradition","ru":"традиция","uz":"an'ana"},
        {"de":"der Wert","ru":"ценность","uz":"qadriyat"},
        {"de":"respektieren","ru":"уважать","uz":"hurmat qilmoq"},
        {"de":"unterstützen","ru":"поддерживать","uz":"qo'llab-quvvatlash"},
        {"de":"die Kindheit","ru":"детство","uz":"bolalik"},
        {"de":"die Erinnerung","ru":"воспоминание","uz":"xotira"},
      ],
      "dialogue":[
        ("A","Was hat dein Großvater erzählt?"),
        ("B","Nachdem er die Schule abgeschlossen hatte, arbeitete er auf dem Feld."),
        ("A","Das war eine andere Zeit!"),
        ("B","Ja. Als ich Kind war, hatte sich vieles schon verändert."),
        ("A","Pflegst du noch Traditionen?"),
        ("B","Ja, wir respektieren die Werte, die unsere Familie uns mitgegeben hatte."),
      ],
      "exercises":[
        {"type":"choice","q":"Nachdem er gegessen ___, ging er aus. (Plusquamperfekt)",
         "opts":["hat","ist","hatte","war"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'die Erinnerung'?",
         "opts":["традиция","ценность","воспоминание","детство"],"ans":2},
        {"type":"fill","q":"Als sie ankam, ___ ich schon gegangen. (уже ушёл, sein-Verb)",
         "opts":["hatte","war","habe","bin"],"ans":1},
      ]
    },
    { "id":6, "title_de":"Essen gehen / Restaurant", "title_ru":"В ресторане", "title_uz":"Restoranda",
      "grammar_topic":"Modalpartikeln: doch, mal, eigentlich, ja | Модальные частицы",
      "grammar_ru":
        "🔷 Модальные частицы придают оттенок:\n"
        "• *doch* = всё же, ведь: Das ist *doch* gut!\n"
        "• *mal* = ну-ка, хоть раз: Probier *mal*!\n"
        "• *ja* = ведь (уже известно): Du weißt *ja*, dass...\n"
        "• *eigentlich* = по сути, вообще-то: Ich bin *eigentlich* satt.",
      "grammar_uz":
        "🔷 Modal zarrachalar mazmun nozikligi beradi:\n"
        "• *doch* = baribir: Das ist *doch* gut!\n"
        "• *mal* = bir ko'r: Probier *mal*!\n"
        "• *ja* = axir (ma'lum narsa): Du weißt *ja*, dass...\n"
        "• *eigentlich* = aslida: Ich bin *eigentlich* satt.",
      "vocab":[
        {"de":"die Speisekarte","ru":"меню","uz":"menyu"},
        {"de":"die Vorspeise","ru":"закуска","uz":"salatlar"},
        {"de":"das Hauptgericht","ru":"основное блюдо","uz":"asosiy taom"},
        {"de":"die Nachspeise","ru":"десерт","uz":"desert"},
        {"de":"bestellen","ru":"заказывать","uz":"buyurtma bermoq"},
        {"de":"empfehlen","ru":"рекомендовать","uz":"tavsiya etmoq"},
        {"de":"die Rechnung","ru":"счёт","uz":"hisob"},
        {"de":"das Trinkgeld","ru":"чаевые","uz":"qo'shimcha to'lov"},
        {"de":"vegetarisch","ru":"вегетарианский","uz":"vegetarian"},
        {"de":"allergen","ru":"аллерген","uz":"allergen"},
        {"de":"zum Mitnehmen","ru":"на вынос","uz":"olib ketish uchun"},
        {"de":"der Kellner","ru":"официант","uz":"ofitsiant"},
      ],
      "dialogue":[
        ("A","Haben Sie mal einen Tisch für zwei?"),
        ("B","Ja, natürlich. Hier bitte."),
        ("A","Was empfehlen Sie denn heute?"),
        ("B","Das Tagesgericht ist eigentlich sehr gut — Fisch mit Gemüse."),
        ("A","Ich bin ja eigentlich Vegetarier..."),
        ("B","Dann empfehle ich doch die Pasta mit Tomaten!"),
        ("A","Prima! Und die Rechnung bitte am Ende."),
      ],
      "exercises":[
        {"type":"choice","q":"Probier ___ den Kuchen! (ну-ка, частица)",
         "opts":["ja","eigentlich","mal","doch"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'die Rechnung'?",
         "opts":["меню","чаевые","счёт","заказ"],"ans":2},
        {"type":"fill","q":"Das ist ___ sehr lecker! (ведь, уверенность)",
         "opts":["mal","ja","eigentlich","nur"],"ans":1},
      ]
    },
    { "id":7, "title_de":"Politik und Gesellschaft", "title_ru":"Политика и общество", "title_uz":"Siyosat va jamiyat",
      "grammar_topic":"Zweiteilige Konnektoren + Passiv Präteritum | Комбинация",
      "grammar_ru":
        "🔷 Пассив Präteritum: wurde + Partizip II\n"
        "• Das Gesetz *wurde* verabschiedet. — Закон был принят.\n"
        "• Viele Menschen *wurden* befragt. — Много людей было опрошено.\n\n"
        "🔷 Двойные союзы (повторение):\n"
        "• *Je mehr* man lernt, *desto besser* wird man.\n"
        "  (Чем больше учишь, тем лучше становишься)",
      "grammar_uz":
        "🔷 Passiv Präteritum: wurde + Partizip II\n"
        "• Das Gesetz *wurde* verabschiedet. — Qonun qabul qilindi.\n"
        "• Viele Menschen *wurden* befragt. — Ko'p odamlar so'roq qilindi.\n\n"
        "🔷 Juft bog'lovchilar (takrorlash):\n"
        "• *Je mehr* man lernt, *desto besser* wird man.",
      "vocab":[
        {"de":"die Demokratie","ru":"демократия","uz":"demokratiya"},
        {"de":"die Wahl","ru":"выборы","uz":"saylov"},
        {"de":"wählen","ru":"выбирать / голосовать","uz":"saylamoq"},
        {"de":"das Gesetz","ru":"закон","uz":"qonun"},
        {"de":"die Regierung","ru":"правительство","uz":"hukumat"},
        {"de":"die Partei","ru":"партия","uz":"partiya"},
        {"de":"die Meinung","ru":"мнение","uz":"fikr"},
        {"de":"diskutieren","ru":"обсуждать","uz":"muhokama qilmoq"},
        {"de":"die Freiheit","ru":"свобода","uz":"erkinlik"},
        {"de":"die Gleichheit","ru":"равенство","uz":"tenglik"},
        {"de":"die Gesellschaft","ru":"общество","uz":"jamiyat"},
        {"de":"verantwortlich","ru":"ответственный","uz":"mas'ul"},
      ],
      "dialogue":[
        ("A","Was denkst du über die letzte Wahl?"),
        ("B","Viele Menschen wurden befragt, und es gab viele verschiedene Meinungen."),
        ("A","Wurde ein neues Gesetz verabschiedet?"),
        ("B","Ja, je mehr diskutiert wurde, desto schneller kam die Einigung."),
        ("A","Ist Demokratie wichtig für die Gesellschaft?"),
        ("B","Ja, denn Freiheit und Gleichheit sind grundlegende Werte."),
      ],
      "exercises":[
        {"type":"choice","q":"Das Gesetz ___ letztes Jahr verabschiedet. (Passiv Prät.)",
         "opts":["wird","wurde","ist","war"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'die Freiheit'?",
         "opts":["равенство","общество","свобода","партия"],"ans":2},
        {"type":"fill","q":"Je mehr man lernt, ___ besser wird man. (тем)",
         "opts":["so","je","desto","aber"],"ans":2},
      ]
    },
    { "id":8, "title_de":"Feste und Traditionen (weltweit)", "title_ru":"Праздники мира", "title_uz":"Dunyo bayramlari",
      "grammar_topic":"Partizip II / I als erweitertes Attribut | Распространённые причастные определения",
      "grammar_ru":
        "🔷 Причастие расширяется определением (книжный стиль):\n"
        "Причастие + дополнения стоят ПЕРЕД существительным\n\n"
        "• das *in vielen Ländern gefeierte* Fest\n"
        "  (праздник, отмечаемый во многих странах)\n"
        "• die *von Millionen besuchte* Ausstellung\n"
        "  (выставка, посещённая миллионами)\n\n"
        "В разговорной речи лучше использовать Relativsatz!",
      "grammar_uz":
        "🔷 Kengaytirilgan sifat (kitobiy uslub):\n"
        "Sifatdosh + qo'shimchalar otning OLDIGA qo'yiladi\n\n"
        "• das *in vielen Ländern gefeierte* Fest\n"
        "  (ko'p mamlakatlarda nishonlanadigan bayram)\n"
        "• die *von Millionen besuchte* Ausstellung\n"
        "  (millionlar tomonidan ko'rilgan ko'rgazma)",
      "vocab":[
        {"de":"das Neujahrsfest","ru":"Новый год","uz":"Yangi yil"},
        {"de":"das Erntedankfest","ru":"праздник урожая","uz":"hosil bayrami"},
        {"de":"der Karneval","ru":"карнавал","uz":"karnaval"},
        {"de":"weltweit","ru":"во всём мире","uz":"butun dunyoda"},
        {"de":"die Tradition","ru":"традиция","uz":"an'ana"},
        {"de":"der Brauch","ru":"обычай","uz":"odat"},
        {"de":"feiern","ru":"праздновать","uz":"nishonlamoq"},
        {"de":"verkleiden (sich)","ru":"наряжаться","uz":"kiyinmoq (niqob)"},
        {"de":"der Umzug","ru":"шествие / парад","uz":"yurish"},
        {"de":"das Feuerwerk","ru":"фейерверк","uz":"otashin"},
        {"de":"der Brauch","ru":"обычай","uz":"odat"},
        {"de":"interkulturell","ru":"межкультурный","uz":"madaniyatlararo"},
      ],
      "dialogue":[
        ("A","Welches Fest findest du am interessantesten?"),
        ("B","Das in vielen Ländern gefeierte Neujahrsfest."),
        ("A","Wie wird es bei euch gefeiert?"),
        ("B","Mit Feuerwerk, Musik und Essen. Es ist ein von der ganzen Familie geliebtes Fest."),
        ("A","Bei uns gibt es auch den Karneval!"),
        ("B","Das ist ein wirklich bunt gestaltetes Fest mit Umzügen und Kostümen."),
      ],
      "exercises":[
        {"type":"choice","q":"Das ___ Fest hat viele Traditionen. (праздник, отмечаемый, Part. II gefeiert)",
         "opts":["feiernde","gefeiernde","gefeierte","feierende"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'das Feuerwerk'?",
         "opts":["карнавал","шествие","фейерверк","традиция"],"ans":2},
        {"type":"fill","q":"Wir feiern ___ mit Musik und Tanz. (во всём мире)",
         "opts":["interkulturell","weltweit","traditionell","gemeinsam"],"ans":1},
      ]
    },
  ]
}
