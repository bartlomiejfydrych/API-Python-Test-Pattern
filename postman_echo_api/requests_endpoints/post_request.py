import requests
from requests import Response

from postman_echo_api.requests_endpoints.base_url import BaseUrl


class PostRequest:

    url = f"{BaseUrl.base_url}post"

    @staticmethod
    def post_request(payload) -> Response:
        return requests.post(PostRequest.url, data=payload, timeout=1)

    @staticmethod
    def post_request_args(params_args) -> Response:
        return requests.post(PostRequest.url, params=params_args, timeout=1)
