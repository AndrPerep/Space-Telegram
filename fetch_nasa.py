import datetime
import requests
import os

from dotenv import load_dotenv
from os.path import split
from os.path import splitext
from urllib.parse import urlsplit
from urllib.parse import unquote

from load_picture import load_picture
from get_path import get_path

def fetch_nasa_apod():
  directory = 'nasa_apod'
  nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
  payload = {
    'api_key': NASA_API_KEY,
    'count': 30
  }
  response = requests.get(nasa_apod_url, params=payload)
  response.raise_for_status()

  for picture in enumerate(response.json()):
    number = picture[0]
    url = picture[1]['url']
    ext = get_extension(url)
    filename = f'nasa_apod{number}{ext}'
    path = get_path(directory, filename)
    load_picture(directory, filename, url, path)

def fetch_nasa_epic():
  directory = 'nasa_epic'
  count = 5
  nasa_epic_url = 'https://epic.gsfc.nasa.gov/api/natural'
  payload = {
    'api_key': NASA_API_KEY
  }
  response = requests.get(nasa_epic_url, params=payload)
  response.raise_for_status()

  for picture in enumerate(response.json()[:count]):
    number = picture[0]
    filename = f'nasa_epic{number}.png'

    picture_name = picture[1]['image']
    picture_date = datetime.datetime.fromisoformat(picture[1]['date'])
    formated_picture_date = picture_date.strftime("%Y/%m/%d")

    url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_picture_date}/png/{picture_name}.png?api_key=DEMO_KEY'
    path = get_path(directory, filename)
    load_picture(directory, filename, url, path)

def get_extension(url):
  split_result = urlsplit(url)
  file_path = unquote(split_result[2])
  splitted_path = split(file_path)
  splitted_filename = splitext(splitted_path[1])
  extension = splitted_filename[1]
  return extension

if __name__ == "__main__":
  load_dotenv()
  NASA_API_KEY = os.getenv('NASA_API_KEY')
  
  fetch_nasa_apod()
  fetch_nasa_epic()
