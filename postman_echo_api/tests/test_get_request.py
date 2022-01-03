import json
from types import SimpleNamespace

from postman_echo_api.requests_endpoints.get_request import GetRequest
from postman_echo_api.tests_data.data_get_request import DataGetRequest
from utils.response_info import ResponseInfo
from jsonschema import validate
from utils.response_show import ResponseShow


# def test_get_request_show():
#     r = GetRequest.get_request()
#     ResponseShow.show_r(r)
#     ResponseShow.show_optional(r)

def test_get_request():
    # Tutaj poruszamy się po JSON
    r = GetRequest.get_request()
    ResponseInfo.log_extra_response_info(r)
    # Basic response tests:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataGetRequest.get_request_schema), "Response should have correct Schema"
    # Detailed tests
    rj = r.json()
    info = "Response should have correct args"
    assert rj["args"]["foo1"] == "bar1", info
    assert rj["args"]["foo2"] == "bar2", info
    info = "Response should have correct headers"
    assert rj["headers"]["x-forwarded-proto"] == "https", info
    assert rj["headers"]["x-forwarded-port"] == "443", info
    assert rj["headers"]["host"] == "postman-echo.com", info
    assert rj["headers"]["x-amzn-trace-id"] != "", info
    assert rj["headers"]["user-agent"] == "python-requests/2.26.0", info
    assert rj["headers"]["accept-encoding"] == "gzip, deflate", info
    assert rj["headers"]["accept"] == "*/*", info
    info = "Response should have correct url"
    assert rj["url"] == "https://postman-echo.com/get?foo1=bar1&foo2=bar2", info


# PORUSZANIE SIĘ PO DTO:
def test_get_request_correct_args_dto():
    r = GetRequest.get_request()
    ResponseInfo.log_extra_response_info(r)
    rj = r.text
    x = json.loads(rj, object_hook=lambda d: SimpleNamespace(**d))
    assert x.args.foo1 == "bar1"
    assert x.args.foo2 == "bar2"


# def test_get_request_correct_headers_dto():
#     r = GetRequest.get_request()
#     ResponseInfo.log_extra_response_info(r)
#     rj = r.text
#     x = json.loads(rj, object_hook=lambda d: SimpleNamespace(**d))
#     assert x.headers.x-forwarded-proto == "https"


"""
NOTES:
r.json() - już podczas używania tego jest walidowane czy resposne posiada prawidłowy JSON.
Jeżeli nie, to ta metoda się wywali.
"""