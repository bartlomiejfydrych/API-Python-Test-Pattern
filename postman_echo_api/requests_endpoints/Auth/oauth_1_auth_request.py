import requests
from requests import Response
from requests_oauthlib import OAuth1

from postman_echo_api.requests_endpoints.base_url import BaseUrl


class Oauth1AuthRequest:

    url = f"{BaseUrl.base_url}oauth1"

    @staticmethod
    def oauth_1_auth_request_positive() -> Response:
        auth = OAuth1("RKCGzna7bv9YD57c", "D+EdQ-gs$-%@2Nu7")
        return requests.get(Oauth1AuthRequest.url, auth=auth)

    @staticmethod
    def ouath_1_auth_request_negative() -> Response:
        auth = OAuth1("TLVHxms8nb0UF68v", "A+CbN-hf%-@$3Mv6")
        return requests.get(Oauth1AuthRequest.url, auth=auth)
