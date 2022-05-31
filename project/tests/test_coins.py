from . import *
import pytest
import json
from app.api import crud_coins

def test_read_all_coins(test_app_with_db):
    valid_coins = (VALID_COIN, VALID_COIN_WITH_DATE)
    valid_coin_ids = [response.json()["id"]
                      for response in [test_app_with_db.post("/coins/", data=json.dumps(valid_coin))
                                       for valid_coin in valid_coins]]
    print(valid_coin_ids)
    response = test_app_with_db.get("/coins/")
    assert response.status_code == 200

    coins = response.json()
    assert ([coin["id"] for coin in coins] == valid_coin_ids)
    assert ([coin["name_id"]
             for coin in coins] == [valid_coin["name_id"]
                                    for valid_coin in valid_coins])

def test_create_coin(test_app_with_db):
    response = test_app_with_db.post(
        "/coins/", data=json.dumps(VALID_COIN)
    )
    assert response.status_code == 201
    assert response.json()["name"] == VALID_COIN["name"]
    assert response.json()["name_id"] == VALID_COIN["name_id"]
    assert response.json()["symbol"] == VALID_COIN["symbol"]
    assert not response.json().get("first_coin_emitted_on")

    response = test_app_with_db.post(
        "/coins/", data=json.dumps(VALID_COIN_WITH_DATE)
    )
    assert response.status_code == 201
    assert response.json()["name"] == VALID_COIN_WITH_DATE["name"]
    assert response.json()["name_id"] == VALID_COIN_WITH_DATE["name_id"]
    assert response.json()["symbol"] == VALID_COIN_WITH_DATE["symbol"]
    assert response.json()["first_coin_emitted_on"] == VALID_COIN_WITH_DATE["first_coin_emitted_on"]

@pytest.mark.parametrize(
    "payload, detail",[
        [{},[NAME_MISSING, NAMEID_MISSING, SYMBOL_MISSING]],
        [INVALID_COIN, [NAMEID_INVALID, SYMBOL_INVALID]]
    ]
)
def test_create_coin_invalid_data(test_app, payload, detail):
    response = test_app.post("/coins/", data=json.dumps(payload))
    assert response.status_code == 422
    assert response.json == {"detail": detail}

def test_read_coin(test_app_with_db):
    response = test_app_with_db.post("/accounts/", data=json.dumps(VALID_COIN_WITH_DATE))
    coin_id = response.json()["id"]

    response = test_app_with_db.get(f"/accounts/{VALID_COIN_WITH_DATE['name_id']}/")
    assert response.status_code == 200

    full_response = response.json()
    assert full_response["id"] == coin_id
    assert full_response["name_id"] == VALID_COIN_WITH_DATE["name_id"]
    assert full_response["name"] == VALID_COIN_WITH_DATE["name"]
    assert full_response["symbol"] == VALID_COIN_WITH_DATE["symbol"]
    assert full_response["first_coin_emitted_on"] == VALID_COIN_WITH_DATE["first_coin_emitted_on"]

def test_read_coin_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/coins/not-a-coin-id/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Coin not found"

def test_update_coin(test_app_with_db):
    response = test_app_with_db.post("/coins/", data=json.dumps(VALID_COIN))
    coin_id = response.json()["id"]

    response = test_app_with_db.put(f"/coins/{VALID_COIN_WITH_DATE['name_id']}/", data=json.dumps(VALID_COIN_WITH_DATE))
    full_response = response.json()
    assert response.status_code == 200
    assert full_response["id"] == coin_id
    assert full_response["name_id"] == VALID_COIN_WITH_DATE["name_id"]
    assert full_response["name"] == VALID_COIN_WITH_DATE["name"]
    assert full_response["symbol"] == VALID_COIN_WITH_DATE["symbol"]
    assert full_response["first_coin_emitted_on"] == VALID_COIN_WITH_DATE["first_coin_emitted_on"]

@pytest.mark.parametrize(
    "coin_name_id, payload, status_code, detail", [
        ["not-a-coin-id", VALID_COIN, 404, "Coin not found"],
    ]
)
def test_update_coin_invalid(test_app_with_db, coin_name_id, payload, status_code, detail):
    response = test_app_with_db.put(f"/coins/{coin_name_id}/", data=json.dumps(payload))
    assert response.status_code == status_code
    assert response.json()["detail"] == detail

def test_delete_coin(test_app_with_db):
    response = test_app_with_db.post("/coins/", data=json.dumps(VALID_COIN))
    coin_id = response.json()["id"]

    response = test_app_with_db.delete(f"/accounts/{VALID_COIN['name_id']}/")
    assert response.status_code == 200
    assert response.json() == {**VALID_COIN, "id": coin_id}

def test_populate_db(test_app_with_db, monkeypatch):

    async def mock_get_external(payload):
        with open("test-data.json", "r") as test_data_source:
            test_data = json.dumps(test_data_source.read())
        return test_data

    monkeypatch.setattr(crud_coins, "get_external", mock_get_external)
    test_payload = {"start_page": 35, "limit": 2}
    test_response = {"data": [
        {"name_id": "whitecoin", "id": 1},
        {"name_id": "energy-web-token", "id": 2}],
        "total_coins_created": 2}

    response = test_app_with_db.post("/coins/populate/", json.dumps(test_payload))
    assert response.status_code == 201
    assert response.json() == test_response
