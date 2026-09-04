from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8973698856:AAEYsZEETpMpbt2O-Wstz8HMt6gnHPSCVuc"
MY_LINK = "https://t.me/dil7598"

async def group_link_sender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return
    await update.message.reply_text(f"🔗 Join karo 👇\n{MY_LINK}", reply_to_message_id=update.message.message_id)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, group_link_sender))
    print("Bot ON hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
