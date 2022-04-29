import logging
import os

from dotenv import load_dotenv
from telegram import Update, ForceReply, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from intent_detection import detect_intent_texts
from logging_handler import TelegramLogsHandler


logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def handle_messages(update: Update, context: CallbackContext) -> None:
    """Handle the answer message from dialogflow on the user message."""
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')
    user_id = os.getenv('USER_ID')
    rus_language = 'ru'
    message = [update.message.text]
    answer = detect_intent_texts(
        project_id=project_id,
        session_id=user_id,
        texts=message,
        language_code=rus_language
    )
    update.message.reply_text(answer)


def main():
    load_dotenv()
    token = os.getenv('TOKEN_TELEGRAM')
    user_id = os.getenv('USER_ID')
    logging_token = os.getenv('TOKEN_LOGGING')
    logging_bot = Bot(token=logging_token)
    logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(tg_bot=logging_bot, chat_id=user_id))
    logger.info('Бот запущен')
    """Start the bot."""
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
