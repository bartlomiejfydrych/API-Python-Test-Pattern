import os
from http import HTTPStatus

import pytest

from api_interview.requests.delete_user import delete_user
from api_interview.requests.get_token import get_token
from api_interview.requests.post_create_user import post_create_user
from dotenv import load_dotenv

from api_interview.resources.files_config import ENV_FILE_PATH


@pytest.fixture(scope="session")
def auth():
    load_dotenv(ENV_FILE_PATH)
    username = os.getenv("USER_USERNAME")
    password = os.getenv("USER_PASSWORD")
    response = get_token(username, password)
    assert response.status_code == 200
    response_json = response.json()
    token = response_json["access_token"]
    return token


@pytest.fixture
def create_delete_user(auth):
    response = post_create_user(
        token=auth,
        username="Adrian PUTa4",
        age=41,
        admin=False,
        skills=["Oddychanie", "Jedzenie", "Spanie"],
        city="Kraków",
        street="Partyzantów",
        street_number="41c",
        additional=[{"key": "Broń", "value": "Miecz"}]
    )
    assert response.status_code == 201
    user = response.json()

    yield user

    response = delete_user(auth, user["id"])
    assert response.status_code == 204
