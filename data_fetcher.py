from requests.auth import HTTPBasicAuth
import requests


import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY')



def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  URL = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  auth = HTTPBasicAuth('X-Api-Key', API_KEY)
  headers = {'X-Api-Key': API_KEY}
  response = requests.get(URL, headers=headers, auth=auth)
  animals_data = response.json()
  return animals_data