from pathlib import Path

def get_path(directory, filename):
    folder = 'images'
    Path(f'{folder}/{directory}').mkdir(parents=True, exist_ok=True)
    path = f'{folder}/{directory}/{filename}'
    return path
