import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.api-ninjas.com/v1/animals?name="
headers = {"X-Api-Key": API_KEY}


def fetch_data(animal_name: str):
    """
    Fetches the animals data for the given 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {...},
        'locations': [...],
        'characteristics': {...}
    }

    If no animal is found, returns a list with one dict:
    [{"error": "<h2>The animal {animal_name} doesn't exist.</h2>"}]
    """

    response = requests.get(URL + animal_name, headers=headers)

    try:
        animals_data = response.json()
    except ValueError:
        return [{"error": f"<h2>The animal {animal_name} doesn't exist.</h2>"}]

    if not animals_data:
        return [{"error": f"<h2>The animal {animal_name} doesn't exist.</h2>"}]

    return animals_data
