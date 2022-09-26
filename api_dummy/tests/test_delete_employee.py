from jsonschema.validators import validate

from api_dummy.requests_endpoints.delete_employee import delete_employee_endpoint
from data_delete_employee import schema_delete_employee
from post_employee_utils import post_employee
from utils.response_info import log_extra_response_info
from utils.response_show import show_r, show_optional
from utils.tests_info import show_tests


# def test_delete_employee_show():
#     r = delete_employee_endpoint(99999)
#     show_r(r)
#     show_optional(r)


def test_positive_delete_employee():
    # ----------------------
    # Prepare data:
    # ----------------------
    # Dodanie własnego pracownika (POST) i pobranie jego ID
    r = post_employee("Dick Delete", 10000, 65)
    info = "Dodanie pracownika"
    assert r.status_code == 200, info
    rj = r.json()
    employee_id = rj["data"]["id"]

    # Usunięcie tego pracownika
    r = delete_employee_endpoint(employee_id)
    log_extra_response_info(r)
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_delete_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been deleted", test_2

    test_3 = "Data should have ID of our deleted employee"
    assert rj["data"] == str(employee_id), test_3

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3)
