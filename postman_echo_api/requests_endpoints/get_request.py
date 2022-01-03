import requests
from requests import Response

from postman_echo_api.requests_endpoints.base_url import BaseUrl


class GetRequest:

    url = f"{BaseUrl.base_url}get?foo1=bar1&foo2=bar2"

    @staticmethod
    def get_request() -> Response:
        return requests.get(GetRequest.url, timeout=1)
