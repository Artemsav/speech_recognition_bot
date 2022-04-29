# Speech recognition bot

## Project description

This is an assistant bot for telegram and VK, it will close all typical user questions, but something more complicated - redirect to operators. The bot was trained by the Google Dialogflow neural network. [Dialogflow](https://dialogflow.com/) is a service that allows you to create chatbots for different platforms and languages on different devices.
At first place after registration and you will get all necessary tokens, see describtion in section instalation, it needs to teach the Dialogflow via special teaching phases. You shall gather them and put in json file ```questions.json```. It looks like:

```json
{
    "Apply to job": {
        "questions": [
            "How to get a job with you?",
            "How do you work?",
            "I want to work for you"
            "Is it possible to get a job with you?",
            "Can I work for you?"
            "I want to work as an editor for you"
        ],
        "answer": "If you'd like to join us, email game-of-verbs@gmail.com with a mini-essay about yourself and attach your portfolio."
    },
    "Forgot password": {
        "questions": [
            "I do not remember the password",
            "I can not enter",
            "Login Problems"
            "Forgot password",
            "I forgot my login"
            "Restore password",
            "How to recover password",
            "Incorrect login or password",
            "Login failed",
            "Can't sign in"
        ],
        "answer": "If you can't log in, use the Forgot your password? under the login form. You will receive an email with further instructions. Check the Spam folder, sometimes letters end up in it."
    }...
}
```
and run prepared for this script:
```bash
python create_intent.py
```

To run telegram_bot:

```bash
python telegram_bot.py
```

To run vk bot:

```bash
python vk.py
```

Example of telegram bot (or you can find it here: @games_of_verbs_bot):
![Example](./images/demo_tg_bot.gif)

Example of vk bot (or you can find it here: [vk bot of club - SZone-Online клан ГОРН](https://vk.com/club56009176), pick messages there):

![Example](./images/demo_vk_bot.gif)

## Instalation

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

There is enviroment variables using in the application, you will need tp create ```.env``` file. A ```.env``` file is a text file containing key value pairs of all the environment variables required by the application. You can see example of it below:

```python
# example of environment variables defined inside a .env file
TOKEN_TELEGRAM=1253123421:FFA1DSGOh_dfQACXYT5IiQwEBP5CwJozyP8
USER_ID=612578269
PROJECT_ID=my-bot-1529
GOOGLE_APPLICATION_CREDENTIALS=my-bot-1529-2cfc3fe2cb11.json
VK_KEY=eLbyo6isRjMrRssdsdsdddsaaafsaad
```

TOKEN_DEVMAN - you will get it via [Devman API](https://dvmn.org/api/docs/)  

TOKEN_TELEGRAM - to get it please writte to Telegram @BotFather bot, first you shall ```/start``` command, than ```/newbot```, than follow the instruction in Telegram.  
USER_ID - to get it please writte to Telegram @userinfobot. Send ```/start``` command to the bot.

PROJECT_ID - to get it sign in here and follow [the guid](https://cloud.google.com/dialogflow/docs/quick/setup)

GOOGLE_APPLICATION_CREDENTIALS - follow [the guid](https://cloud.google.com/dialogflow/docs/quick/setup)

VK_KEY - in the menu "Work with API" in the group management menu in VK

## Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org)
