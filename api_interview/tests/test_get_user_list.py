import os

from api_interview.requests.delete_user import delete_user
from api_interview.requests.get_token import env_authorization
from api_interview.requests.get_user_list import get_user_list
from api_interview.requests.get_version import get_version
from api_interview.requests.post_create_user import post_create_user
from api_interview.requests.put_edit_user import put_edit_user
from utils.response_show import show_response_data


def test_token():
    response = env_authorization()
    show_response_data(response)


def test_get_user_list(auth):
    response = get_user_list(auth)
    response_version = get_version(auth)
    show_response_data(response)
    show_response_data(response_version)


def test_get_user_list_add_user(auth, create_delete_user):
    response = get_user_list(auth)
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert response.status_code == 200

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct data"
    added_user = next((user for user in resp if user["id"] == create_delete_user["id"]), None)
    assert create_delete_user == added_user


def test_get_user_list_edit_user(auth, create_delete_user):
    response_put = put_edit_user(
        auth,
        create_delete_user["id"],
        username="Radim",
        age=66,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": ""}]
    )
    resp_put = response_put.json()

    response = get_user_list(auth)
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert response.status_code == 200

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct data"
    edit_user = next((user for user in resp if user["id"] == create_delete_user["id"]), None)
    assert resp_put == edit_user


def test_get_user_list_delete_user(auth):
    # Add user
    response_post = post_create_user(
        auth,
        username="Edward",
        age=44,
        admin=True,
        skills=["Chodzenie", "Pływanie"],
        city="Radom",
        street="Sokolska",
        street_number="9g",
        additional=[{"key": "Język", "value": "Angielski"}]
    )
    resp_post = response_post.json()
    user_id = resp_post["id"]
    assert response_post.status_code == 201

    # Delete user
    response_delete = delete_user(auth, user_id)
    assert response_delete.status_code == 204

    # Get user
    response = get_user_list(auth)
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert response.status_code == 200

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct data"
    deleted_user = next((user for user in resp if user["id"] == user_id), None)
    assert deleted_user is None
