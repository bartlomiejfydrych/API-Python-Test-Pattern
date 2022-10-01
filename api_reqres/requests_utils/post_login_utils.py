from api_reqres.requests_endpoints.post_login import post_login_endpoint


def post_login(email, password):
    payload = {
        "email": email,
        "password": password
    }
    r = post_login_endpoint(payload)
    return r
