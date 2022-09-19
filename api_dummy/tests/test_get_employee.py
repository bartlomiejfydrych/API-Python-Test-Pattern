from jsonschema.validators import validate

from api_dummy.requests_endpoints.get_employee import get_employee
from data_get_employee import schema_get_employee, response_get_employee
from utils.response_info import log_extra_response_info
from utils.response_show import show_r, show_optional
from utils.tests_info import show_tests


def test_get_employee_show():
    r = get_employee(9999)
    show_r(r)
    show_optional(r)


def test_get_employee():
    # Puszczenie requesta i logowanie info:
    r = get_employee(4)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been fetched.", test_2

    test_3 = "Employee with ID=4 should have correct data"
    assert rj["data"]["id"] == 4, test_3
    assert rj["data"]["employee_name"] == "Cedric Kelly", test_3
    assert rj["data"]["employee_salary"] == 433060, test_3
    assert rj["data"]["employee_age"] == 22, test_3
    assert rj["data"]["profile_image"] == "", test_3

    test_4 = "Complete response must be the same as saved response"
    assert rj == response_get_employee, test_4

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3, test_4)


def test_get_employee_no_exist_id():
    # Puszczenie requesta i logowanie info:
    r = get_employee(9999)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_get_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been fetched.", test_2

    test_3 = "Data should be null"
    assert rj["data"] is None, test_3

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3)
