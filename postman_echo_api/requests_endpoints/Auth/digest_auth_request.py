import requests
from requests import Response
from requests.auth import HTTPDigestAuth

from postman_echo_api.requests_endpoints.base_url import BaseUrl


class DigestAuthRequest:

    url = f"{BaseUrl.base_url}digest-auth"

    @staticmethod
    def digest_auth_request_positive() -> Response:
        return requests.get(DigestAuthRequest.url, auth=HTTPDigestAuth('postman', 'password'), timeout=1)

    @staticmethod
    def digest_auth_request_negative() -> Response:
        return requests.get(DigestAuthRequest.url, auth=HTTPDigestAuth('Dave', 'potato'), timeout=1)
