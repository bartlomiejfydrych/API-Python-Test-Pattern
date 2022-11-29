from requests import Response

from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper

url = f"{URL_BASE}users"


def get_user_list() -> Response:
    return requests_wrapper.get(url, timeout=1)
