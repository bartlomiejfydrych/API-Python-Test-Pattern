from api_reqres.requests_endpoints.delete_user import delete_user
from utils.response_info import log_extra_response_info
from utils.response_show import show_optional, show_bad_json
from utils.tests_info import show_tests


# def test_delete_user_show():
#     r = delete_user(2)
#     show_bad_json(r)
#     show_optional(r)


def test_delete_user():
    # Puszczenie requesta i logowanie info:
    r = delete_user(2)
    log_extra_response_info(r)
    # Przerobienie response na tekst:
    rt = r.text

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 204"
    assert r.status_code == 204, test_a

    test_b = "Response should be empty text"
    assert rt == "", test_b

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b)

# Nie ma jak zrobić negatywnych testów
