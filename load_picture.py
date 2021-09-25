import requests
from pathlib import Path

def load_picture(directory, filename, url, path):
  response = requests.get(url)
  response.raise_for_status()
  print('load')

  with open(path, 'wb') as file:
      file.write(response.content)
