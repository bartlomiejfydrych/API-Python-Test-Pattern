from api_interview.requests.get_user import get_user
from utils.response_show import show_response_data
from utils.tests_info import show_tests


def test_get_user_no_exist_id(auth):
    response = get_user(auth, 99999)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 404"
    assert response.status_code == 404

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct error message"
    assert resp["status"] == 404
    assert resp["message"] == "Could not find user with id '99999'"

    # Wyświetlanie testów:
    show_tests(test_a, test_1)
