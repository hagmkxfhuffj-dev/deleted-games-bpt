from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8998637230:AAEv2Utfld_OimFWuCCaK-y4hJi9vilAFYU"

GAMES = {
"flappy": "🐤 Flappy Bird الاصلية\nhttps://flappybird.io/",
"pou": "👽 Pou القديمة\nhttps://pou-game.com/",
"subway": "🏃 Subway Surfers\nhttps://poki.com/en/g/subway-surfers",
"temple": "🏛️ Temple Run 1\nhttps://temple-run.en.uptodown.com/android",
"angry": "🐦 Angry Birds 2009\nhttps://angry-birds.en.uptodown.com/android",
"candy": "🍬 Candy Crush 2012\nhttps://candy-crush-saga.en.uptodown.com/android",
"hill": "🚗 Hill Climb Racing\nhttps://hill-climb-racing.en.uptodown.com/android",
"tom": "🐱 Talking Tom 2010\nhttps://talking-tom.en.uptodown.com/android"
}

async def start(update, context):
    await update.message.reply_text("🎮 اهلا بيك في بوت العاب محذوفة BPT!\n\nابعت اسم لعبة مثل:\nflappy, pou, subway, temple, angry, candy, hill, tom")

async def search(update, context):
    q = update.message.text.lower()
    for k, v in GAMES.items():
        if k in q:
            await update.message.reply_text(f"لقيتها 🔥\n\n{v}")
            return
    await update.message.reply_text("مش لاقيها 😅 جرب: flappy, pou, subway, temple")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))
    app.run_polling()

if __name__ == "__main__":
    main()
