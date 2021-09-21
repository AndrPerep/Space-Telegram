import os
import telegram
import time

from dotenv import load_dotenv
from os import listdir 
from os.path import isfile
from os.path import join as joinpath

def post_in_telegram():
  bot = telegram.Bot(token=TG_TOKEN)
  sleep_time = 86400
  while True:
    for picture in get_pictures_list():
      bot.send_photo(chat_id=CHAT_ID, photo=open(f'images/{picture}', 'rb'))
      time.sleep(sleep_time)

def get_pictures_list():
  pictures = []
  path = ('images/')
  for i in listdir(path):
    if isfile(joinpath(path,i)):
      pictures.append(i)
    else:
      for file in listdir(f'images/{i}/'):
        pictures.append(f'{i}/{file}')
  return pictures

if __name__ == "__main__":
  load_dotenv()
  TG_TOKEN = os.getenv('TG_TOKEN')
  CHAT_ID = os.getenv('CHAT_ID')

  post_in_telegram()
