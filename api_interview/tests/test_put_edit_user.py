import json

from jsonschema.validators import validate

from api_interview.requests.delete_user import teardown_delete_user
from api_interview.requests.get_user import get_user
from api_interview.requests.post_create_user import post_create_user
from api_interview.requests.put_edit_user import put_edit_user
from api_interview.tests_data.data_post_create_user import schema_post_create_user, CreateUserDTO
from utils.response_show import show_response_data
from utils.tests_info import show_tests


def test_edit_user_admin_true(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
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
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


def test_edit_user_admin_false():
    response_post = post_create_user(
        username="Adam1",
        age=29,
        admin=True,
        skills=["Chodzenie"],
        city="City1",
        street="Street1",
        street_number="1a",
        additional=[{"key": "Frytki", "value": "Z keczupem"}]
    )
    assert response_post.status_code == 201
    resp_post = response_post.json()
    user_id = resp_post["id"]

    try:
        response = put_edit_user(
            user_id,
            username="AdamE",
            age=30,
            admin=False,
            skills=["ChodzenieE"],
            city="City1E",
            street="Street1E",
            street_number="1e",
            additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
        )
        show_response_data(response)
        resp = response.json()
        resp_no_id = response.json()

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
        test_1 = "Edited user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Edited user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(user_id)


def test_edit_user_more_skills(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="AdamE",
        age=30,
        admin=False,
        skills=["Latanie", "Śmianie", "Szczekanie"],
        city="City1E",
        street="Street1E",
        street_number="1e",
        additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


def test_edit_user_more_additional(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="AdamE",
        age=30,
        admin=False,
        skills=["Oddychanie"],
        city="City1E",
        street="Street1E",
        street_number="1e",
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
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


def test_edit_user_one_skills():
    response_post = post_create_user(
        username="Adam1",
        age=29,
        admin=True,
        skills=["Chodzenie", "Mlaskanie", "Rodzenie"],
        city="City1",
        street="Street1",
        street_number="1a",
        additional=[{"key": "Frytki", "value": "Z keczupem"}]
    )
    assert response_post.status_code == 201
    resp_post = response_post.json()
    user_id = resp_post["id"]

    try:
        response = put_edit_user(
            user_id,
            username="AdamE",
            age=30,
            admin=False,
            skills=["ChodzenieE"],
            city="City1E",
            street="Street1E",
            street_number="1e",
            additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
        )
        show_response_data(response)
        resp = response.json()
        resp_no_id = response.json()

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
        test_1 = "Edited user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Edited user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(user_id)


def test_edit_user_one_additional():
    response_post = post_create_user(
        username="Adam1",
        age=29,
        admin=True,
        skills=["Chodzenie"],
        city="City1",
        street="Street1",
        street_number="1a",
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
    assert response_post.status_code == 201
    resp_post = response_post.json()
    user_id = resp_post["id"]

    try:
        response = put_edit_user(
            user_id,
            username="AdamE",
            age=30,
            admin=False,
            skills=["ChodzenieE"],
            city="City1E",
            street="Street1E",
            street_number="1e",
            additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
        )
        show_response_data(response)
        resp = response.json()
        resp_no_id = response.json()

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
        test_1 = "Edited user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Edited user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(user_id)


# --------------------------------------------------------------------------------------------------------------
# NEGATIVE TESTS:
# --------------------------------------------------------------------------------------------------------------
def test_edit_user_on_already_exist_user(create_delete_user):
    response_post = post_create_user(
        username="Adam1",
        age=29,
        admin=True,
        skills=["Chodzenie"],
        city="City1",
        street="Street1",
        street_number="1a",
        additional=[{"key": "Blok", "value": "Techniczny"}]
    )
    assert response_post.status_code == 201
    resp_post = response_post.json()
    user_id = resp_post["id"]

    try:
        response = put_edit_user(
            user_id,
            username="Adrian PUTa3",
            age=41,
            admin=False,
            skills=["Oddychanie"],
            city="Kraków",
            street="Partyzantów",
            street_number="41c",
            additional=[{"key": "Broń", "value": "Miecz"}]
        )
        show_response_data(response)
        resp = response.json()
        resp_no_id = response.json()

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
        test_1 = "Edited user should have correct data"
        response_body = json.loads(response.request.body.decode('utf-8'))
        del resp_no_id["id"]
        assert resp_no_id == response_body

        test_2 = "Edited user should be visible"
        response_get = get_user(user_id)
        resp_get = response_get.json()
        assert resp == resp_get

        # Wyświetlanie testów:
        show_tests(test_a, test_b, test_c, test_1, test_2)

    finally:
        # ----------------------
        # TEARDOWN:
        # ----------------------
        teardown_delete_user(user_id)


# ------------------------------------------------------
# USERNAME:
# ------------------------------------------------------
def test_edit_user_username_empty(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="",
        age=30,
        admin=False,
        skills=["Latanie", "Śmianie", "Szczekanie"],
        city="City1E",
        street="Street1E",
        street_number="1e",
        additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


def test_edit_user_username_null(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username=None,
        age=30,
        admin=False,
        skills=["Latanie", "Śmianie", "Szczekanie"],
        city="City1E",
        street="Street1E",
        street_number="1e",
        additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "username"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_edit_user_username_only_spaces(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="      ",
        age=30,
        admin=False,
        skills=["Latanie", "Śmianie", "Szczekanie"],
        city="City1E",
        street="Street1E",
        street_number="1e",
        additional=[{"key": "FrytkiE", "value": "Z keczupemE"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


# ------------------------------------------------------
# AGE:
# ------------------------------------------------------
def test_edit_user_age_null(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=None,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "age"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_edit_user_age_minus(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=-15,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


def test_edit_user_age_dot(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=12.34,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()
    resp_no_id = response.json()

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
    test_1 = "Edited user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Edited user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


def test_edit_user_age_comma(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age="43,21",
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "age"
                ],
                "msg": "value is not a valid integer",
                "type": "type_error.integer"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ------------------------------------------------------
# ADMIN:
# ------------------------------------------------------
def test_edit_user_admin_null(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=45,
        admin=None,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "admin"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ------------------------------------------------------
# SKILLS:
# ------------------------------------------------------
def test_edit_user_skills_empty_array(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=45,
        admin=False,
        skills=[],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "skills"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_edit_user_skills_null_in_array(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=45,
        admin=False,
        skills=None,
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "skills"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ------------------------------------------------------
# LOCATION - CITY:
# ------------------------------------------------------
def test_edit_user_location_city_empty(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


def test_edit_user_location_city_null(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city=None,
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


def test_edit_user_location_city_only_spaces(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="      ",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


# ------------------------------------------------------
# LOCATION - STREET:
# ------------------------------------------------------
def test_edit_user_location_street_empty(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


def test_edit_user_location_street_null(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street=None,
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


def test_edit_user_location_street_only_spaces(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="      ",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


# ------------------------------------------------------
# LOCATION - STREET_NUMBER:
# ------------------------------------------------------
def test_edit_user_location_street_number_empty(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


def test_edit_user_location_street_number_null(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number=None,
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


def test_edit_user_location_street_number_only_spaces(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="      ",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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


# ------------------------------------------------------
# ADDITIONAL:
# ------------------------------------------------------
def test_edit_user_additional_empty_array(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[]
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "additional"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


def test_edit_user_additional_null_array(create_delete_user):
    response = put_edit_user(
        create_delete_user["id"],
        username="Bogdan",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=None
    )
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
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
                    "additional"
                ],
                "msg": "none is not an allowed value",
                "type": "type_error.none.not_allowed"
            }
        ]
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)


# ------------------------------------------------------
# ADDITIONAL - KEY:
# ------------------------------------------------------
# def test_edit_user_additional_key_empty(create_delete_user):
# def test_edit_user_additional_key_null(create_delete_user):
# def test_edit_user_additional_key_only_spaces(create_delete_user):


# ------------------------------------------------------
# ADDITIONAL - VALUE:
# ------------------------------------------------------
# def test_edit_user_additional_value_empty(create_delete_user):
# def test_edit_user_additional_value_null(create_delete_user):
# def test_edit_user_additional_value_only_spaces(create_delete_user):


'''
TODO: DODAĆ FAKER NA USERNAME
DEFEKTY:
1. Endpoint PUT nie jest w stanie edytować obiektu "additional".
2. Można zmienić dane na dane już istniejącego użytkownika.
3. Można zmienić 'username' na pusty string "".
4. Można zmienić 'username' na same spacje string "      ".
5. Można zmienić 'age' na liczbę ujemną -15.
6. ? Gdy w 'age' wpiszemy 12.34 to to przechodzi, ale liczby po kropce są ucinane. Chyba takie coś wcale nie powinno przechodzić.
7. W "skills" możemy umieścić pustą tablicę [].
8. Dla "location.city" przechodzi pusty String "".
9. Dla "location.city" przechodzi String z samych spacji "      ".
10. Dla "location.street" przechodzi pusty String "".
11. Dla "location.street" przechodzi String z samych spacji "      ".
12. Dla "location.street_number" przechodzi pusty String "".
13. Dla "location.street_number" przechodzi String z samych spacji "      ".
14. Dla "additional" przechodzi pusta tablica [].

PLAN TESTÓW:
[✓]Zmiana ("admin": false -> true)
[✓]Dodać usera z ("admin": true) -> zmienić na ("admin": false)
[✓]Z jeden "skills" -> zmienić na kilka "skills"
[✓]Z jeden "additional" -> zmienić na kilka "additional"
[✓]Dodać usera z kilkoma "skills" -> zmienić na jeden
[✓]Dodać usera z kilkoma "additional" -> zmienić na jeden
    TESTY NEGATYWNE:
        [✓]Dodać usera + zmienić dane usera na dane istniejącego już usera
            USERNAME:
                [✓]Puste ""
                [✓]Null/None
                [✓]Same spacje
            AGE:
                [✓]Null/None
                [✓]Z minusem
                [✓]Po kropce
                [✓]Po przecinku
            ADMIN:
                [✓]Null/None - Brak
            SKILLS:
                [✓]Pusta tablica
                [✓]Null/None w tablicy
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
                [✓]Pusta tablica
                [✓]Null/None tablica
                    KEY:
                        Puste ""
                        Null
                        Same spacje
                    VALUE:
                        Puste ""
                        Null
                        Same spacje
'''
