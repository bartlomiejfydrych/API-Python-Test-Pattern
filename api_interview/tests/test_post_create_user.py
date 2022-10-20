import json

from jsonschema.validators import validate

from api_interview.requests.post_create_user import post_create_user
from api_interview.tests_data.data_post_create_user import schema_post_create_user, CreateUserDTO
from utils.tests_info import show_tests


def test_post_create_user_true_admin():
    response = post_create_user(
        username="Marcin",
        age=30,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    resp = response.json()

    # Pobranie ID usera
    user_id = resp["id"]

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert response.status_code == 200

    test_b = "Response should have correct Schema"
    validate(resp, schema_post_create_user)

    test_c = "Response should have correct Data Transfer Object (DTO)"
    CreateUserDTO.validate(resp)

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Add user should have correct data"
    response_body = json.loads(response.request.body.decode('uft-8'))
    del resp["id"]
    assert resp == response_body

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_c, test_1)


'''
PLAN TESTÓW:
Utworzenie użytkownika z jedną umiejętnością i jednym obiektem "additional" oraz admin true.
Utworzenie użytkownika z jedną umiejętnością i jednym obiektem "additional" oraz admin false.
Utworzenie użytkownika z trzema umiejętnościami i trzema obiektami "additional" oraz admin true.
Utworzenie użytkownika z trzema umiejętnościami i trzema obiektami "additional" oraz admin false.
    TESTY NEGATYWNE:
        Czy nie da się drugi raz dodać takiego samego użytkownika
        USERNAME:
Puste ""
Null
Same spacje
Integer
Za długie (nie ma limitu znaków więc test odpada)
AGE:
String
Brak
Z minusem
Po przecinku
Za duże 9999 (nie ma limitu znaków więc test odpada)
ADMIN:
String
Integer
Brak
SKILLS:
Pusta tablica
Brak
Za dużo (nie ma limitu znaków więc test odpada)
Tablica integerów
LOCATION:

'''
