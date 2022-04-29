import json
import os

from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent():
    load_dotenv()
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    """Create an intent of the given intent type"""
    with open('questions.json', 'r', encoding='UTF-8') as file:
        questions = json.load(file)
    for question in questions:
        display_name = question
        training_phrases_parts = questions[question]['questions']
        message_texts = [questions[question]['answer']]
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


if __name__ == '__main__':
    create_intent()
