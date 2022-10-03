from jsonschema.validators import validate

from api_reqres.requests_endpoints.get_resource_single import get_resource_single
from data_get_resource_single import schema_get_resource_single
from utils.response_info import log_extra_response_info
from utils.response_show import show_r, show_optional
from utils.tests_info import show_tests


def test_get_resource_single_show():
    r = get_resource_single(99999)
    show_r(r)
    show_optional(r)


def test_positive_get_resource_single():
    # Puszczenie requesta i logowanie info:
    r = get_resource_single(2)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_resource_single), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response 'data' section should have correct values"
    assert rj["data"]["id"] == 2, test_1
    assert rj["data"]["name"] == "fuchsia rose", test_1
    assert rj["data"]["year"] == 2001, test_1
    assert rj["data"]["color"] == "#C74375", test_1
    assert rj["data"]["pantone_value"] == "17-2031", test_1

    test_2 = "Response 'support' section should have correct values"
    assert rj["support"]["url"] == "https://reqres.in/#support-heading", test_2
    assert rj["support"]["text"] == "To keep ReqRes free, contributions towards server costs are appreciated!", test_2

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2)


# -----------------------------------------------------------------------------
# NEGATIVE TESTS:
# -----------------------------------------------------------------------------

def test_no_exist_resource_get_resource_single():
    # Puszczenie requesta i logowanie info:
    r = get_resource_single(99999)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 404"
    assert r.status_code == 404, test_a

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should be empty object (for Python dictionary)"
    assert type(rj) is dict, test_1
    assert rj == {}, test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_1)
