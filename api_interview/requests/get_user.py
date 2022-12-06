from requests import Response

from api_interview.requests.get_token import get_auth_token
from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper


def get_user(user_id) -> Response:
    url = f"{URL_BASE}users/{user_id}"
    response_json_token = get_auth_token()
    token = response_json_token["access_token"]
    auth_header = {"Authorization": f"Bearer {token}"}
    return requests_wrapper.get(url, headers=auth_header, timeout=1)
