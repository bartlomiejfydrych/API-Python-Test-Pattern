from jsonschema.validators import validate

from data_post_register import schema_post_register
from post_register_utils import post_register
from schema_error import schema_error
from utils.response_info import log_extra_response_info
from utils.response_show import show_response_as_json, show_optional
from utils.tests_info import show_tests


# def test_post_register_show():
#     r = post_register("", "")
#     show_r(r)
#     show_optional(r)


def test_positive_post_register():
    # Puszczenie requesta i logowanie info:
    r = post_register("eve.holt@reqres.in", "pistol")
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert r.status_code == 200, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_post_register), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Generated ID should be above 0"
    assert rj["id"] > 0, test_1

    test_2 = "Generated token should not be null"
    assert rj["token"] is not None, test_2

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1, test_2)


# -----------------------------------------------------------------------------
# NEGATIVE TESTS:
# -----------------------------------------------------------------------------

def test_no_password_post_register():
    # Puszczenie requesta i logowanie info:
    r = post_register("eve.holt@reqres.in", None)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 400"
    assert r.status_code == 400, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_error), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert rj["error"] == "Missing password", test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)


def test_no_email_post_register():
    # Puszczenie requesta i logowanie info:
    r = post_register(None, "pistol")
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 400"
    assert r.status_code == 400, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_error), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert rj["error"] == "Missing email or username", test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)


def test_no_defined_user_post_register():
    # Puszczenie requesta i logowanie info:
    r = post_register("bob@op.pl", "1234")
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 400"
    assert r.status_code == 400, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_error), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert rj["error"] == "Note: Only defined users succeed registration", test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)
