import logging
import os
import random
import time

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkEventType, VkLongPoll
from telegram import Bot
from intent_detection import detect_intent_texts
from logging_handler import TelegramLogsHandler

logger = logging.getLogger(__name__)


def handle_messages(event, vk_api, answer):
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer,
        random_id=random.randint(1, 1000)
    )


def main():
    load_dotenv()
    token = os.getenv('VK_KEY')
    rus_language = 'ru'
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    user_id = os.getenv('TG_USER_ID')
    logging_token = os.getenv('TG_TOKEN_LOGGING')
    logging_bot = Bot(token=logging_token)
    logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
    logger.setLevel(logging.DEBUG)
    """Start the bot."""
    vk_session = vk.VkApi(token=token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    logger.addHandler(TelegramLogsHandler(tg_bot=logging_bot, chat_id=user_id))
    logger.info('Бот запущен')
    for event in longpoll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                answer = detect_intent_texts(
                    project_id=project_id,
                    session_id=event.user_id,
                    texts=[event.text],
                    language_code=rus_language
                    ).get('vk')
                if answer:
                    handle_messages(event, vk_api, answer=answer)
        except ConnectionError as exc:
            logger.error(exc)
            time.sleep(60)


if __name__ == '__main__':
    main()
