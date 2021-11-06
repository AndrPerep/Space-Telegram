import os
import telegram
import time

from dotenv import load_dotenv
from os import listdir
from os.path import isfile
from os.path import join


def post_in_telegram(tg_token, chat_id):

  folder = 'images/'
  bot = telegram.Bot(token=tg_token)
  sleep_time = 86400

  while True:
    for picture in get_pictures(folder):
      picture_path = f'{folder}{picture}'
      with open(picture_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)
      time.sleep(sleep_time)


def get_pictures(folder):
  pictures = []
  for element in listdir(folder):
    if isfile(join(folder, element)):
      pictures.append(element)
    else:
      for file in listdir(join(folder,element)):
        pictures.append(f'{element}/{file}')
  return pictures


if __name__ == '__main__':
  load_dotenv()
  tg_token = os.getenv('TG_TOKEN')
  chat_id = os.getenv('CHAT_ID')
  post_in_telegram(tg_token, chat_id)
