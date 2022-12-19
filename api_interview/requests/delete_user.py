from http import HTTPStatus

from requests import Response

from api_interview.requests.get_token import env_authorization
from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper


def delete_user(token, user_id) -> Response:
    url = f"{URL_BASE}users/{user_id}"
    # response_json_token = get_auth_token()
    # token = response_json_token["access_token"]
    auth_header = {"Authorization": f"Bearer {token}"}
    return requests_wrapper.delete(url, headers=auth_header, timeout=1)


def teardown_delete_user(token, user_id):
    url = f"{URL_BASE}users/{user_id}"
    # response_json_token = get_auth_token()
    # token = response_json_token["access_token"]
    auth_header = {"Authorization": f"Bearer {token}"}
    response = requests_wrapper.delete(url, headers=auth_header, timeout=1)
    assert response.status_code == HTTPStatus.NO_CONTENT
