import json

from jsonschema.validators import validate

from api_interview.requests.get_user import get_user
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
    test_1 = "Add user should have correct data"
    response_body = json.loads(response.request.body.decode('utf-8'))
    del resp_no_id["id"]
    assert resp_no_id == response_body

    test_2 = "Added user should be visible"
    response_get = get_user(create_delete_user.user["id"])
    resp_get = response_get.json()
    assert resp == resp_get

    # Wyświetlanie testów:
    show_tests(test_a, test_b, test_c, test_1, test_2)


"""
DEFEKTY:
1. Endpoint PUT nie jest w stanie edytować obiektu "additional".
"""