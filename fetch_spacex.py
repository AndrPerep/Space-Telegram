import requests
from pathlib import Path

def fetch_spacex_last_launch():
  directory = 'spacex'
  spacex_url = 'https://api.spacexdata.com/v4/launches/latest'
  response = requests.get(spacex_url)
  response.raise_for_status()
  images_links = response.json()['links']['flickr']['original']

  for link in enumerate(images_links):
    number = link[0]
    url = link[1]
    filename = f'spacex{number}.jpg'
    load_picture(directory, filename, url)

def load_picture(directory, filename, url):
  response = requests.get(url)
  response.raise_for_status()

  Path(f'images/{directory}').mkdir(parents=True, exist_ok=True)
  path = f'images/{directory}/{filename}'
  with open(path, 'wb') as file:
      file.write(response.content)

if __name__ == "__main__":
  fetch_spacex_last_launch()