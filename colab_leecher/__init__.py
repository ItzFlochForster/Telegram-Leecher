# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging, json
from uvloop import install
from pyrogram.client import Client

# Read the dictionary from the txt file
with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["22606849"]
API_HASH = credentials["ef85493cd32eadcb5309b5957d8d1b86"]
BOT_TOKEN = credentials["7565794309:AAEu04K7yOmB5C4IjfFn3yPgZXn4bkC3B-o"]
OWNER = credentials["8189246702"]
DUMP_ID = credentials["-1002623071471"]


logging.basicConfig(level=logging.INFO)

install()

colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
