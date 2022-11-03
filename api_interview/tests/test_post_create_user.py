import json
from http import HTTPStatus

from jsonschema.validators import validate

from api_interview.requests.delete_user import teardown_delete_user
from api_interview.requests.get_user import get_user
from api_interview.requests.post_create_user import post_create_user
from api_interview.tests_data.data_post_create_user import schema_post_create_user, CreateUserDTO, \
    response_validation_error_username, response_validation_error_age, response_validation_error_age_integer
from utils.response_show import show_response_data
from utils.tests_info import show_tests


# def test_create_user_show():
#     response = post_create_user(
#         username="Moko",
#         age=30,
#         admin=True,
#         skills=["Chodzenie"],
#         city="Wąchock",
#         street="Oświęcimska",
#         street_number="5a",
#         additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
#     )
#     show_response_data(response)
#     resp = response.json()
#     try:
#         user_id = resp["id"]
#     finally:
#         teardown_delete_user(resp["id"])


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

    try:
        # Pobranie ID usera
        user_id = resp["id"]

        # ----------------------
        # Basic response tests:
        # ----------------------
        test_a = "Response should have status code 201"
        assert response.status_code == 201

        test_b = "Response should have correct Schema"
        validate(resp, schema_post_create_user)

        test_c = "Response should have correct Data Transfer Object (DTO)"
        CreateUserDTO.validate(resp)

        # ----------------------
        # Detailed tests:
        # ----------------------
        test_1 = "Add user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Added user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(resp["id"])


def test_create_user_admin_false():
    response = post_create_user(
        username="Andrzej",
        age=8,
        admin=False,
        skills=["Walka"],
        city="Płock",
        street="Kombatanów",
        street_number="21g",
        additional=[{"key": "Może i jest mały", "value": "Ale pachnie jak duży"}]
    )
    resp = response.json()
    resp_no_id = response.json()

    try:
        # Pobranie ID usera
        user_id = resp["id"]

        # ----------------------
        # Basic response tests:
        # ----------------------
        test_a = "Response should have status code 201"
        assert response.status_code == 201

        test_b = "Response should have correct Schema"
        validate(resp, schema_post_create_user)

        test_c = "Response should have correct Data Transfer Object (DTO)"
        CreateUserDTO.validate(resp)

        # ----------------------
        # Detailed tests:
        # ----------------------
        test_1 = "Add user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Added user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(resp["id"])


def test_create_user_more_skills_and_additional_true():
    response = post_create_user(
        username="Konrad",
        age=100,
        admin=True,
        skills=["Jedzienie", "Spanie", "Picie"],
        city="Ruda Śląska",
        street="Kubackiego",
        street_number="111x",
        additional=[
            {
                "key": "Papier",
                "value": "Toaletowy"
            },
            {
                "key": "Zaprawa",
                "value": "Murarska"
            },
            {
                "key": "Inka",
                "value": "Waniliowa"
            },
        ]
    )
    resp = response.json()
    resp_no_id = response.json()

    try:
        # Pobranie ID usera
        user_id = resp["id"]

        # ----------------------
        # Basic response tests:
        # ----------------------
        test_a = "Response should have status code 201"
        assert response.status_code == 201

        test_b = "Response should have correct Schema"
        validate(resp, schema_post_create_user)

        test_c = "Response should have correct Data Transfer Object (DTO)"
        CreateUserDTO.validate(resp)

        # ----------------------
        # Detailed tests:
        # ----------------------
        test_1 = "Add user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Added user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(resp["id"])


