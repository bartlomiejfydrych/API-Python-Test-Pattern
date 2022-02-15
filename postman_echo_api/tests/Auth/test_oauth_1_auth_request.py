from jsonschema.validators import validate

from Auth.data_oauth_1_auth_request import DataOauth1AuthRequest
from postman_echo_api.requests_endpoints.Auth.oauth_1_auth_request import Oauth1AuthRequest
from utils.response_info import ResponseInfo
from utils.response_show import ResponseShow


# def test_oauth_1_auth_request_show():
#     r = Oauth1AuthRequest.ouath_1_auth_request_negative()
#     ResponseShow.show_r(r)
#     # ResponseShow.show_optional(r)
#     # ResponseShow.show_bad_json(r)


def test_oauth_1_auth_request_positive():

    # Prepare response:
    r = Oauth1AuthRequest.oauth_1_auth_request_positive()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response tests:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataOauth1AuthRequest.data_oauth_1_auth_request_positive_schema), "Response should have " \
                                                                                         "correct Schema "

    # Detailed tests
    info = "Response should return correct authorization status and message"
    assert rj["status"] == "pass", info
    assert rj["message"] == "OAuth-1.0a signature verification was successful", info


def test_ouath_1_auth_request_negative():

    # Prepare response:
    r = Oauth1AuthRequest.ouath_1_auth_request_negative()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response tests:
    assert r.status_code == 401, "Response should have status code 401"
    validate(r.json(), DataOauth1AuthRequest.data_oauth_1_auth_request_negative_schema), "Response should have " \
                                                                                         "correct Schema "
    # Detailed tests
    info = "Response should return correct fail auth informations"
    assert rj["status"] == "fail", info
    assert rj["message"] == "HMAC-SHA1 verification failed", info
    assert rj["base_uri"] == "https://postman-echo.com/oauth1", info
    assert rj["signing_key"] == "D%2BEdQ-gs%24-%25%402Nu7&", info
