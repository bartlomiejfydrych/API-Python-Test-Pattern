from jsonschema.validators import validate

from api_reqres.requests_endpoints.get_user import get_user
from data_get_user import schema_get_user
from utils.response_info import log_extra_response_info
from utils.response_show import show_optional, show_response_as_json
from utils.tests_info import show_tests


def test_get_user_show():
    r = get_user(99999)
    show_response_as_json(r)
    show_optional(r)


def test_positive_get_user_1():
    # Puszczenie requesta i logowanie info:
    r = get_user(1)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_user), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response 'data' section should have correct values"
    assert rj["data"]["id"] == 1, test_1
    assert rj["data"]["email"] == "george.bluth@reqres.in", test_1
    assert rj["data"]["first_name"] == "George", test_1
    assert rj["data"]["last_name"] == "Bluth", test_1
    assert rj["data"]["avatar"] == "https://reqres.in/img/faces/1-image.jpg", test_1

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

def test_no_exist_user_get_user():
    # Puszczenie requesta i logowanie info:
    r = get_user(99999)
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