def test_create_user_more_skills_and_additional_false():
    response = post_create_user(
        username="Adrian",
        age=50,
        admin=False,
        skills=["Leżing", "Plażing", "Smażing"],
        city="Olsztyn",
        street="Bimbrowskiego",
        street_number="1c",
        additional=[
            {
                "key": "Woda kolońska",
                "value": "Leśny dzik"
            },
            {
                "key": "Komputer stacjonarny",
                "value": "Tibia 7.6"
            },
            {
                "key": "Płatki śniadaniowe",
                "value": "Kuleczki Nesquik"
            },
        ]
    )
    resp = response.json()
    resp_no_id = response.json()

    try:
        # Pobranie ID usera
        user_id = resp["id"]

        # ----------------------
        # Basic response tests:
        # ----------------------
        test_a = "Response should have status code 201"
        assert response.status_code == 201

        test_b = "Response should have correct Schema"
        validate(resp, schema_post_create_user)

        test_c = "Response should have correct Data Transfer Object (DTO)"
        CreateUserDTO.validate(resp)

        # ----------------------
        # Detailed tests:
        # ----------------------
        test_1 = "Add user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Added user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(resp["id"])


# --------------------------------------------------------------------------------------------------------------
# NEGATIVE TESTS:
# --------------------------------------------------------------------------------------------------------------
def test_create_user_try_add_the_same_user():
    response_one = post_create_user(
        username="Wacław",
        age=21,
        admin=False,
        skills=["Klaskanie"],
        city="Bydgoszcz",
        street="Grzybowa",
        street_number="4g",
        additional=[{"key": "Papryczka", "value": "Chili"}]
    )
    assert response_one.status_code == HTTPStatus.CREATED
    resp_one = response_one.json()

    try:
        response = post_create_user(
            username="Wacław",
            age=21,
            admin=False,
            skills=["Klaskanie"],
            city="Bydgoszcz",
            street="Grzybowa",
            street_number="4g",
            additional=[{"key": "Papryczka", "value": "Chili"}]
        )
        resp = response.json()

        # ----------------------
        # Basic response tests:
        # ----------------------
        test_a = "Response should have status code 201"
        assert response.status_code == 400

        # ----------------------
        # Detailed tests:
        # ----------------------
        test_1 = "Response should have correct error message"
        assert resp["status"] == 400
        assert resp["message"] == "Provided username 'Wacław' already exists"

        # Wyświetlanie testów:
        show_tests(test_a, test_1)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(resp_one["id"])


