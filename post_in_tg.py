import os
import telegram
import time

from dotenv import load_dotenv
from os import listdir 
from os.path import isfile
from os.path import join

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def post_in_telegram(tg_token, chat_id, folder):
  bot = telegram.Bot(token=tg_token)
  sleep_time = 86400
  while True:
    for picture in get_pictures(folder):
      picture_path = f'{folder}{picture}'
      with open(picture_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=open(picture_path, 'rb'))
      time.sleep(sleep_time)


def get_pictures(folder):
  pictures = []
  for element in listdir(folder):
    if isfile(join(folder,element)):
      pictures.append(element)
    else:
      for file in listdir(join(folder,element)):
        pictures.append(f'{element}/{file}')
  return pictures


if __name__ == "__main__":
  folder = 'images/'
  post_in_telegram(TG_TOKEN, CHAT_ID, folder)
