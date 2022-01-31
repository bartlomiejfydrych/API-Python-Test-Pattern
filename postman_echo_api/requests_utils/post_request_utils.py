from requests import Response

from postman_echo_api.requests_endpoints.post_request import PostRequest
from postman_echo_api.resources.files_config import POST_REQUEST_TEXT_FILE_PATH, POST_REQUEST_GRAPHIC_FILE_PATH


class PostRequestUtils:

    @staticmethod
    def post_form_data() -> Response:
        payload = {
            "Wartość_1": "12żółć34",
            "Wartość 2": "12polska34",
            "Wartość3": "1bęc2()$%3",
        }
        r = PostRequest.post_request(payload)
        return r

    @staticmethod
    def post_raw_text() -> Response:
        payload = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus efficitur ante arcu, " \
                  "nec gravida libero varius at. Curabitur rhoncus purus."
        r = PostRequest.post_request(payload)
        return r

    @staticmethod
    def post_args() -> Response:
        params_args = {
            "status": "positive",
            "photos": "no duplicate",
            "region": "HKS 122",
            "ph": "Albert Gizmo"
        }
        r = PostRequest.post_request_args(params_args)
        return r

    @staticmethod
    def post_file() -> Response:
        file = {
            "file": open(POST_REQUEST_GRAPHIC_FILE_PATH, "rb")
        }
        r = PostRequest.post_request_file(file)
        return r
