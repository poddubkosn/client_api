from pyrogram import Client
from pyrogram import filters
from dotenv import load_dotenv
import os
import telegram
import re
load_dotenv()
other_list_of_chats = [-1001521804025]
list_of_chats = [-632320349, -1001424513919, ]
TELEGRAM_TOKEN = os.getenv('TOKEN')
API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')
local_dir = os.path.abspath(os.curdir)

app = Client('my_account', API_ID, API_HASH)

CHAT_IDS = os.getenv('CHAT_IDS')
CHAT_IDS = [int(el) for el in CHAT_IDS.split(',') if el]
with open(local_dir+'/data', 'r') as f:
    numbers_str = f.read()
template_of_numbers = [int(el) for el in numbers_str.split(', ')]
# template_of_numbers = [3421, 6079, 594, 595, 2353, 4824, 4556, 21, 17, 2354,
#                        4825, 60, 637, 2355, 1459, 2255, 4036, 70, 66, 60,
#                        6229, 3429, 645, 5356, 2350, 4530, 4559, 4558, 4557,
#                        2825, 2254, 3797, 5486, 64]
try:
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
except Exception as error:
    print(error)


@app.on_message(filters.chat(list_of_chats))
def from_pyrogramchat(client, message):
    print(message)
    match_number = re.match(r'(\d+).*', message.text)
    if match_number:
        if int(match_number[1]) in template_of_numbers:
            for chat_id in CHAT_IDS:
                try:
                    bot.send_message(chat_id, message.text)
                except Exception as error:
                    print(error)
                    continue


app.run()
