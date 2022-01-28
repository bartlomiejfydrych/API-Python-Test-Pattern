import requests
from requests import Response

from postman_echo_api.requests_endpoints.base_url import BaseUrl


class PostRawText:

    url = f"{BaseUrl.base_url}post"

    @staticmethod
    def post_raw_text(payload: dict) -> Response:
        return requests.post(PostRawText.url, data=payload, timeout=1)
