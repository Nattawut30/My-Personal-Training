# How to connect to an API using Python
# Import another resources from online

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response) # [200] HTTP status code means OK

    # To check if it works or not
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "Mewtwo"
pokemon_infor = get_pokemon_info(pokemon_name)

if pokemon_infor:
    print(f"Name: {pokemon_infor["name"].capitalize()}")
    print(f"ID: {pokemon_infor["id"]}")
    print(f"Height: {pokemon_infor["height"]}")
    print(f"Weight: {pokemon_infor["weight"]}")