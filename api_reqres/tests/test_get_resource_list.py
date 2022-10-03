from jsonschema.validators import validate

from api_reqres.requests_endpoints.get_resource_list import get_resource_list
from data_get_resource_list import schema_get_resource_list, response_get_resource_list
from utils.response_info import log_extra_response_info
from utils.response_show import show_r, show_optional
from utils.tests_info import show_tests


def test_get_resource_list_show():
    r = get_resource_list()
    show_r(r)
    show_optional(r)


def test_positive_get_resource_list():
    # Puszczenie requesta i logowanie info:
    r = get_resource_list()
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_resource_list), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should be same as saved response"
    assert rj == response_get_resource_list, test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)
