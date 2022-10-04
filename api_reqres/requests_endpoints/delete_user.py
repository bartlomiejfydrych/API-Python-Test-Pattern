import requests
from requests import Response

from api_reqres.requests_endpoints.url_base import URL_BASE


def delete_user(number) -> Response:
    url = f"{URL_BASE}users/{number}"
    return requests.delete(url, timeout=1)
