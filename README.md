# Speech recognition bot

## Project description

This is an assistant bot for telegram and VK, it will close all typical user questions, but something more complicated - redirect to operators. The bot was trained by the Google Dialogflow neural network

To run telegram_bot:

```bash
python telegram_bot.py
```

To run vk bot:

```bash
python vk.py
```

Example of telegram bot:
![Example](./images/demo_tg_bot.gif)

Example of vk bot:

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
