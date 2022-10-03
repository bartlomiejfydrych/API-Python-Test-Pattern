import requests
from requests import Response

from api_reqres.requests_endpoints.url_base import URL_BASE


def get_resource_single(resource_id) -> Response:
    url = f"{URL_BASE}unknown/{resource_id}"
    return requests.get(url, timeout=1)
