from jsonschema.validators import validate

from data_put_employee import schema_put_employee
from post_employee_utils import post_employee
from put_employee_utils import put_employee
from utils.response_info import log_extra_response_info
from utils.response_show import show_response_as_json, show_optional
from utils.tests_info import show_tests


# def test_put_employee_show():
#     r = put_employee(5, "Mike Ashbringer", 4125, 35)
#     show_r(r)
#     show_optional(r)


def test_positive_put_emplotee():
    # ----------------------
    # Prepare data:
    # ----------------------
    # Dodanie własnego pracownika (POST) i pobranie jego ID
    r = post_employee("Bob Edition", 5000, 40)
    info = "Dodanie pracownika"
    assert r.status_code == 200, info
    rj = r.json()
    employee_id = rj["data"]["id"]

    # Edycja dodanego pracownika
    r = put_employee(employee_id, "Mike Ashbringer", 4125, 35)
    log_extra_response_info(r)
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_put_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been updated.", test_2

    test_3 = "Edited employee should have correct data"
    assert rj["data"]["name"] == "Mike Ashbringer", test_3
    assert rj["data"]["salary"] == "4125", test_3
    assert rj["data"]["age"] == "35", test_3

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3)


def test_overload_data_put_emplotee():
    # ----------------------
    # Prepare data:
    # ----------------------
    # Dodanie własnego pracownika (POST) i pobranie jego ID
    r = post_employee("Bob Edition 2", 5002, 42)
    info = "Dodanie pracownika"
    assert r.status_code == 200, info
    rj = r.json()
    employee_id = rj["data"]["id"]

    # Edycja dodanego pracownika
    r = put_employee(
        employee_id,
        "Cras pulvinar justo ac efficitur semper tincidunt.",
        888888888888,
        666666666666
    )
    log_extra_response_info(r)
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_put_employee), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Status should be 'success'"
    assert rj["status"] == "success", test_1

    test_2 = "Message should have correct value"
    assert rj["message"] == "Successfully! Record has been updated.", test_2

    test_3 = "Edited employee should have correct data"
    assert rj["data"]["name"] == "Cras pulvinar justo ac efficitur semper tincidunt.", test_3
    assert rj["data"]["salary"] == "888888888888", test_3
    assert rj["data"]["age"] == "666666666666", test_3

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2, test_3)
