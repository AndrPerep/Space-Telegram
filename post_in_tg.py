import os
import telegram
import time

from dotenv import load_dotenv
from os import listdir 
from os.path import isfile
from os.path import join

def post_in_telegram(TG_TOKEN, CHAT_ID, folder):
  bot = telegram.Bot(token=TG_TOKEN)
  sleep_time = 86400
  while True:
    for picture in get_pictures_list(folder):
      picture_path = f'{folder}{picture}'
      with open(picture_path, 'rb') as file:
        bot.send_photo(chat_id=CHAT_ID, photo=open(picture_path, 'rb'))
      print('hello')
      time.sleep(sleep_time)

def get_pictures_list(folder):
  pictures = []
  path = (folder)
  for i in listdir(path):
    if isfile(join(path,i)):
      pictures.append(i)
    else:
      for file in listdir(f'images/{i}/'):
        pictures.append(f'{i}/{file}')
  return pictures

if __name__ == "__main__":
  load_dotenv()
  TG_TOKEN = os.getenv('TG_TOKEN')
  CHAT_ID = os.getenv('CHAT_ID')

  folder = 'images/'

  post_in_telegram(TG_TOKEN, CHAT_ID, folder)
