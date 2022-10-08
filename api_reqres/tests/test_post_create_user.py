from jsonschema.validators import validate

from data_post_create_user import schema_post_create_user
from post_create_user_utils import post_create_user
from utils.response_info import log_extra_response_info
from utils.response_show import show_response_as_json, show_optional
from utils.tests_info import show_tests


# def test_post_create_user_show():
#     r = post_create_user("Bogdan Kopytko", "spawacz")
#     show_r(r)
#     show_optional(r)


def test_positive_post_create_user():
    # Zmienne do payload
    user_name = "Bogdan Kopytko"
    user_job = "spawacz"

    # Puszczenie requesta i logowanie info:
    r = post_create_user(user_name, user_job)
    log_extra_response_info(r)
    # Przerobienie response na JSON:
    rj = r.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 201"
    assert r.status_code == 201, test_a

    test_b = "Response should have correct Schema"
    validate(rj, schema_post_create_user), test_b

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Created user should have correct values"
    assert rj["name"] == user_name, test_1
    assert rj["job"] == user_job, test_1

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_1)

# Nie było jak zrobić negatywnych testów, ponieważ wszystkie dane przechodzą
