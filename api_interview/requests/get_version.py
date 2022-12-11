from requests import Response

from api_interview.requests.get_token import get_auth_token
from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper

url = f"{URL_BASE}version"


def get_version(token) -> Response:
    # response_json_token = get_auth_token()
    # token = response_json_token["access_token"]
    auth_header = {"Authorization": f"Bearer {token}"}
    return requests_wrapper.get(url, headers=auth_header, timeout=1)