# ----------------------
# USERNAME:
# ----------------------
def test_create_user_username_empty():
    response = post_create_user(
        username="",
        age=91,
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp["status"] == 400
    assert resp["message"] == "Provided username 'Wacław' already exists"

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_username_null():
    response = post_create_user(
        username=None,
        age=91,
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_username

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_username_only_spaces():
    response = post_create_user(
        username="      ",
        age=91,
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_username

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ----------------------
# AGE:
# ----------------------
def test_create_user_age_null():
    response = post_create_user(
        username="Kordian",
        age=None,
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_age_minus():
    response = post_create_user(
        username="Kordian",
        age=-100,
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_age_dot():
    response = post_create_user(
        username="Mokebe",
        age=24.2,
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_age_comma():
    response = post_create_user(
        username="Johan",
        age="31,9",
        admin=False,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age_integer

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ----------------------
# ADMIN:
# ----------------------
def test_create_user_without_admin():
    response = post_create_user(
        username="Brajan",
        age=55,
        admin=None,
        skills=["Klikanie"],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    # TODO: Zapytać Dawida czy w takiej metodzie można jakoś zrobić, że nie podajemy jakiejś wartości
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age_integer

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ----------------------
# SKILLS:
# ----------------------
def test_create_user_skills_empty_array():
    response = post_create_user(
        username="Brajan",
        age=55,
        admin=False,
        skills=[],
        city="Otwock",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age_integer

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_city_empty():
    response = post_create_user(
        username="User1",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == response_validation_error_age_integer

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_city_null():
    response = post_create_user(
        username="User2",
        age=55,
        admin=False,
        skills=["Latanie"],
        city=None,
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "city"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_city_only_spaces():
    response = post_create_user(
        username="User3",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="      ",
        street="Jabłkowa",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "city"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_street_empty():
    response = post_create_user(
        username="User4",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="Karpacz",
        street="",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "city"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_street_null():
    response = post_create_user(
        username="User4",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="Karpacz",
        street=None,
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "street"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_street_only_spaces():
    response = post_create_user(
        username="User5",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="Karpacz",
        street="      ",
        street_number="9a",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "street"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_street_number_empty():
    response = post_create_user(
        username="User6",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="Karpacz",
        street="Serowa",
        street_number="",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "street"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_street_number_null():
    response = post_create_user(
        username="User6",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="Karpacz",
        street="Serowa",
        street_number=None,
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "street_number"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_create_user_location_street_number_only_spaces():
    response = post_create_user(
        username="User7",
        age=55,
        admin=False,
        skills=["Latanie"],
        city="Karpacz",
        street="Serowa",
        street_number="   ",
        additional=[
            {
                "key": "Pilot telewizora",
                "value": "Kosz na śmieci"
            }
        ]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    # TODO: Poprawić testy
    test_a = "Response should have status code 422"
    assert response.status_code == 422

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp == {
        "detail": [
            {
                "loc": [
                    "body",
                    "location",
                    "street_number"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


'''
ZNALEZIONE DEFEKTY:
1. Nie można utworzyć użytkownika z "admin": True
2. Endpoint DELETE nie usuwa użytkownika, mimo, że sprawia wrażenie jakby to robił
3. Można utworzyć użytkownika z pustą "" nazwą
4. Można utworzyć użytkownika z nazwą z samych spacji "      "
5. Można dodać użytkownika z ujemną liczbą lat
6?. Można podać wiek z kropką. Niby jest ucinana i jest okej, ale chyba nie powinno takie coś przechodzić
7. Przechodzi pusta tablica SKILLS.
8. Przechodzi pusty string "" dla Location->City
9. Przechodzi string z samych spacji "      " dla Location->City
10. Przechodzi pusty string "" dla Location->Street
11. Przechodzi string z samych spacji "      " dla Location->Street
12. Przechodzi pusty string "" dla Location->street_number
13. Przechodzi string z samych spacji "      " dla Location->street_number

PLAN TESTÓW:
[✓]Utworzenie użytkownika z jedną umiejętnością i jednym obiektem "additional" oraz admin true.
[✓]Utworzenie użytkownika z jedną umiejętnością i jednym obiektem "additional" oraz admin false.
[✓]Utworzenie użytkownika z trzema umiejętnościami i trzema obiektami "additional" oraz admin true.
[✓]Utworzenie użytkownika z trzema umiejętnościami i trzema obiektami "additional" oraz admin false.
    TESTY NEGATYWNE:
        [✓]Czy nie da się drugi raz dodać takiego samego użytkownika
            USERNAME:
                [✓]Puste ""
                [✓]Null
                [✓]Same spacje
                [>]Integer (przeszło, zazwyczaj integer jest zmieniany na string w razie czego, czy jest sens takie coś sprawdzać?)
                [>]Za długie (nie ma limitu znaków więc test odpada)
            AGE:
                [>]String (przeszło, chyba to samo co z integer->string, test chyba nie ma sensu)
                [✓]Null/None
                [✓]Z minusem
                [?]Po kropce
                [✓]Po przecinku
                [>]Za duże 9999 (nie ma limitu znaków więc test odpada)
            ADMIN:
                [?]Brak
            SKILLS:
                [✓]Pusta tablica
                [>]Tablica integerów (integery są zamieniane na stringi, więc test raczej bez sensu)
                [?]Brak
                [>]Za dużo (nie ma limitu elementów tablicy więc test odpada)
            LOCATION:
                CITY:
                    [✓]Puste ""
                    [✓]Null
                    [✓]Same spacje
                STREET:
                    [✓]Puste ""
                    [✓]Null
                    [✓]Same spacje
                STREET_NUMBER:
                    [✓]Puste ""
                    [✓]Null
                    [✓]Same spacje
            ADDITIONAL:
                Pusta tablica
                [?] Brak
                Inny "key"
                Inny "value"
                Pusty "key"
                Pusty "value"
'''
