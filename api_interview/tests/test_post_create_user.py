import json

from jsonschema.validators import validate

from api_interview.requests.delete_user import delete_user
from api_interview.requests.get_user import get_user
from api_interview.requests.post_create_user import post_create_user
from api_interview.tests_data.data_post_create_user import schema_post_create_user, CreateUserDTO
from utils.response_show import show_response_data
from utils.tests_info import show_tests


def test_create_user_show():
    response = post_create_user(
        username="Bogdan",
        age=30,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()
    user_id = resp["id"]
    response_delete = delete_user(user_id)
    assert response_delete.status_code == 204


def test_create_user_admin_true():
    response = post_create_user(
        username="Bogdan",
        age=30,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    resp = response.json()
    resp_no_id = response.json()

    # Pobranie ID usera
    user_id = resp["id"]

    # BASIC RESPONSE TESTS:
    test_a = "Response should have status code 201"
    assert response.status_code == 201
    test_b = "Response should have correct Schema"
    validate(resp, schema_post_create_user)
    test_c = "Response should have correct Data Transfer Object (DTO)"
    CreateUserDTO.validate(resp)

    # DETAILED TESTS:
    test_1 = "Add user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body
    test_2 = "Added user should be visible"
    response_get = get_user(user_id)
    resp_get = response_get.json()
    assert resp == resp_get

    # CLEANUP:
    response_delete = delete_user(user_id)
    assert response_delete.status_code == 204

    # WYŚWIETLANIE TESTÓW:
    show_tests(test_a, test_b, test_c, test_1, test_2)


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
