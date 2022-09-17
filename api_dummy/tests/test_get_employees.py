from jsonschema.validators import validate

from api_dummy.requests_endpoints.get_employees import EndpointGetEmployees
from data_get_employees import DataGetEmployees
from utils.response_info import ResponseInfo
from utils.tests_info import TestsInfo
from utils.response_show import ResponseShow


# Dla PyTest nazwy klas z testami zaczynamy od słowa 'Test'
# np. class TestGetEmployees:

# def test_get_employees_show():
#     r = EndpointGetEmployees.get_employees()
#     ResponseShow.show_r(r)
#     ResponseShow.show_optional(r)


def test_get_employees():
    # Puszczenie requesta i logowanie info:
    r = EndpointGetEmployees.get_employees()
    ResponseInfo.log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, DataGetEmployees.schema_get_employees), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! All records has been fetched.", test_2

    test_3 = "Employee with ID=5 should be on list"
    employees = rj["data"]
    assert any(employee["id"] == 5 for employee in employees), test_3

    test_4 = "Employee with ID=5 should have correct data"
    employee_five = next(employee for employee in employees if employee["id"] == 5)
    assert employee_five["id"] == 5, test_4
    assert employee_five["employee_name"] == "Airi Satou", test_4
    assert employee_five["employee_salary"] == 162700, test_4
    assert employee_five["employee_age"] == 33, test_4
    assert employee_five["profile_image"] == "", test_4

    test_5 = "Complete response must be the same as saved response"
    assert rj == DataGetEmployees.response_get_employees, test_5

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    TestsInfo.show_tests(test_a, test_b, test_1, test_2, test_3, test_4, test_5)
