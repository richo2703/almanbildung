"""Alman Bildung — Telegram Launcher Bot
Просто открывает Mini App кнопкой.
"""
import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://your-domain.com")


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "Ученик"

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="🇩🇪 Открыть Alman Bildung",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])

    await update.message.reply_text(
        f"Привет, {name}! 👋\n\n"
        "🎓 *Alman Bildung* — учи немецкий A1→B1\n\n"
        "• 48 уроков с грамматикой\n"
        "• 2304 слова с карточками\n"
        "• 576 тестовых вопросов\n"
        "• Прогресс и XP-система\n\n"
        "Нажми кнопку чтобы начать 👇",
        parse_mode="Markdown",
        reply_markup=keyboard
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Нажми /start чтобы открыть приложение.",
    )


def main():
    if not TOKEN:
        print("❌ BOT_TOKEN не установлен!")
        return
    if "your-domain" in WEBAPP_URL:
        print("⚠️  Установи WEBAPP_URL в env переменных!")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))

    print(f"🤖 Bot запущен. WEBAPP_URL={WEBAPP_URL}")
    app.run_polling()


if __name__ == "__main__":
    main()
