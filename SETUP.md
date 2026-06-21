# Alman Bildung Mini App — Инструкция по деплою

## Структура проекта

```
mini_app/
├── backend/          ← FastAPI (API + контент)
│   ├── main.py
│   ├── database.py
│   ├── content.py
│   ├── content_a1.py / a2.py / b1.py
│   ├── ext_a1.py / a2.py / b1.py
│   └── requirements.txt
├── frontend/         ← React + Vite (Mini App UI)
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── bot.py            ← Launcher bot (открывает Mini App)
└── SETUP.md
```

---

## Шаг 1 — Получить токен бота

1. Написать @BotFather → `/newbot`
2. Имя: `Alman Bildung`, username: `alman_bildung_bot`
3. Скопировать токен

---

## Шаг 2 — Настроить домен (HTTPS обязателен!)

Telegram Mini App требует HTTPS. Варианты:

### Вариант A: Nginx + SSL (рекомендуется)

```bash
# Установить Nginx + Certbot
sudo apt install nginx certbot python3-certbot-nginx -y

# Получить SSL сертификат
sudo certbot --nginx -d your-domain.com

# Nginx конфиг /etc/nginx/sites-available/alman
server {
    listen 443 ssl;
    server_name your-domain.com;

    # Frontend (React build)
    root /home/ubuntu/mini_app/frontend/dist;
    index index.html;
    try_files $uri $uri/ /index.html;

    # Backend API
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
}
```

### Вариант B: ngrok (для тестирования)

```bash
ngrok http 8000
# Скопировать https://xxxx.ngrok.io как WEBAPP_URL
```

---

## Шаг 3 — Запустить Backend

```bash
cd mini_app/backend

# Установить зависимости
pip3 install -r requirements.txt --break-system-packages

# Запустить
BOT_TOKEN="ВАШ_ТОКЕН" uvicorn main:app --host 0.0.0.0 --port 8000
```

### Systemd сервис для backend:

```bash
sudo nano /etc/systemd/system/alman-api.service
```

```ini
[Unit]
Description=Alman Bildung API
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/mini_app/backend
Environment=BOT_TOKEN=ВАШ_ТОКЕН_ЗДЕСЬ
ExecStart=/usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable alman-api
sudo systemctl start alman-api
```

---

## Шаг 4 — Собрать Frontend

```bash
cd mini_app/frontend

# Установить Node.js (если нет)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y

# Установить зависимости
npm install

# Собрать (если API на том же домене)
npm run build

# Если API на другом адресе — добавить в .env:
echo "VITE_API_URL=https://your-domain.com" > .env
npm run build
```

Готовая папка `dist/` обслуживается Nginx.

---

## Шаг 5 — Запустить Launcher Bot

```bash
# Установить зависимости бота
pip3 install python-telegram-bot==20.7 --break-system-packages

# Запустить
BOT_TOKEN="ВАШ_ТОКЕН" WEBAPP_URL="https://your-domain.com" python3 bot.py
```

### Systemd для бота:

```ini
[Unit]
Description=Alman Bildung Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/mini_app
Environment=BOT_TOKEN=ВАШ_ТОКЕН_ЗДЕСЬ
Environment=WEBAPP_URL=https://your-domain.com
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

---

## Шаг 6 — Настроить Mini App в BotFather

1. @BotFather → `/mybots` → выбрать бота
2. `Bot Settings` → `Menu Button` → `Configure menu button`
3. Ввести URL: `https://your-domain.com`
4. Ввести текст кнопки: `🎓 Учить немецкий`

---

## Проверка

```bash
# Статус сервисов
sudo systemctl status alman-api
sudo systemctl status alman-bot

# Логи
sudo journalctl -u alman-api -f
sudo journalctl -u alman-bot -f

# Тест API
curl https://your-domain.com/api/levels
```

---

## Команды бота

| Команда | Действие |
|---------|----------|
| /start  | Открыть Mini App |
| /help   | Справка |

---

## Возможности Mini App

- 📚 **48 уроков** (A1.1 → B1.2)
- 📝 **2304 слова** с карточками "Знаю / Не знаю"
- ✅ **576 тестовых вопросов** с мгновенной проверкой
- ⭐ **XP-система** (5 XP/урок, 2 XP/слово, 2 XP/вопрос)
- 📊 **Статистика** по каждому уровню
- 🇩🇪🇷🇺🇺🇿 **Немецкий + Русский + Узбекский**
