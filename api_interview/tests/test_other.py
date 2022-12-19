import json
import os
from base64 import b64decode
from typing import Optional

import jwt
from dotenv import load_dotenv
from jwt import ExpiredSignatureError

from api_interview.requests.get_token import request_get_token
from api_interview.resources.files_config import ENV_FILE_PATH, TOKEN_FILE_PATH


def test_payload_cut():
    def payload_cut(
            # Żeby nam mnie podkreślało 'None' to dla opcjonalnych parametrów piszemy <parametr: Optional[str]>
            remove_none: bool,
            username: Optional[str],
            age: int,
            admin: bool,
            skills: list[str],
            city: str,
            street: str,
            street_number: str,
            additional: list[dict]
    ):
        payload = {
            "username": username,
            "age": age,
            "admin": admin,
            "skills": skills,
            "location": {
                "city": city,
                "street": street,
                "street_number": street_number
            },
            "additional": additional
        }

        if remove_none:
            for payload_key in list(payload):
                if payload[payload_key] is None:
                    del payload[payload_key]

        payload_json = json.dumps(payload, ensure_ascii=False, indent=4)
        print(f"\n{payload_json}")

    # ----------------------------------------------
    # Sprawdzenie pełnego payloadu:
    # ----------------------------------------------
    print("\n"
          "\n-------------------------------------------------------"
          "\nWyświetlenie całego payloadu"
          "\n-------------------------------------------------------")
    payload_cut(
        remove_none=False,
        username="Bartek",
        age=45,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street="Opolska",
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # ----------------------------------------------
    # Sprawdzenie usuwania parametrów payloadu:
    # ----------------------------------------------

    # Usunięcie username:
    print("\nUsunięcie [username]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username=None,
        age=45,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street="Opolska",
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie age:
    print("\nUsunięcie [age]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=None,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street="Opolska",
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie admin:
    print("\nUsunięcie [admin]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=45,
        admin=None,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street="Opolska",
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie skills:
    print("\nUsunięcie [skills]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=45,
        admin=True,
        skills=None,
        city="Opole",
        street="Opolska",
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie city:
    print("\nUsunięcie [city]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=45,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city=None,
        street="Opolska",
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie street:
    print("\nUsunięcie [street]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=45,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street=None,
        street_number="90b",
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie street_number:
    print("\nUsunięcie [street_number]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=45,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street="Opolska",
        street_number=None,
        additional=[
            {
                "keyOne": "Value one"
            },
            {
                "keyTwo": "Value two"
            }
        ]
    )

    # Usunięcie additional:
    print("\nUsunięcie [additional]-------------------------------------------------------")
    payload_cut(
        remove_none=True,
        username="Bartek",
        age=45,
        admin=True,
        skills=[
            "Pływanie",
            "Chodzenie"
        ],
        city="Opole",
        street="Opolska",
        street_number="90b",
        additional=None
    )

    # Na pozostałe próby:
    print("\nPozostałe próby-------------------------------------------------------")


def test_token():
    def auth():
        # Zaciągam ścieżkę do pliku
        token_file_path = TOKEN_FILE_PATH
        # Jeżeli plik nie istnieje to puszczam request i tworzę plik z tokenem
        if not os.path.isfile(token_file_path):
            load_dotenv(ENV_FILE_PATH)
            username = os.getenv("USER_USERNAME")
            password = os.getenv("USER_PASSWORD")
            response = request_get_token(username, password)
            assert response.status_code == 200
            response_json = response.json()
            token = response_json["access_token"]
            file = open(token_file_path, "r+")
            file.write(token)
            file.close()
            return token
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
                load_dotenv(ENV_FILE_PATH)
                username = os.getenv("USER_USERNAME")
                password = os.getenv("USER_PASSWORD")
                response = request_get_token(username, password)
                assert response.status_code == 200
                response_json = response.json()
                token = response_json["access_token"]
                file = open(token_file_path, "r+")
                file.write(token)
                file.close()
                return token

            # # Dekoduję token i zapisuję jego parametry do zmiennej
            # token_decode = jwt.decode(token, algorithms=['HS256'], options={"verify_signature": False, "verify_exp": True})
            # # Zapisuję sobie jego czas wygaśnięcia do zmiennej
            # token_expirie_time = token_decode['exp']
            # print(token_decode['exp'])


        # file = open(TOKEN_FILE_PATH, "r+")
        # load_dotenv(ENV_FILE_PATH)
        # username = os.getenv("USER_USERNAME")
        # password = os.getenv("USER_PASSWORD")
        # response = get_token(username, password)
        # assert response.status_code == 200
        # response_json = response.json()
        # token = response_json["access_token"]
        # file.truncate()
        # file.write(token)
        # file.close()
        # return token

    print(auth())


# Stare auth():
# def auth():
#     load_dotenv(ENV_FILE_PATH)
#     username = os.getenv("USER_USERNAME")
#     password = os.getenv("USER_PASSWORD")
#     response = request_get_token(username, password)
#     assert response.status_code == 200
#     response_json = response.json()
#     token = response_json["access_token"]
#     return token


"""
# Poprzedni kod pisany na stronce:

    def sendRequest(
            remove_none: bool,
            name: str,
            surname: str,
            age: int,
            hobby: str
    ):
        payload = {
            "name": name,
            "surname": surname,
            "age": age,
            "hobby": hobby
        }
        if remove_none == True:
            for i in list(payload):
                if payload[i] is None:
                    del payload[i]

        print(payload)

    # Sprawdzenie pełnego payloadu:
    sendRequest(False, "Bogdan", "Nowacki", 29, "Bieganie")

    # Sprawdzenie IF'ów na usuwanie:
    sendRequest(True, None, "Nazwisko", 30, "Hobby")
    sendRequest(True, "Imię", None, 30, "Hobby")
    sendRequest(True, "Imię", "Nazwisko", None, "Hobby")
    sendRequest(True, "Imię", "Nazwisko", 30, None)
"""