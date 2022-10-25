from http import HTTPStatus

from requests import Response

from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper


def delete_user(user_id) -> Response:
    url = f"{URL_BASE}users/{user_id}"
    return requests_wrapper.delete(url, timeout=1)


def teardown_delete_user(user_id):
    url = f"{URL_BASE}users/{user_id}"
    response = requests_wrapper.delete(url, timeout=1)
    assert response.status_code == HTTPStatus.NO_CONTENT
