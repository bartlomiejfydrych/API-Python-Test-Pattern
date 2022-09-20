import requests
from requests import Response

from api_dummy.requests_endpoints.url_base import URL_BASE

url = f"{URL_BASE}create"
headers = {'user-agent': 'Chrome/105.0.0.0'}


def post_employee_endpoint(payload) -> Response:
    return requests.post(url, data=payload, headers=headers, timeout=1)
