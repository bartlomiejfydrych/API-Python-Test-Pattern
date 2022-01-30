from jsonschema.validators import validate

from data_post_request import DataPostRequest
from post_request_utils import PostRequestUtils
from utils.response_info import ResponseInfo
from utils.response_show import ResponseShow


def test_post_request_show():
    r = PostRequestUtils.post_raw_text()
    ResponseShow.show_r(r)
    ResponseShow.show_optional(r)


def test_post_form_data():
    # Prepare response:
    r = PostRequestUtils.post_form_data()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response tests:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataPostRequest.post_request_schema), "Response should have correct Schema"

    # Detailed tests
    info = "Response should have correct keys and values in 'form'"
    assert rj["form"]["Wartość_1"] == "12żółć34", info
    assert rj["form"]["Wartość 2"] == "12polska34", info
    assert rj["form"]["Wartość3"] == "1bęc2()$%3", info

    info = "Response should have correct keys and values in 'json'"
    assert rj["json"]["Wartość_1"] == "12żółć34", info
    assert rj["json"]["Wartość 2"] == "12polska34", info
    assert rj["json"]["Wartość3"] == "1bęc2()$%3", info

    info = "Response should have correct other parameters"
    assert rj["args"] == {}, info
    assert rj["data"] == "", info
    assert rj["files"] == {}, info
    assert rj["headers"]["x-forwarded-proto"] == "https", info
    assert rj["headers"]["x-forwarded-port"] == "443", info
    assert rj["headers"]["host"] == "postman-echo.com", info

    info = "Response should have correct url"
    assert rj["url"] == "https://postman-echo.com/post", info


def test_post_raw_text():
    # Prepare response:
    r = PostRequestUtils.post_raw_text()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response test:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataPostRequest.post_request_schema), "Response should have correct Schema"

    # Detailed tests
    info = "Response should have correct value in 'data'"
    assert rj["data"] == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus efficitur ante arcu, " \
                         "nec gravida libero varius at. Curabitur rhoncus purus.", info

    info = "Response should have correct other parameters"
    assert rj["args"] == {}, info
    assert rj["files"] == {}, info
    assert rj["form"] == {}, info
    assert rj["json"] is None, info
    assert rj["headers"]["x-forwarded-proto"] == "https", info
    assert rj["headers"]["x-forwarded-port"] == "443", info
    assert rj["headers"]["host"] == "postman-echo.com", info

    info = "Response should have correct url"
    assert rj["url"] == "https://postman-echo.com/post", info


def test_post_args():
    # Prepare response:
    r = PostRequestUtils.post_args()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response test:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataPostRequest.post_request_schema), "Response should have correct Schema"

    # Detailed tests
    info = "Response should have correct value in 'args'"
    assert rj["args"] == DataPostRequest.params_args, info

    info = "Response should have correct other parameters"
    assert rj["data"] == {}, info
    assert rj["files"] == {}, info
    assert rj["form"] == {}, info
    assert rj["json"] is None, info
    assert rj["headers"]["x-forwarded-proto"] == "https", info
    assert rj["headers"]["x-forwarded-port"] == "443", info
    assert rj["headers"]["host"] == "postman-echo.com", info

    info = "Response should have correct url"
    assert rj["url"] == "https://postman-echo.com/post?status=positive&photos=no+duplicate&region=HKS+122&ph=Albert" \
                        "+Gizmo", info
