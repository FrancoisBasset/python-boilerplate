import random
import requests

def get_random_pokemon():
    pokedex_id = str(random.randint(1, 1025))
    return get_pokemon_by_id(pokedex_id)

def get_pokemon_by_id(pokedex_id):
    json = requests.get('https://tyradex.app/api/v1/pokemon/' + pokedex_id).json()

    if 'status' in json and 'message' in json:
        return None

    return json['name']['fr']