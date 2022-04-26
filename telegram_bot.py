import json
import logging
import os
import time

import requests
from dotenv import load_dotenv
from requests.models import ReadTimeoutError
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google.cloud import dialogflow


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


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


def create_intent():
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')
    """Create an intent of the given intent type."""
    with open('questions.json', 'r', encoding='UTF-8') as file:
        questions = json.load(file)
    for question in questions:
        display_name = question
        training_phrases_parts = questions[question]['questions']
        message_texts = [questions[question]['answer']]
        print(message_texts)
        intents_client = dialogflow.IntentsClient()

        parent = dialogflow.AgentsClient.agent_path(project_id)
        training_phrases = []
        for training_phrases_part in training_phrases_parts:
            part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
            # Here we create a new training phrase for each provided part.
            training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)

        text = dialogflow.Intent.Message.Text(text=message_texts)
        message = dialogflow.Intent.Message(text=text)

        intent = dialogflow.Intent(
            display_name=display_name, training_phrases=training_phrases, messages=[message]
        )

        response = intents_client.create_intent(
            request={"parent": parent, "intent": intent}
        )

        print("Intent created: {}".format(response))


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def handle_status(update: Update, context: CallbackContext) -> None:
    """Handle the answer message from dialogflow the user message."""
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
    """Start the bot."""
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_status))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
