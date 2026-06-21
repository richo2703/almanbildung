# 🇩🇪 Alman Bildung — Telegram Mini App

Приложение для изучения немецкого языка A1–B1 на русском и узбекском.

## Возможности

- 📚 **48 уроков** — грамматика, диалоги, примеры (A1.1 → B1.2)
- 📝 **2304 слова** — флэш-карточки с кнопками «Знаю / Не знаю»
- ✅ **576 тестовых вопросов** — мгновенная проверка
- ⭐ **XP-система** — мотивация через очки опыта
- 📊 **Прогресс** — статистика по каждому уровню
- 🇷🇺🇺🇿 Русский + Узбекский интерфейс

## Стек

| Слой | Технология |
|------|-----------|
| Frontend | React 18 + Vite + React Router |
| Backend | FastAPI + SQLite |
| Bot | python-telegram-bot 20 |

## Структура

```
mini_app/
├── backend/          # FastAPI API
│   ├── main.py       # Эндпоинты
│   ├── database.py   # SQLite слой
│   ├── content.py    # Агрегатор контента
│   ├── content_a1/a2/b1.py  # Базовый контент
│   ├── ext_a1/a2/b1.py      # Расширения (+36 слов/урок)
│   └── requirements.txt
├── frontend/         # React Mini App
│   ├── src/
│   │   ├── pages/    # 7 страниц
│   │   ├── components/
│   │   ├── api.js    # HTTP клиент
│   │   └── App.jsx
│   ├── index.html
│   └── package.json
├── bot.py            # Launcher bot
└── SETUP.md          # Инструкция деплоя
```

## Быстрый старт

### Backend
```bash
cd backend
pip install -r requirements.txt
BOT_TOKEN="токен" uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev     # dev режим
npm run build   # сборка для продакшена
```

### Bot
```bash
BOT_TOKEN="токен" WEBAPP_URL="https://your-domain.com" python3 bot.py
```

Полная инструкция деплоя на VPS — см. [SETUP.md](SETUP.md).
