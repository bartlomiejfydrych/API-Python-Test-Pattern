from jsonschema.validators import validate

from api_reqres.requests_endpoints.get_users import get_users
from data_get_users import schema_get_users, response_get_users_page_1, response_get_users_page_2
from utils.response_info import log_extra_response_info
from utils.response_show import show_r, show_optional
from utils.tests_info import show_tests


# def test_get_users_show():
#     r = get_users(1)
#     show_r(r)
#     show_optional(r)


def test_positive_get_users_page_1():
    # Puszczenie requesta i logowanie info:
    r = get_users(1)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_users), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should be same as saved response"
    assert rj == response_get_users_page_1, test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)


def test_positive_get_users_page_2():
    # Puszczenie requesta i logowanie info:
    r = get_users(2)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_users), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should be same as saved response"
    assert rj == response_get_users_page_2, test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)
