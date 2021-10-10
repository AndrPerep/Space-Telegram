import requests
from pathlib import Path
from load_picture import load_picture

def fetch_spacex_last_launch():
  directory = 'spacex'
  spacex_url = 'https://api.spacexdata.com/v4/launches/latest'
  response = requests.get(spacex_url)
  response.raise_for_status()
  images_links = response.json()['links']['flickr']['original']

  for number, url in enumerate(images_links):
    filename = f'spacex{number}.jpg'
    path = get_path(directory, filename)
    load_picture(url, path, payload='')

if __name__ == "__main__":
  fetch_spacex_last_launch()
  