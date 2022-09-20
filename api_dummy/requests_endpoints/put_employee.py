import requests

from api_dummy.requests_endpoints.url_base import URL_BASE

headers = {'user-agent': 'Chrome/105.0.0.0'}


def put_employee_endpoint(employee_id, payload):
    url = f"{URL_BASE}update/{employee_id}"
    return requests.put(url, data=payload, headers=headers, timeout=1)
