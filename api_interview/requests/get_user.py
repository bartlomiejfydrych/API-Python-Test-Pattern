from requests import Response

from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper


def get_user(user_id) -> Response:
    url = f"{URL_BASE}users/{user_id}"
    return requests_wrapper.get(url, timeout=1)
