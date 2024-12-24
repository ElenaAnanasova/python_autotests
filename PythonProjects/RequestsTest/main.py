import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "99b572ea0024c6b6a824a9553a05d74a"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
body_create = {
    "name": "Lenny",
    "photo_id": 1
}

body_name_change = {
    "pokemon_id": "168151",
    "name": "Zazu"
}

body_ad_pokeball = {
    "pokemon_id": "168151",
}


"""response_create = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_create)
print(response_create.text)"""

"""response_name_change = requests.patch(url = f"{URL}/pokemons", headers = HEADER, json = body_name_change)
print(response_name_change.text)"""

"""response_add_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = body_ad_pokeball)
print(response_add_pokeball.text)"""