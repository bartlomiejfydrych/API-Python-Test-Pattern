import requests
from requests import Response

from postman_echo_api.requests_endpoints.base_url import BaseUrl


class BasicAuthRequest:

    url = f"{BaseUrl.base_url}basic-auth"

    @staticmethod
    def basic_auth_request_positive() -> Response:
        return requests.get(BasicAuthRequest.url, auth=("postman", "password"), timeout=1)

    @staticmethod
    def basic_auth_request_negative() -> Response:
        return requests.get(BasicAuthRequest.url, auth=("Dave", "Potato"), timeout=1)


"""
Inna forma zapisu:
>>> from requests.auth import HTTPBasicAuth
>>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
<Response [200]>
"""
