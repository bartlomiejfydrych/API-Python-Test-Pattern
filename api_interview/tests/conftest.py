from http import HTTPStatus

import pytest

from api_interview.requests.delete_user import delete_user
from api_interview.requests.post_create_user import post_create_user


@pytest.fixture
def create_delete_user():
    response = post_create_user(
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

    response = delete_user(user["id"])
    assert response.status_code == 204
