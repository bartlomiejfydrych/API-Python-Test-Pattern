import json
from typing import Optional


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
    payload_cut(21)


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