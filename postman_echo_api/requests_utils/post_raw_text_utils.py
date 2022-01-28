from requests import Response

from postman_echo_api.requests_endpoints.post_raw_text import PostRawText


class PostRawTextUtils:

    @staticmethod
    def post_raw_text_payload() -> Response:
        payload = {
            "Wartość_1": "12żółć34",
            "Wartość 2": "12polska34",
            "Wartość3": "1bęc2()$%3",
        }
        r = PostRawText.post_raw_text(payload)
        return r
