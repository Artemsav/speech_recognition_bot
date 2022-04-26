import logging
import os
import random

import vk_api as vk
from dotenv import load_dotenv
from google.cloud import dialogflow
from requests.models import ReadTimeoutError
from vk_api.longpoll import VkEventType, VkLongPoll


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
        return response.query_result.fulfillment_text


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def echo(event, vk_api, answer):
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer,
        random_id=random.randint(1,1000)
    )


def main():
    load_dotenv()
    token = os.getenv('VK_KEY')
    rus_language = 'ru'
    project_id = os.getenv('PROJECT_ID')
    user_id = os.getenv('USER_ID')
    """Start the bot."""
    vk_session = vk.VkApi(token=token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer = detect_intent_texts(
                project_id=project_id,
                session_id=user_id,
                texts=[event.text],
                language_code=rus_language
                )
            echo(event, vk_api, answer=answer)


if __name__ == '__main__':
    main()
