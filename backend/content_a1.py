"""A1.1 + A1.2 content"""

A1_1 = {
  "title_ru": "Начинающий — часть 1", "title_uz": "Boshlang'ich — 1-qism",
  "lessons": [
    { "id":1, "title_de":"Hallo! Kennenlernen", "title_ru":"Знакомство", "title_uz":"Tanishish",
      "grammar_topic":"Verben: sein & heißen | Глагол sein и heißen",
      "grammar_ru":
        "🔷 *sein* (быть): ich bin, du bist, er/sie ist, wir sind, ihr seid, sie/Sie sind\n"
        "🔷 *heißen* (называться): ich heiße, du heißt, er heißt\n\n"
        "Примеры:\n• Ich *bin* Maria. — Я Мария.\n• Wie *heißen* Sie? — Как вас зовут?\n• Er *ist* Student. — Он студент.",
      "grammar_uz":
        "🔷 *sein* (bo'lmoq): ich bin, du bist, er/sie ist, wir sind, ihr seid, sie/Sie sind\n"
        "🔷 *heißen* (atalmoq): ich heiße, du heißt, er heißt\n\n"
        "Misollar:\n• Ich *bin* Maria. — Men Mariyaman.\n• Wie *heißen* Sie? — Ismingiz nima?\n• Er *ist* Student. — U talaba.",
      "vocab":[
        {"de":"Hallo","ru":"Привет","uz":"Salom"},
        {"de":"Guten Morgen","ru":"Доброе утро","uz":"Xayrli tong"},
        {"de":"Guten Tag","ru":"Добрый день","uz":"Xayrli kun"},
        {"de":"Guten Abend","ru":"Добрый вечер","uz":"Xayrli kech"},
        {"de":"Auf Wiedersehen","ru":"До свидания","uz":"Xayr"},
        {"de":"Tschüss","ru":"Пока","uz":"Xayr (norasmiy)"},
        {"de":"Wie heißen Sie?","ru":"Как вас зовут?","uz":"Ismingiz nima?"},
        {"de":"Ich heiße...","ru":"Меня зовут...","uz":"Mening ismim..."},
        {"de":"Woher kommen Sie?","ru":"Откуда вы?","uz":"Qayerdansiz?"},
        {"de":"Ich komme aus...","ru":"Я из...","uz":"Men ... danman"},
        {"de":"Wie geht es Ihnen?","ru":"Как у вас дела?","uz":"Ishlaringiz qanday?"},
        {"de":"Danke, gut.","ru":"Спасибо, хорошо.","uz":"Rahmat, yaxshi."},
      ],
      "dialogue":[
        ("A","Guten Tag! Ich heiße Anna. Wie heißen Sie?"),
        ("B","Guten Tag! Ich heiße Karim. Woher kommen Sie?"),
        ("A","Ich komme aus Deutschland. Und Sie?"),
        ("B","Ich komme aus Usbekistan."),
        ("A","Schön, Sie kennenzulernen!"),
        ("B","Sehr angenehm!"),
      ],
      "exercises":[
        {"type":"choice","q":"Was bedeutet 'Ich heiße Anna'?",
         "opts":["Я из Анны","Меня зовут Анна","Я Анна хочу","Она зовут Анна"],"ans":1},
        {"type":"choice","q":"Wie sagt man 'Добрый день' auf Deutsch?",
         "opts":["Guten Morgen","Guten Abend","Guten Tag","Auf Wiedersehen"],"ans":2},
        {"type":"fill","q":"Ergänzen Sie: Ich ___ aus Usbekistan. (kommen)",
         "opts":["komme","kommen","kommst","kommt"],"ans":0},
      ]
    },
    { "id":2, "title_de":"Meine Familie", "title_ru":"Моя семья", "title_uz":"Mening oilam",
      "grammar_topic":"Possessivartikel: mein/meine | Притяжательные артикли",
      "grammar_ru":
        "🔷 *mein/meine* (мой/моя): mein Vater, meine Mutter\n"
        "🔷 Определённый артикль: der → mein, die → meine, das → mein\n\n"
        "Примеры:\n• Das ist *mein* Bruder. — Это мой брат.\n"
        "• Das ist *meine* Schwester. — Это моя сестра.\n"
        "• Wie alt ist *dein* Vater? — Сколько лет твоему отцу?",
      "grammar_uz":
        "🔷 *mein/meine* (mening): mein Vater, meine Mutter\n"
        "🔷 Aniq artikl: der → mein, die → meine, das → mein\n\n"
        "Misollar:\n• Das ist *mein* Bruder. — Bu mening akam.\n"
        "• Das ist *meine* Schwester. — Bu mening singlim.\n"
        "• Wie alt ist *dein* Vater? — Otangiz necha yoshda?",
      "vocab":[
        {"de":"die Familie","ru":"семья","uz":"oila"},
        {"de":"der Vater","ru":"отец","uz":"ota"},
        {"de":"die Mutter","ru":"мать","uz":"ona"},
        {"de":"der Bruder","ru":"брат","uz":"aka/uka"},
        {"de":"die Schwester","ru":"сестра","uz":"opa/singil"},
        {"de":"der Sohn","ru":"сын","uz":"o'g'il"},
        {"de":"die Tochter","ru":"дочь","uz":"qiz"},
        {"de":"die Großmutter","ru":"бабушка","uz":"buvi"},
        {"de":"der Großvater","ru":"дедушка","uz":"bobo"},
        {"de":"der Mann","ru":"муж / мужчина","uz":"er / erkak"},
        {"de":"die Frau","ru":"жена / женщина","uz":"xotin / ayol"},
        {"de":"das Kind","ru":"ребёнок","uz":"bola"},
      ],
      "dialogue":[
        ("A","Hast du Geschwister?"),
        ("B","Ja, ich habe einen Bruder und eine Schwester."),
        ("A","Wie alt ist dein Bruder?"),
        ("B","Er ist 20 Jahre alt. Und meine Schwester ist 15."),
        ("A","Und deine Eltern?"),
        ("B","Mein Vater ist 45 und meine Mutter ist 43."),
      ],
      "exercises":[
        {"type":"choice","q":"Wie sagt man 'моя мать' auf Deutsch?",
         "opts":["mein Mutter","meine Mutter","meinen Mutter","meine Vater"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'das Kind'?",
         "opts":["сестра","ребёнок","брат","семья"],"ans":1},
        {"type":"fill","q":"Ich habe ___ Bruder. (einen/eine/ein)",
         "opts":["eine","ein","einen","meine"],"ans":2},
      ]
    },
    { "id":3, "title_de":"Meine Wohnung", "title_ru":"Моя квартира", "title_uz":"Mening uyim",
      "grammar_topic":"es gibt + Akkusativ | Конструкция 'есть'",
      "grammar_ru":
        "🔷 *es gibt* = есть (существует)\n"
        "🔷 После 'es gibt' используется Akkusativ:\n"
        "   der → einen, die → eine, das → ein\n\n"
        "Примеры:\n• Es gibt *einen* Tisch. — Есть стол.\n"
        "• Es gibt *eine* Küche. — Есть кухня.\n"
        "• Es gibt *kein* Wohnzimmer. — Нет гостиной.",
      "grammar_uz":
        "🔷 *es gibt* = bor (mavjud)\n"
        "🔷 'es gibt' dan keyin Akkusativ ishlatiladi:\n"
        "   der → einen, die → eine, das → ein\n\n"
        "Misollar:\n• Es gibt *einen* Tisch. — Stol bor.\n"
        "• Es gibt *eine* Küche. — Oshxona bor.\n"
        "• Es gibt *kein* Wohnzimmer. — Mehmonxona yo'q.",
      "vocab":[
        {"de":"die Wohnung","ru":"квартира","uz":"kvartira"},
        {"de":"das Zimmer","ru":"комната","uz":"xona"},
        {"de":"das Wohnzimmer","ru":"гостиная","uz":"mehmonxona"},
        {"de":"das Schlafzimmer","ru":"спальня","uz":"yotoqxona"},
        {"de":"die Küche","ru":"кухня","uz":"oshxona"},
        {"de":"das Badezimmer","ru":"ванная","uz":"hammom"},
        {"de":"der Tisch","ru":"стол","uz":"stol"},
        {"de":"der Stuhl","ru":"стул","uz":"stul"},
        {"de":"das Bett","ru":"кровать","uz":"karavot"},
        {"de":"das Fenster","ru":"окно","uz":"deraza"},
        {"de":"die Tür","ru":"дверь","uz":"eshik"},
        {"de":"groß / klein","ru":"большой / маленький","uz":"katta / kichik"},
      ],
      "dialogue":[
        ("A","Wie ist deine Wohnung?"),
        ("B","Sie ist nicht sehr groß. Es gibt ein Schlafzimmer, ein Wohnzimmer und eine Küche."),
        ("A","Hast du ein Badezimmer?"),
        ("B","Ja, natürlich! Und es gibt auch einen Balkon."),
        ("A","Schön! Wie viele Zimmer hat die Wohnung?"),
        ("B","Drei Zimmer plus Küche und Bad."),
      ],
      "exercises":[
        {"type":"choice","q":"Was bedeutet 'das Schlafzimmer'?",
         "opts":["кухня","гостиная","спальня","ванная"],"ans":2},
        {"type":"choice","q":"Es gibt ___ Tisch. (Akkusativ von 'der')",
         "opts":["ein","eine","einen","einem"],"ans":2},
        {"type":"fill","q":"Das Zimmer ist sehr ___. (большой)",
         "opts":["klein","groß","alt","neu"],"ans":1},
      ]
    },
    { "id":4, "title_de":"Essen und Trinken", "title_ru":"Еда и напитки", "title_uz":"Ovqat va ichimliklar",
      "grammar_topic":"Mögen & möchten | Глаголы 'любить' и 'хотеть'",
      "grammar_ru":
        "🔷 *mögen* (нравиться/любить): ich mag, du magst, er mag\n"
        "🔷 *möchten* (хотеть): ich möchte, du möchtest, er möchte\n\n"
        "Примеры:\n• Ich *mag* Kaffee. — Мне нравится кофе.\n"
        "• Ich *möchte* einen Tee, bitte. — Я хочу чай, пожалуйста.\n"
        "• Er *mag* kein Fleisch. — Ему не нравится мясо.",
      "grammar_uz":
        "🔷 *mögen* (yoqmoq): ich mag, du magst, er mag\n"
        "🔷 *möchten* (xohlamoq): ich möchte, du möchtest, er möchte\n\n"
        "Misollar:\n• Ich *mag* Kaffee. — Men qahvani yaxshi ko'raman.\n"
        "• Ich *möchte* einen Tee, bitte. — Bir choy istardim.\n"
        "• Er *mag* kein Fleisch. — Unga go'sht yoqmaydi.",
      "vocab":[
        {"de":"das Brot","ru":"хлеб","uz":"non"},
        {"de":"die Butter","ru":"масло","uz":"sariyog'"},
        {"de":"der Käse","ru":"сыр","uz":"pishloq"},
        {"de":"das Fleisch","ru":"мясо","uz":"go'sht"},
        {"de":"der Fisch","ru":"рыба","uz":"baliq"},
        {"de":"das Gemüse","ru":"овощи","uz":"sabzavotlar"},
        {"de":"das Obst","ru":"фрукты","uz":"mevalar"},
        {"de":"der Kaffee","ru":"кофе","uz":"qahva"},
        {"de":"der Tee","ru":"чай","uz":"choy"},
        {"de":"das Wasser","ru":"вода","uz":"suv"},
        {"de":"der Saft","ru":"сок","uz":"sharbat"},
        {"de":"lecker","ru":"вкусный","uz":"mazali"},
      ],
      "dialogue":[
        ("A","Was möchten Sie trinken?"),
        ("B","Ich möchte einen Kaffee, bitte."),
        ("A","Mit Milch und Zucker?"),
        ("B","Nur mit Milch, danke. Und ich möchte auch ein Stück Kuchen."),
        ("A","Gern! Unser Kuchen ist sehr lecker."),
        ("B","Wunderbar!"),
      ],
      "exercises":[
        {"type":"choice","q":"Ich ___ einen Tee, bitte. (хотеть)",
         "opts":["mag","möchte","habe","bin"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'lecker'?",
         "opts":["дорогой","вкусный","дешёвый","холодный"],"ans":1},
        {"type":"fill","q":"Er mag ___ Fleisch. (не любит — отрицание)",
         "opts":["kein","nicht","keine","nein"],"ans":0},
      ]
    },
    { "id":5, "title_de":"Mein Tag / Alltag", "title_ru":"Мой день", "title_uz":"Mening kunim",
      "grammar_topic":"Trennbare Verben | Отделяемые приставки",
      "grammar_ru":
        "🔷 Некоторые глаголы имеют отделяемые приставки:\n"
        "aufstehen → Ich stehe auf (вставать)\n"
        "aufmachen → Ich mache auf (открывать)\n"
        "fernsehen → Ich sehe fern (смотреть ТВ)\n\n"
        "Приставка уходит в КОНЕЦ предложения!\n"
        "• Ich *stehe* um 7 Uhr *auf*. — Я встаю в 7 часов.",
      "grammar_uz":
        "🔷 Ba'zi fe'llar ajraladigan prefiksga ega:\n"
        "aufstehen → Ich stehe auf (turmoq)\n"
        "aufmachen → Ich mache auf (ochmoq)\n"
        "fernsehen → Ich sehe fern (televizor ko'rmoq)\n\n"
        "Prefiks jumlaning OXIRIGA ketadi!\n"
        "• Ich *stehe* um 7 Uhr *auf*. — Men soat 7da turaman.",
      "vocab":[
        {"de":"aufstehen","ru":"вставать","uz":"turmoq"},
        {"de":"frühstücken","ru":"завтракать","uz":"nonushta qilmoq"},
        {"de":"zur Arbeit gehen","ru":"идти на работу","uz":"ishga bormoq"},
        {"de":"zu Mittag essen","ru":"обедать","uz":"tushlik qilmoq"},
        {"de":"nach Hause kommen","ru":"приходить домой","uz":"uyga kelmoq"},
        {"de":"fernsehen","ru":"смотреть ТВ","uz":"televizor ko'rmoq"},
        {"de":"schlafen gehen","ru":"ложиться спать","uz":"uxlash"},
        {"de":"die Uhrzeit","ru":"время","uz":"vaqt"},
        {"de":"morgens","ru":"утром","uz":"ertalab"},
        {"de":"mittags","ru":"в обед","uz":"tushda"},
        {"de":"abends","ru":"вечером","uz":"kechqurun"},
        {"de":"immer / manchmal","ru":"всегда / иногда","uz":"har doim / ba'zan"},
      ],
      "dialogue":[
        ("A","Wann stehst du auf?"),
        ("B","Ich stehe um halb sieben auf."),
        ("A","Und wann frühstückst du?"),
        ("B","Um sieben Uhr. Dann gehe ich um acht zur Arbeit."),
        ("A","Wann kommst du nach Hause?"),
        ("B","Meistens um 18 Uhr. Dann sehe ich fern oder lese ein Buch."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich stehe um 6 Uhr ___. (aufstehen)",
         "opts":["auf","aus","an","ab"],"ans":0},
        {"type":"choice","q":"Was bedeutet 'frühstücken'?",
         "opts":["обедать","ужинать","завтракать","спать"],"ans":2},
        {"type":"fill","q":"___ sehe ich fern. (вечером)",
         "opts":["Morgens","Mittags","Abends","Nachts"],"ans":2},
      ]
    },
    { "id":6, "title_de":"Einkaufen", "title_ru":"Покупки", "title_uz":"Xarid qilish",
      "grammar_topic":"Akkusativ | Винительный падеж",
      "grammar_ru":
        "🔷 Akkusativ — прямое дополнение (кого? что?)\n"
        "der → den, die → die, das → das\n"
        "ein → einen (m), eine (f), ein (n)\n\n"
        "Примеры:\n• Ich kaufe *den* Apfel. — Я покупаю яблоко.\n"
        "• Ich brauche *einen* Stift. — Мне нужна ручка.\n"
        "• Ich nehme *die* Milch. — Я беру молоко.",
      "grammar_uz":
        "🔷 Akkusativ — to'ldiruvchi (kimni? nini?)\n"
        "der → den, die → die, das → das\n"
        "ein → einen (m), eine (f), ein (n)\n\n"
        "Misollar:\n• Ich kaufe *den* Apfel. — Men olmani sotib olaman.\n"
        "• Ich brauche *einen* Stift. — Menga qalam kerak.\n"
        "• Ich nehme *die* Milch. — Men sutni olaman.",
      "vocab":[
        {"de":"kaufen","ru":"покупать","uz":"sotib olmoq"},
        {"de":"kosten","ru":"стоить","uz":"turmoq (narx)"},
        {"de":"der Preis","ru":"цена","uz":"narx"},
        {"de":"teuer / billig","ru":"дорогой / дешёвый","uz":"qimmat / arzon"},
        {"de":"der Supermarkt","ru":"супермаркет","uz":"supermarket"},
        {"de":"die Kasse","ru":"касса","uz":"kassa"},
        {"de":"bezahlen","ru":"платить","uz":"to'lamoq"},
        {"de":"bar / mit Karte","ru":"наличными / картой","uz":"naqd / karta bilan"},
        {"de":"der Apfel","ru":"яблоко","uz":"olma"},
        {"de":"die Milch","ru":"молоко","uz":"sut"},
        {"de":"das Bier","ru":"пиво","uz":"pivo"},
        {"de":"Wie viel kostet das?","ru":"Сколько это стоит?","uz":"Bu necha pul?"},
      ],
      "dialogue":[
        ("A","Guten Tag! Was darf es sein?"),
        ("B","Ich möchte ein Kilo Äpfel, bitte."),
        ("A","Gern. Noch etwas?"),
        ("B","Ja, eine Flasche Milch und zwei Brote."),
        ("A","Das macht 4 Euro 50."),
        ("B","Kann ich mit Karte bezahlen?"),
        ("A","Natürlich!"),
      ],
      "exercises":[
        {"type":"choice","q":"Wie viel ___ das? (стоить)",
         "opts":["ist","hat","kostet","macht"],"ans":2},
        {"type":"choice","q":"Ich kaufe ___ Apfel. (Akkusativ, der Apfel)",
         "opts":["der","die","den","das"],"ans":2},
        {"type":"fill","q":"Das ist sehr ___. (дорогой)",
         "opts":["billig","neu","teuer","alt"],"ans":2},
      ]
    },
    { "id":7, "title_de":"Freizeit und Hobbys", "title_ru":"Хобби и досуг", "title_uz":"Hobby va bo'sh vaqt",
      "grammar_topic":"Gern / nicht gern | Выражение предпочтений",
      "grammar_ru":
        "🔷 *gern* = с удовольствием (любить что-то делать)\n"
        "🔷 *nicht gern* = не любить\n"
        "🔷 *lieber* = предпочитать (сравнение)\n\n"
        "Примеры:\n• Ich lese *gern*. — Я люблю читать.\n"
        "• Er spielt *nicht gern* Fußball. — Он не любит играть в футбол.\n"
        "• Ich schwimme *lieber*. — Я предпочитаю плавать.",
      "grammar_uz":
        "🔷 *gern* = mamnuniyat bilan (yoqtirmoq)\n"
        "🔷 *nicht gern* = yoqtirmaslik\n"
        "🔷 *lieber* = afzal ko'rmoq\n\n"
        "Misollar:\n• Ich lese *gern*. — Men o'qishni yaxshi ko'raman.\n"
        "• Er spielt *nicht gern* Fußball. — U futbol o'ynashni yoqtirmaydi.\n"
        "• Ich schwimme *lieber*. — Men suzishni afzal ko'raman.",
      "vocab":[
        {"de":"lesen","ru":"читать","uz":"o'qimoq"},
        {"de":"Musik hören","ru":"слушать музыку","uz":"musiqa tinglash"},
        {"de":"Sport treiben","ru":"заниматься спортом","uz":"sport qilish"},
        {"de":"schwimmen","ru":"плавать","uz":"suzmoq"},
        {"de":"reisen","ru":"путешествовать","uz":"sayohat qilish"},
        {"de":"kochen","ru":"готовить","uz":"pishirmoq"},
        {"de":"tanzen","ru":"танцевать","uz":"raqs tushmoq"},
        {"de":"fotografieren","ru":"фотографировать","uz":"suratga olmoq"},
        {"de":"das Kino","ru":"кино","uz":"kino"},
        {"de":"das Theater","ru":"театр","uz":"teatr"},
        {"de":"der Verein","ru":"клуб / кружок","uz":"to'garak / klub"},
        {"de":"das Wochenende","ru":"выходные","uz":"dam olish kuni"},
      ],
      "dialogue":[
        ("A","Was machst du in deiner Freizeit?"),
        ("B","Ich lese gern und höre Musik. Und du?"),
        ("A","Ich treibe Sport. Ich schwimme und spiele Tennis."),
        ("B","Tennis ist toll! Spielst du im Verein?"),
        ("A","Ja, jeden Samstag."),
        ("B","Am Wochenende gehe ich manchmal ins Kino."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich lese ___. (с удовольствием)",
         "opts":["gut","gern","lieber","viel"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'reisen'?",
         "opts":["готовить","плавать","путешествовать","танцевать"],"ans":2},
        {"type":"fill","q":"Er spielt ___ gern Tennis. (не любит)",
         "opts":["kein","nicht","keine","nein"],"ans":1},
      ]
    },
    { "id":8, "title_de":"In der Stadt", "title_ru":"В городе", "title_uz":"Shaharda",
      "grammar_topic":"Präpositionen mit Dativ | Предлоги с дативом",
      "grammar_ru":
        "🔷 Предлоги *in, an, auf, neben, vor, hinter, zwischen, über, unter* + Dativ (местонахождение)\n"
        "der/das → dem, die → der\n\n"
        "Примеры:\n• Die Bank ist *neben dem* Supermarkt. — Банк рядом с супермаркетом.\n"
        "• Das Hotel ist *in der* Stadtmitte. — Отель в центре города.\n"
        "• Ich stehe *vor dem* Bahnhof. — Я стою перед вокзалом.",
      "grammar_uz":
        "🔷 *in, an, auf, neben, vor, hinter, zwischen, über, unter* + Dativ (joylashuv)\n"
        "der/das → dem, die → der\n\n"
        "Misollar:\n• Die Bank ist *neben dem* Supermarkt. — Bank supermarket yonida.\n"
        "• Das Hotel ist *in der* Stadtmitte. — Mehmonxona shahar markazida.\n"
        "• Ich stehe *vor dem* Bahnhof. — Men vokzal oldida turaman.",
      "vocab":[
        {"de":"der Bahnhof","ru":"вокзал","uz":"vokzal"},
        {"de":"die Bank","ru":"банк","uz":"bank"},
        {"de":"das Krankenhaus","ru":"больница","uz":"kasalxona"},
        {"de":"die Apotheke","ru":"аптека","uz":"dorixona"},
        {"de":"das Rathaus","ru":"ратуша","uz":"munitsipalitet"},
        {"de":"die Kirche","ru":"церковь","uz":"cherkov"},
        {"de":"der Park","ru":"парк","uz":"park"},
        {"de":"die Straße","ru":"улица","uz":"ko'cha"},
        {"de":"links / rechts","ru":"налево / направо","uz":"chapga / o'ngga"},
        {"de":"geradeaus","ru":"прямо","uz":"to'g'ri"},
        {"de":"Entschuldigung!","ru":"Извините!","uz":"Kechirasiz!"},
        {"de":"Wie komme ich zu...?","ru":"Как добраться до...?","uz":"...ga qanday boraman?"},
      ],
      "dialogue":[
        ("A","Entschuldigung! Wie komme ich zum Bahnhof?"),
        ("B","Gehen Sie geradeaus, dann links."),
        ("A","Und wie weit ist das?"),
        ("B","Etwa 5 Minuten zu Fuß."),
        ("A","Gibt es auch eine U-Bahn?"),
        ("B","Ja, die Station ist direkt neben dem Rathaus."),
        ("A","Vielen Dank!"),
      ],
      "exercises":[
        {"type":"choice","q":"Die Apotheke ist ___ dem Supermarkt. (рядом с)",
         "opts":["vor","neben","hinter","über"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'geradeaus'?",
         "opts":["направо","налево","прямо","назад"],"ans":2},
        {"type":"fill","q":"Das Hotel ist ___ der Stadtmitte. (в)",
         "opts":["an","auf","in","bei"],"ans":2},
      ]
    },
  ]
}

A1_2 = {
  "title_ru": "Начинающий — часть 2", "title_uz": "Boshlang'ich — 2-qism",
  "lessons": [
    { "id":1, "title_de":"Sprachen & Konnektoren", "title_ru":"Языки и союзы", "title_uz":"Tillar va bog'lovchilar",
      "grammar_topic":"Konnektoren: und, aber, oder, denn | Союзы",
      "grammar_ru":
        "🔷 *und* = и, *aber* = но, *oder* = или, *denn* = потому что\n"
        "🔷 После этих союзов порядок слов НЕ меняется!\n\n"
        "Примеры:\n• Ich lerne Deutsch, *denn* es ist wichtig.\n"
        "• Er spricht Englisch *und* Russisch.\n"
        "• Kommst du mit *oder* bleibst du zu Hause?",
      "grammar_uz":
        "🔷 *und* = va, *aber* = lekin, *oder* = yoki, *denn* = chunki\n"
        "🔷 Bu bog'lovchilardan keyin so'z tartibi o'zgarmaydi!\n\n"
        "Misollar:\n• Ich lerne Deutsch, *denn* es ist wichtig.\n"
        "• Er spricht Englisch *und* Russisch.\n"
        "• Kommst du mit *oder* bleibst du zu Hause?",
      "vocab":[
        {"de":"die Sprache","ru":"язык","uz":"til"},
        {"de":"sprechen","ru":"говорить","uz":"gapirmoq"},
        {"de":"lernen","ru":"учить","uz":"o'rganmoq"},
        {"de":"verstehen","ru":"понимать","uz":"tushunmoq"},
        {"de":"fließend","ru":"свободно","uz":"ravon"},
        {"de":"ein bisschen","ru":"немного","uz":"biroz"},
        {"de":"wichtig","ru":"важный","uz":"muhim"},
        {"de":"schwierig","ru":"сложный","uz":"qiyin"},
        {"de":"einfach","ru":"простой","uz":"oson"},
        {"de":"die Muttersprache","ru":"родной язык","uz":"ona tili"},
        {"de":"übersetzen","ru":"переводить","uz":"tarjima qilmoq"},
        {"de":"der Kurs","ru":"курс","uz":"kurs"},
      ],
      "dialogue":[
        ("A","Welche Sprachen sprechen Sie?"),
        ("B","Ich spreche Usbekisch und Russisch. Und ich lerne Deutsch."),
        ("A","Warum lernen Sie Deutsch?"),
        ("B","Denn ich möchte in Deutschland studieren."),
        ("A","Sprechen Sie auch Englisch?"),
        ("B","Ja, aber nicht sehr gut."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich lerne Deutsch, ___ es wichtig ist. (потому что)",
         "opts":["und","aber","oder","denn"],"ans":3},
        {"type":"choice","q":"Was bedeutet 'fließend'?",
         "opts":["медленно","свободно","немного","плохо"],"ans":1},
        {"type":"fill","q":"Er spricht Englisch ___ Französisch. (и)",
         "opts":["aber","oder","und","denn"],"ans":2},
      ]
    },
    { "id":2, "title_de":"Kleidung und Mode", "title_ru":"Одежда и мода", "title_uz":"Kiyim va moda",
      "grammar_topic":"Adjektivdeklination (Nominativ) | Прилагательные в именительном падеже",
      "grammar_ru":
        "🔷 Прилагательное после неопределённого артикля:\n"
        "m: ein *roter* Pullover, f: eine *blaue* Jacke, n: ein *weißes* Hemd\n\n"
        "🔷 После определённого артикля:\n"
        "m: der *rote* Pullover, f: die *blaue* Jacke",
      "grammar_uz":
        "🔷 Noaniq artikl keyin sifat:\n"
        "m: ein *roter* Pullover, f: eine *blaue* Jacke, n: ein *weißes* Hemd\n\n"
        "🔷 Aniq artikl keyin:\n"
        "m: der *rote* Pullover, f: die *blaue* Jacke",
      "vocab":[
        {"de":"das Hemd","ru":"рубашка","uz":"ko'ylak"},
        {"de":"die Jacke","ru":"куртка","uz":"kurtka"},
        {"de":"der Pullover","ru":"свитер","uz":"sviter"},
        {"de":"die Hose","ru":"брюки","uz":"shim"},
        {"de":"der Rock","ru":"юбка","uz":"yubka"},
        {"de":"das Kleid","ru":"платье","uz":"ko'ylak (ayollar)"},
        {"de":"die Schuhe (Pl.)","ru":"туфли / обувь","uz":"poyafzal"},
        {"de":"rot / blau / grün","ru":"красный / синий / зелёный","uz":"qizil / ko'k / yashil"},
        {"de":"weiß / schwarz","ru":"белый / чёрный","uz":"oq / qora"},
        {"de":"die Größe","ru":"размер","uz":"o'lcham"},
        {"de":"anprobieren","ru":"примерять","uz":"kirib ko'rmoq"},
        {"de":"passen","ru":"подходить","uz":"to'g'ri kelmoq"},
      ],
      "dialogue":[
        ("A","Guten Tag! Kann ich Ihnen helfen?"),
        ("B","Ja, bitte. Ich suche eine Jacke."),
        ("A","Welche Farbe und Größe?"),
        ("B","Blau, Größe 42."),
        ("A","Möchten Sie diese hier anprobieren?"),
        ("B","Ja, gerne. — Sie passt perfekt! Was kostet sie?"),
        ("A","59 Euro."),
      ],
      "exercises":[
        {"type":"choice","q":"Ich suche ein___ Pullover. (m, unbestimmter Artikel Nom.)",
         "opts":["einen","einer","ein","eine"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'anprobieren'?",
         "opts":["покупать","примерять","продавать","искать"],"ans":1},
        {"type":"fill","q":"Die Hose ___ mir gut. (подходит)",
         "opts":["kostet","passt","kauft","sucht"],"ans":1},
      ]
    },
    { "id":3, "title_de":"Gesundheit und Körper", "title_ru":"Здоровье и тело", "title_uz":"Salomatlik va tana",
      "grammar_topic":"Modalverben: müssen, dürfen, sollen | Модальные глаголы",
      "grammar_ru":
        "🔷 *müssen* = должен (необходимость): ich muss, du musst, er muss\n"
        "🔷 *dürfen* = можно (разрешение): ich darf, du darfst\n"
        "🔷 *sollen* = следует (обязанность): ich soll, du sollst\n\n"
        "Инфинитив уходит в КОНЕЦ!\n"
        "• Du *musst* viel Wasser *trinken*. — Тебе нужно пить много воды.",
      "grammar_uz":
        "🔷 *müssen* = kerak: ich muss, du musst, er muss\n"
        "🔷 *dürfen* = mumkin: ich darf, du darfst\n"
        "🔷 *sollen* = lozim: ich soll, du sollst\n\n"
        "Infinitiv oxiriga ketadi!\n"
        "• Du *musst* viel Wasser *trinken*. — Ko'p suv ichishing kerak.",
      "vocab":[
        {"de":"der Kopf","ru":"голова","uz":"bosh"},
        {"de":"der Bauch","ru":"живот","uz":"qorin"},
        {"de":"der Rücken","ru":"спина","uz":"orqa"},
        {"de":"die Hand","ru":"рука (кисть)","uz":"qo'l"},
        {"de":"das Bein","ru":"нога","uz":"oyoq"},
        {"de":"Ich habe Kopfschmerzen.","ru":"У меня болит голова.","uz":"Boshim og'riydi."},
        {"de":"krank / gesund","ru":"больной / здоровый","uz":"kasal / sog'lom"},
        {"de":"der Arzt / die Ärztin","ru":"врач","uz":"shifokor"},
        {"de":"das Medikament","ru":"лекарство","uz":"dori"},
        {"de":"die Tablette","ru":"таблетка","uz":"tabletkа"},
        {"de":"Schmerzen haben","ru":"испытывать боль","uz":"og'riq sezmoq"},
        {"de":"sich erholen","ru":"отдыхать / выздоравливать","uz":"dam olmoq / tuzalmoq"},
      ],
      "dialogue":[
        ("A","Guten Tag, Herr Doktor. Ich fühle mich nicht gut."),
        ("B","Was haben Sie?"),
        ("A","Ich habe Kopfschmerzen und Fieber."),
        ("B","Seit wann?"),
        ("A","Seit zwei Tagen."),
        ("B","Sie müssen viel trinken und sich erholen. Ich verschreibe Ihnen etwas."),
        ("A","Danke, Herr Doktor."),
      ],
      "exercises":[
        {"type":"choice","q":"Du ___ zum Arzt gehen. (должен)",
         "opts":["kannst","magst","musst","darfst"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'krank'?",
         "opts":["здоровый","усталый","больной","грустный"],"ans":2},
        {"type":"fill","q":"Ich habe ___schmerzen. (голова болит)",
         "opts":["Kopf","Bauch","Rücken","Hand"],"ans":0},
      ]
    },
    { "id":4, "title_de":"Arbeit und Beruf", "title_ru":"Работа и профессия", "title_uz":"Ish va kasb",
      "grammar_topic":"Perfekt (haben/sein + Partizip II) | Перфект",
      "grammar_ru":
        "🔷 Перфект = прошедшее время (разговорное)\n"
        "haben/sein + Partizip II (в конце)\n\n"
        "Слабые глаголы: ge- + Stamm + -t\n"
        "• arbeiten → ge*arbeit*et\n"
        "Сильные: ge- + Stamm(изм.) + -en\n"
        "• fahren → ge*fahr*en\n\n"
        "• Ich habe *gearbeitet*. — Я работал.\n"
        "• Er ist nach Hause *gefahren*. — Он уехал домой.",
      "grammar_uz":
        "🔷 Perfekt = o'tgan zamon (suhbat)\n"
        "haben/sein + Partizip II (oxirida)\n\n"
        "Zaif fe'llar: ge- + asos + -t\n"
        "• arbeiten → ge*arbeit*et\n"
        "Kuchli fe'llar: ge- + asos(o'zgargan) + -en\n"
        "• fahren → ge*fahr*en\n\n"
        "• Ich habe *gearbeitet*. — Men ishladim.\n"
        "• Er ist nach Hause *gefahren*. — U uyga ketdi.",
      "vocab":[
        {"de":"der Beruf","ru":"профессия","uz":"kasb"},
        {"de":"arbeiten","ru":"работать","uz":"ishlash"},
        {"de":"der Arzt","ru":"врач","uz":"shifokor"},
        {"de":"der Lehrer","ru":"учитель","uz":"o'qituvchi"},
        {"de":"der Ingenieur","ru":"инженер","uz":"muhandis"},
        {"de":"der Kaufmann","ru":"бизнесмен","uz":"savdogar"},
        {"de":"das Büro","ru":"офис","uz":"ofis"},
        {"de":"die Stelle","ru":"должность","uz":"lavozim"},
        {"de":"das Gehalt","ru":"зарплата","uz":"maosh"},
        {"de":"der Chef","ru":"начальник","uz":"boshliq"},
        {"de":"die Bewerbung","ru":"заявка / анкета","uz":"ariza"},
        {"de":"Vollzeit / Teilzeit","ru":"полный / неполный рабочий день","uz":"to'liq / qisman ish kuni"},
      ],
      "dialogue":[
        ("A","Was sind Sie von Beruf?"),
        ("B","Ich bin Lehrer. Ich unterrichte Mathematik."),
        ("A","Und wo arbeiten Sie?"),
        ("B","An einer Schule in Taschkent."),
        ("A","Haben Sie vorher auch als Lehrer gearbeitet?"),
        ("B","Nein, ich habe früher als Ingenieur gearbeitet."),
      ],
      "exercises":[
        {"type":"choice","q":"Was sind Sie von ___? (профессия)",
         "opts":["Arbeit","Name","Beruf","Stelle"],"ans":2},
        {"type":"choice","q":"Perfekt von 'arbeiten':",
         "opts":["hat gearbeitet","ist gearbeitet","hat gearbeit","hatte gearbeitet"],"ans":0},
        {"type":"fill","q":"Der Lehrer ___ an einer Schule. (работает)",
         "opts":["wohnt","arbeitet","lernt","fährt"],"ans":1},
      ]
    },
    { "id":5, "title_de":"Reisen und Verkehr", "title_ru":"Путешествия и транспорт", "title_uz":"Sayohat va transport",
      "grammar_topic":"Präpositionen mit Akkusativ | Предлоги с аккузативом",
      "grammar_ru":
        "🔷 Предлоги с Akkusativ: *durch, für, gegen, ohne, um*\n\n"
        "Примеры:\n• Ich fahre *durch* die Stadt. — Я еду через город.\n"
        "• Das Ticket ist *für* dich. — Билет для тебя.\n"
        "• Wir fahren *ohne* Auto. — Мы едем без машины.\n"
        "• Das Flugzeug fliegt *um* 10 Uhr. — Самолёт летит в 10 часов.",
      "grammar_uz":
        "🔷 Akkusativ bilan predloglar: *durch, für, gegen, ohne, um*\n\n"
        "Misollar:\n• Ich fahre *durch* die Stadt. — Men shahar orqali boraman.\n"
        "• Das Ticket ist *für* dich. — Chipta sen uchun.\n"
        "• Wir fahren *ohne* Auto. — Biz mashinasiz ketamiz.\n"
        "• Das Flugzeug fliegt *um* 10 Uhr. — Samolyot soat 10da uchadi.",
      "vocab":[
        {"de":"die Reise","ru":"путешествие","uz":"sayohat"},
        {"de":"das Flugzeug","ru":"самолёт","uz":"samolyot"},
        {"de":"der Zug","ru":"поезд","uz":"poyezd"},
        {"de":"der Bus","ru":"автобус","uz":"avtobus"},
        {"de":"das Ticket / die Fahrkarte","ru":"билет","uz":"chipta"},
        {"de":"der Flughafen","ru":"аэропорт","uz":"aeroport"},
        {"de":"abfahren","ru":"отправляться","uz":"jo'nab ketmoq"},
        {"de":"ankommen","ru":"приезжать","uz":"kelmoq"},
        {"de":"umsteigen","ru":"пересаживаться","uz":"o'tish"},
        {"de":"der Koffer","ru":"чемодан","uz":"chamadon"},
        {"de":"der Pass","ru":"паспорт","uz":"pasport"},
        {"de":"buchen","ru":"бронировать","uz":"band qilmoq"},
      ],
      "dialogue":[
        ("A","Wann fährt der nächste Zug nach Berlin?"),
        ("B","Um 14:30 Uhr auf Gleis 3."),
        ("A","Und wann kommt er in Berlin an?"),
        ("B","Um 18:45 Uhr."),
        ("A","Muss ich umsteigen?"),
        ("B","Nein, es ist ein Direktzug."),
        ("A","Super! Ich nehme eine Fahrkarte, bitte."),
      ],
      "exercises":[
        {"type":"choice","q":"Das Ticket ist ___ mich. (для меня)",
         "opts":["mit","für","durch","ohne"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'umsteigen'?",
         "opts":["садиться","пересаживаться","выходить","стоять"],"ans":1},
        {"type":"fill","q":"Der Zug ___ um 14 Uhr ab. (отправляться)",
         "opts":["kommt","fährt","geht","reist"],"ans":1},
      ]
    },
    { "id":6, "title_de":"Das Wetter", "title_ru":"Погода", "title_uz":"Ob-havo",
      "grammar_topic":"Komparativ und Superlativ | Степени сравнения",
      "grammar_ru":
        "🔷 Komparativ: Adj + *-er* + als\n"
        "🔷 Superlativ: am + Adj + *-(e)sten*\n\n"
        "Примеры:\n• Es ist *wärmer* als gestern. — Теплее, чем вчера.\n"
        "• Der Sommer ist *heißer* als der Frühling.\n"
        "• Der Winter ist *am kältesten*. — Зима самая холодная.\n\n"
        "Неправильные: gut → besser → am besten\n"
        "viel → mehr → am meisten",
      "grammar_uz":
        "🔷 Komparativ: Adj + *-er* + als\n"
        "🔷 Superlativ: am + Adj + *-(e)sten*\n\n"
        "Misollar:\n• Es ist *wärmer* als gestern. — Kechagidan issiqroq.\n"
        "• Der Sommer ist *heißer* als der Frühling.\n"
        "• Der Winter ist *am kältesten*. — Qish eng sovuq.\n\n"
        "Noto'g'ri: gut → besser → am besten",
      "vocab":[
        {"de":"das Wetter","ru":"погода","uz":"ob-havo"},
        {"de":"die Sonne / sonnig","ru":"солнце / солнечный","uz":"quyosh / quyoshli"},
        {"de":"der Regen / regnerisch","ru":"дождь / дождливый","uz":"yomg'ir / yomg'irli"},
        {"de":"der Schnee / verschneit","ru":"снег / снежный","uz":"qor / qorli"},
        {"de":"der Wind / windig","ru":"ветер / ветреный","uz":"shamol / shamolли"},
        {"de":"warm / kalt","ru":"тёплый / холодный","uz":"issiq / sovuq"},
        {"de":"heiß","ru":"жаркий","uz":"juda issiq"},
        {"de":"die Temperatur","ru":"температура","uz":"temperatura"},
        {"de":"der Frühling","ru":"весна","uz":"bahor"},
        {"de":"der Sommer","ru":"лето","uz":"yoz"},
        {"de":"der Herbst","ru":"осень","uz":"kuz"},
        {"de":"der Winter","ru":"зима","uz":"qish"},
      ],
      "dialogue":[
        ("A","Wie ist das Wetter heute?"),
        ("B","Es ist bewölkt und ein bisschen windig."),
        ("A","Regnet es?"),
        ("B","Nein, aber vielleicht am Nachmittag."),
        ("A","Wie viel Grad hat es?"),
        ("B","Ungefähr 15 Grad. Morgen soll es wärmer werden."),
      ],
      "exercises":[
        {"type":"choice","q":"Es ist ___ als gestern. (теплее)",
         "opts":["warm","wärmer","wärmsten","am wärmsten"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'verschneit'?",
         "opts":["дождливый","ветреный","снежный","облачный"],"ans":2},
        {"type":"fill","q":"Der Winter ist am ___. (самый холодный)",
         "opts":["kälteste","kältesten","kälter","kalt"],"ans":1},
      ]
    },
    { "id":7, "title_de":"Feste und Feiern", "title_ru":"Праздники", "title_uz":"Bayramlar",
      "grammar_topic":"Temporale Präpositionen: an, in, um | Временные предлоги",
      "grammar_ru":
        "🔷 *an* + День/Дата: an Weihnachten, am Montag, am 1. Januar\n"
        "🔷 *in* + Месяц/Сезон: im Januar, im Sommer, in der Woche\n"
        "🔷 *um* + Время: um 8 Uhr, um Mitternacht\n\n"
        "Примеры:\n• *An* Weihnachten feiern wir mit der Familie.\n"
        "• *Im* Sommer fahre ich in Urlaub.\n"
        "• Die Party beginnt *um* 20 Uhr.",
      "grammar_uz":
        "🔷 *an* + Kun/Sana: an Weihnachten, am Montag, am 1. Januar\n"
        "🔷 *in* + Oy/Fasl: im Januar, im Sommer\n"
        "🔷 *um* + Vaqt: um 8 Uhr\n\n"
        "Misollar:\n• *An* Weihnachten feiern wir mit der Familie.\n"
        "• *Im* Sommer fahre ich in Urlaub.\n"
        "• Die Party beginnt *um* 20 Uhr.",
      "vocab":[
        {"de":"das Fest / die Feier","ru":"праздник / торжество","uz":"bayram / tantana"},
        {"de":"Weihnachten","ru":"Рождество","uz":"Rojdestvo"},
        {"de":"Ostern","ru":"Пасха","uz":"Pasxa"},
        {"de":"der Geburtstag","ru":"день рождения","uz":"tug'ilgan kun"},
        {"de":"feiern","ru":"праздновать","uz":"nishonlamoq"},
        {"de":"einladen","ru":"приглашать","uz":"taklif qilmoq"},
        {"de":"das Geschenk","ru":"подарок","uz":"sovg'a"},
        {"de":"der Kuchen","ru":"торт / пирог","uz":"tort / pirog"},
        {"de":"die Kerze","ru":"свеча","uz":"sham"},
        {"de":"singen","ru":"петь","uz":"qo'shiq aytmoq"},
        {"de":"tanzen","ru":"танцевать","uz":"raqs tushmoq"},
        {"de":"gratulieren","ru":"поздравлять","uz":"tabriklamoq"},
      ],
      "dialogue":[
        ("A","Herzlichen Glückwunsch zum Geburtstag!"),
        ("B","Danke schön!"),
        ("A","Wie alt wirst du heute?"),
        ("B","Ich werde 25."),
        ("A","Feierst du heute Abend?"),
        ("B","Ja, ich lade Freunde ein. Wir feiern um 19 Uhr."),
        ("A","Toll! Ich bringe einen Kuchen mit."),
      ],
      "exercises":[
        {"type":"choice","q":"___ Weihnachten feiern wir. (на Рождество)",
         "opts":["Im","An","Um","In"],"ans":1},
        {"type":"choice","q":"Was bedeutet 'das Geschenk'?",
         "opts":["торт","свеча","подарок","пение"],"ans":2},
        {"type":"fill","q":"Die Party beginnt ___ 20 Uhr. (в 20:00)",
         "opts":["an","in","um","am"],"ans":2},
      ]
    },
    { "id":8, "title_de":"Pläne und Zukunft", "title_ru":"Планы и будущее", "title_uz":"Rejalar va kelajak",
      "grammar_topic":"Futur I (werden + Infinitiv) | Будущее время",
      "grammar_ru":
        "🔷 Futur I = werden + Infinitiv (в конце)\n"
        "ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden\n\n"
        "Примеры:\n• Ich *werde* Deutsch *lernen*. — Я буду учить немецкий.\n"
        "• Er *wird* Arzt *werden*. — Он станет врачом.\n"
        "• Wir *werden* nach Berlin *fahren*. — Мы поедем в Берлин.\n\n"
        "💡 Часто заменяется Präsens + Zeit: Morgen fahre ich.",
      "grammar_uz":
        "🔷 Futur I = werden + Infinitiv (oxirida)\n"
        "ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden\n\n"
        "Misollar:\n• Ich *werde* Deutsch *lernen*. — Men nemis tilini o'rganaman.\n"
        "• Er *wird* Arzt *werden*. — U shifokor bo'ladi.\n"
        "• Wir *werden* nach Berlin *fahren*. — Biz Berlinga boramiz.",
      "vocab":[
        {"de":"die Zukunft","ru":"будущее","uz":"kelajak"},
        {"de":"der Plan","ru":"план","uz":"reja"},
        {"de":"vorhaben","ru":"планировать","uz":"niyat qilmoq"},
        {"de":"studieren","ru":"учиться (в вузе)","uz":"o'qimoq (oliy maktabda)"},
        {"de":"heiraten","ru":"жениться / выходить замуж","uz":"uylanmoq / turmushga chiqmoq"},
        {"de":"umziehen","ru":"переезжать","uz":"ko'chib o'tmoq"},
        {"de":"vielleicht","ru":"может быть","uz":"balki"},
        {"de":"bestimmt","ru":"точно / обязательно","uz":"albatta"},
        {"de":"hoffentlich","ru":"надеюсь","uz":"umid qilaman"},
        {"de":"der Traum","ru":"мечта","uz":"orzu"},
        {"de":"erreichen","ru":"достичь","uz":"erishmoq"},
        {"de":"erfolgreich","ru":"успешный","uz":"muvaffaqiyatli"},
      ],
      "dialogue":[
        ("A","Was wirst du nach dem Kurs machen?"),
        ("B","Ich werde in Deutschland studieren, hoffentlich."),
        ("A","Was möchtest du studieren?"),
        ("B","Ich werde Ingenieurwissenschaften studieren."),
        ("A","Das ist ein guter Plan! Und danach?"),
        ("B","Danach werde ich vielleicht in Deutschland bleiben oder zurückkommen."),
        ("A","Viel Erfolg!"),
      ],
      "exercises":[
        {"type":"choice","q":"Ich ___ Deutsch lernen. (буду учить, Futur)",
         "opts":["bin","habe","werde","muss"],"ans":2},
        {"type":"choice","q":"Was bedeutet 'hoffentlich'?",
         "opts":["обязательно","может быть","надеюсь","никогда"],"ans":2},
        {"type":"fill","q":"Er wird Arzt ___. (станет)",
         "opts":["sein","werden","haben","gehen"],"ans":1},
      ]
    },
  ]
}
