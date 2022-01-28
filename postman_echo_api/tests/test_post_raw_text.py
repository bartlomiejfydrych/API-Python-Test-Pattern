from jsonschema.validators import validate

from data_post_raw_text import DataPostRawText
from post_raw_text_utils import PostRawTextUtils
from utils.response_info import ResponseInfo
from utils.response_show import ResponseShow


# def test_post_raw_text_show():
#     r = PostRawTextUtils.post_raw_text_payload()
#     ResponseShow.show_r(r)
#     ResponseShow.show_optional(r)


def test_post_raw_text():
    # Prepare response:
    r = PostRawTextUtils.post_raw_text_payload()
    ResponseInfo.log_extra_response_info(r)
    rj = r.json()

    # Basic response tests:
    assert r.status_code == 200, "Response should have status code 200"
    validate(r.json(), DataPostRawText.post_raw_text_schema), "Response should have correct Schema"

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
    assert rj["headers"]["x-forwarded-proto"] == "https", info
    assert rj["headers"]["x-forwarded-port"] == "443", info
    assert rj["headers"]["host"] == "postman-echo.com", info

    info = "Response should have correct url"
    assert rj["url"] == "https://postman-echo.com/post", info
