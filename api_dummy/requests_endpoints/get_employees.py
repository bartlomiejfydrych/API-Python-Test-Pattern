import requests
from requests import Response

from api_dummy.requests_endpoints.url_base import URL_BASE

url = f"{URL_BASE}employees"
headers = {'user-agent': 'Chrome/105.0.0.0'}


def get_employees_endpoint() -> Response:
    return requests.get(url, headers=headers, timeout=1)


"""
Dla tego API nie jest możliwe puszczanie requestów dla 'user-agent=python',
dlatego trzeba było ten header podmienić na jedną z przeglądarek:
{'user-agent': 'Chrome/105.0.0.0'}
Przykład pozostałych:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
"""
