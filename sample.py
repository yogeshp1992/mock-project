import requests


data = requests.get("https://swapi.dev/api/species/")
print(data.text)
