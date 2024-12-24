import pytest
import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "99b572ea0024c6b6a824a9553a05d74a"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = 12649
def test_status_code():
    response = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "Cucumber"