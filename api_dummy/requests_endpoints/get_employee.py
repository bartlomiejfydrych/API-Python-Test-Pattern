import requests
from requests import Response

from api_dummy.requests_endpoints.url_base import URL_BASE

headers = {'user-agent': 'Chrome/105.0.0.0'}


def get_employee(employee_id) -> Response:
    url = f"{URL_BASE}employee/{employee_id}"
    return requests.get(url, headers=headers, timeout=1)
