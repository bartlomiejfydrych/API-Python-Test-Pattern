from requests import Response

from api_reqres.requests_endpoints.post_register import post_register_endpoint


def post_register(email, password) -> Response:
    payload = {
        "email": email,
        "password": password
    }
    r = post_register_endpoint(payload)
    return r
