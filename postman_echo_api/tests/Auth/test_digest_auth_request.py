from jsonschema.validators import validate

from Auth.data_basic_digest_auth_request import DataBasicDigestAuthRequest
from postman_echo_api.requests_endpoints.Auth.digest_auth_request import DigestAuthRequest
from utils.response_info import ResponseInfo
from utils.response_show import ResponseShow


# def test_digest_auth_request_show():
#     r = DigestAuthRequest.digest_auth_request_negative()
#     # ResponseShow.show_r(r)
#     # ResponseShow.show_optional(r)
#     ResponseShow.show_bad_json(r)


def test_digest_auth_request_positive():

    # Prepare response:
    r = DigestAuthRequest.digest_auth_request_positive()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response tests:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataBasicDigestAuthRequest.basic_auth_request_schema), "Response should have correct Schema"

    # Detailed tests
    info = "Response should return a valid confirmation of authorization"
    assert rj["authenticated"] is True, info


def test_digest_auth_request_negative():

    # Prepare response:
    r = DigestAuthRequest.digest_auth_request_negative()
    ResponseInfo.log_extra_response_info(r)
    rt = r.text

    # Basic response tests:
    assert r.status_code == 401, "Response should have status code 401"

    # Detailed tests
    info = "Response should return string 'Unauthorized'"
    assert rt == "Unauthorized", info
