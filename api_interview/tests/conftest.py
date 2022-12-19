import os
from http import HTTPStatus

import jwt
import pytest
from jwt import ExpiredSignatureError

from api_interview.requests.delete_user import delete_user
from api_interview.requests.get_token import request_get_token, get_token
from api_interview.requests.post_create_user import post_create_user
from dotenv import load_dotenv

from api_interview.resources.files_config import ENV_FILE_PATH, TOKEN_FILE_PATH


@pytest.fixture(scope="session")
def auth():
    # Zaciągam ścieżkę do pliku
    token_file_path = TOKEN_FILE_PATH
    # Jeżeli plik nie istnieje to puszczam request i tworzę plik z tokenem
    if not os.path.isfile(token_file_path):
        return get_token(token_file_path)
    # Jeżeli powyższy warunek nie jest spełniony to
    else:
        # Otwieram plik z tokenem
        file = open(token_file_path, "r+")
        # Przypisuję zawartość pliku do zmiennej
        token = file.read()
        # Próbuję zdecodować token oraz sprawdzić jego ważność
        try:
            jwt.decode(token, algorithms=['HS256'], options={"verify_signature": False, "verify_exp": True})
            return token
        # Jeżeli token stracił ważność to łapię błąd i puszczam request ponownie
        except ExpiredSignatureError:
            return get_token(token_file_path)


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
