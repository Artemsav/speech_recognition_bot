# If_check bot

## Project description

This is bot for cheking if the works are already reviewed. To run the bot you shall use the following command. Also there is the separate logging bot for main bot, it sends you messages when something caused errors in the bot.:

```bash
python main.py
```

When you will get review results from your curator you will have the message with it in your telegram bot.
![Example](./images/devman.png)

Example of logging error:

![Example](./images/devman2.png)

## Instalation

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

There is enviroment variables using in the application, you will need tp create ```.env``` file. A ```.env``` file is a text file containing key value pairs of all the environment variables required by the application. You can see example of it below:

```python
# example of environment variables defined inside a .env file
TOKEN_DEVMAN=Token b21a135t53faba6a70w12d11e223657689ae21qj
TOKEN_TELEGRAM=1253123421:FFA1DSGOh_dfQACXYT5IiQwEBP5CwJozyP8
USER_ID=612578269
TOKEN_LOGGING=5479412501:FFA1DSGOh_Lm3eLbyo6isRjMrRssdsdsdSAW
```

TOKEN_DEVMAN - you will get it via [Devman API](https://dvmn.org/api/docs/)  
TOKEN_TELEGRAM - to get it please writte to Telegram @BotFather bot, first you shall ```/start``` command, than ```/newbot```, than follow the instruction in Telegram.  
USER_ID - to get it please writte to Telegram @userinfobot. Send ```/start``` command to the bot.

TOKEN_LOGGING - to get it once again please writte to Telegram @BotFather bot, first you shall ```/start``` command, than ```/newbot```, than follow the instruction in Telegram. This is token for separate bot supposed to logging error from main one.S

## Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org)
