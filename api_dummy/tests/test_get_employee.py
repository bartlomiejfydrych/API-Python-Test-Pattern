from jsonschema.validators import validate

from api_dummy.requests_endpoints.get_employee import EndpointGetEmployee
from data_get_employee import DataGetEmployee
from utils.response_info import ResponseInfo
from utils.response_show import ResponseShow
from utils.tests_info import TestsInfo


def test_get_employee_show():
    r = EndpointGetEmployee.get_employee_no_exist_id()
    ResponseShow.show_r(r)
    ResponseShow.show_optional(r)


def test_get_employee():
    # Puszczenie requesta i logowanie info:
    r = EndpointGetEmployee.get_employee()
    ResponseInfo.log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, DataGetEmployee.schema_get_employee), test_b

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
    assert rj == DataGetEmployee.response_get_employee, test_4

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    TestsInfo.show_tests(test_a, test_b, test_1, test_2, test_3, test_4)


def test_get_employee_no_exist_id():
    # Puszczenie requesta i logowanie info:
    r = EndpointGetEmployee.get_employee_no_exist_id()
    ResponseInfo.log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, DataGetEmployee.schema_get_employee), test_b

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
    TestsInfo.show_tests(test_a, test_b, test_1, test_2, test_3)
