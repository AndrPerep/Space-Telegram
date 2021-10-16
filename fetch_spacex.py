import requests
from pathlib import Path
from load_picture import load_picture


def fetch_spacex_last_launch(folder, directory):
  spacex_url = 'https://api.spacexdata.com/v4/launches/latest'
  response = requests.get(spacex_url)
  response.raise_for_status()
  images_links = response.json()['links']['flickr']['original']

  payload = None
  for number, url in enumerate(images_links):
    filename = f'spacex{number}.jpg'
    path = f'{folder}/{directory}/{filename}'
    load_picture(url, path, payload)


if __name__ == "__main__":
  folder = 'images'
  directory = 'spacex'
  Path(f'{folder}/{directory}').mkdir(parents=True, exist_ok=True)

  fetch_spacex_last_launch(folder, directory)
  