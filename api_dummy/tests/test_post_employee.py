from jsonschema.validators import validate

from data_post_employee import schema_post_employee
from post_employee_utils import post_employee
from utils.response_info import log_extra_response_info
from utils.response_show import show_r, show_optional, show_bad_json
from utils.tests_info import show_tests


def test_post_employee_show():
    r = post_employee("Lorem ipsum dolor sit amet, consectetur porttitor.", 999999999999, 777777777777)
    show_r(r)
    show_optional(r)


def test_positive_post_employee():
    # Puszczenie requesta i logowanie info:
    r = post_employee("Dave", 20000, 27)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_post_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been added.", test_2

    test_3 = "Added employee should have correct data"
    assert rj["data"]["name"] == "Dave", test_3
    assert rj["data"]["salary"] == "20000", test_3
    assert rj["data"]["age"] == "27", test_3
    assert rj["data"]["id"] > 0, test_3

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3)


def test_overload_data_post_employee():
    # Puszczenie requesta i logowanie info:
    r = post_employee(
        "Lorem ipsum dolor sit amet, consectetur porttitor.",
        999999999999,
        777777777777
    )
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_post_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been added.", test_2

    test_3 = "Added employee should have correct data"
    assert rj["data"]["name"] == "Lorem ipsum dolor sit amet, consectetur porttitor.", test_3
    assert rj["data"]["salary"] == "999999999999", test_3
    assert rj["data"]["age"] == "777777777777", test_3
    assert rj["data"]["id"] > 0, test_3

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3)
