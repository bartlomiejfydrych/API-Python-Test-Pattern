import requests
from requests import Response

from api_reqres.requests_endpoints.url_base import URL_BASE

url = f"{URL_BASE}login"


def post_login_endpoint(payload) -> Response:
    return requests.post(url, data=payload, timeout=1)
