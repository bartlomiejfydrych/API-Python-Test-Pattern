from api_interview.requests.delete_user import delete_user
from api_interview.requests.get_user import get_user
from api_interview.requests.post_create_user import post_create_user
from utils.response_show import show_response_data
from utils.tests_info import show_tests


def test_delete_user():
    # Add
    response_post = post_create_user(
        username="Endriu",
        age=30,
        admin=True,
        skills=["Chodzenie", "Skakanie", "Pływanie"],
        city="Wąchock",
        street="Oświęcimska",
        street_number="5a",
        additional=[{"key": "Ulubione jedzenie", "value": "Kotlety"}]
    )
    resp_post = response_post.json()
    user_id = resp_post["id"]

    # Delete
    response = delete_user(user_id)
    show_response_data(response)
    resp_txt = response.text

    test_a = "Response should have status code 204"
    assert response.status_code == 204

    test_1 = "Response should have empty body"
    assert resp_txt == ""

    # Get
    response_get = get_user(user_id)
    resp_get = response_get.json()

    test_b = "Response should have status code 404"
    assert response_get.status_code == 404

    test_2 = "Deleted user should not exist"
    expected_response = {
        "status": 404,
        "message": f"Could not find user with id '{user_id}'"
    }
    assert resp_get == expected_response

    # Wyświetlanie testów:
    show_tests(test_a, test_1, test_b, test_2)


# ----------------------------------------------------------------------------------------------------------
# TESTY NEGATYWNE:
# ----------------------------------------------------------------------------------------------------------
def test_delete_user_no_exist():
    user_id = 99999
    response = delete_user(user_id)
    show_response_data(response)
    resp = response.json()

    test_a = "Response should have status code 404"
    assert response.status_code == 404

    test_1 = "Response should have correct body"
    assert resp == {
        "status": 404,
        "message": f"Could not find user with id '{user_id}'"
    }

    # Wyświetlanie testów:
    show_tests(test_a, test_1)
