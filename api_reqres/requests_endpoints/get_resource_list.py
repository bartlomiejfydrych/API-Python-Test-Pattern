import requests
from requests import Response

from api_reqres.requests_endpoints.url_base import URL_BASE

url = f"{URL_BASE}unknown"


def get_resource_list() -> Response:
    return requests.get(url, timeout=1)
