from requests import Response

from api_reqres.requests_endpoints.post_create_user import post_create_user_endpoint


def post_create_user(name, job) -> Response:
    payload = {
        "name": name,
        "job": job
    }
    r = post_create_user_endpoint(payload)
    return r
