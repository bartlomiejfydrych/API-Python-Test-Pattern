import requests
from requests import Response

from api_reqres.requests_endpoints.url_base import URL_BASE

url = f"{URL_BASE}users"


def post_create_user_endpoint(payload) -> Response:
    return requests.post(url, data=payload, timeout=1)
