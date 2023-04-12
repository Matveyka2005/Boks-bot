import os 
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import message_texts
from books import get_all_books


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_caht is None in /start")
        return 
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_texts.GREETINGS
        )
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_caht is None in /help")
        return 
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_texts.HELP
        )
    
async def all_books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_caht is None in /all_books")
        return 
    all_books_chanks = await get_all_books(chank_size=5)
    for chunk in all_books_chanks:
        response = "\n".join((book.name for book in chunk))
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=response
            )
    

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)
    
    allbooks_handler = CommandHandler('allbooks', all_books)
    application.add_handler(allbooks_handler)
    
    application.run_polling()