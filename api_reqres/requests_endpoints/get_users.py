import requests
from requests import Response

from api_reqres.requests_endpoints.url_base import URL_BASE


def get_users(page) -> Response:
    url = f"{URL_BASE}users?page={page}"
    return requests.get(url, timeout=1)
