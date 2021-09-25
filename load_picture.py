import requests

def load_picture(directory, filename, url, path):
  response = requests.get(url)
  response.raise_for_status()

  with open(path, 'wb') as file:
      file.write(response.content)
