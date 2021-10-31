import datetime
import requests
import os

from dotenv import load_dotenv
from os.path import split
from os.path import splitext
from pathlib import Path
from urllib.parse import urlsplit
from urllib.parse import unquote

from load_picture import load_picture


def fetch_nasa_apod(nasa_api_key, folder, directory):
  nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
  payload = {
    'api_key': nasa_api_key,
    'count': 2
  }
  response = requests.get(nasa_apod_url, params=payload)
  response.raise_for_status()

  for number, picture in enumerate(response.json()):
    url = picture['url']
    ext = get_extension(url)
    filename = f'nasa_apod{number}{ext}'
    path = f'{folder}/{directory}/{filename}'
    load_picture(url, path)


def fetch_nasa_epic(nasa_api_key, folder, directory):
  count = 2
  nasa_epic_url = 'https://epic.gsfc.nasa.gov/api/natural'
  payload = {
    'api_key': nasa_api_key
  }
  response = requests.get(nasa_epic_url, params=payload)
  response.raise_for_status()

  for number, picture in enumerate(response.json()[:count]):
    filename = f'nasa_epic{number}.png'
    picture_name = picture['image']
    picture_date = datetime.datetime.fromisoformat(picture['date'])
    formated_picture_date = picture_date.strftime('%Y/%m/%d')

    url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_picture_date}/png/{picture_name}.png'
    path = f'{folder}/{directory}/{filename}'
    load_picture(url, path, payload)


def get_extension(url):
  splitted_url = urlsplit(url)
  file_path = unquote(splitted_url[2])
  splitted_filename = splitext(file_path)
  extension = splitted_filename[1]
  return extension


if __name__ == '__main__':
  load_dotenv()
  nasa_api_key = os.getenv('NASA_API_KEY')
  folder = 'images'
  apod_directory = 'nasa_apod'
  epic_directory = 'nasa_epic'
  Path(f'{folder}/{apod_directory}').mkdir(parents=True, exist_ok=True)
  Path(f'{folder}/{epic_directory}').mkdir(parents=True, exist_ok=True)

  fetch_nasa_apod(nasa_api_key, folder, apod_directory)
  fetch_nasa_epic(nasa_api_key, folder, epic_directory)
