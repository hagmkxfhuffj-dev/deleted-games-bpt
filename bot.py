from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8998637230:AAEv2Utfld_OimFWuCCaK-y4hJi9vilAFYU"

GAMES = {
    "flappy": "🐤 فلابي بيرد الاصلية - https://flappybird.io/",
    "subway": "🏃 صب واي القديمة",
}

async def start(update, context):
    await update.message.reply_text("أهلا بيك في بوت الألعاب المحذوفة! 🎮🔥")

async def handle_message(update, context):
    await update.message.reply_text("لقيتها! جرب /start")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
