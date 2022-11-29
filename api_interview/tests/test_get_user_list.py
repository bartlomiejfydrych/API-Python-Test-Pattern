from api_interview.requests.get_user_list import get_user_list
from utils.response_show import show_response_data


def test_get_user_list_add_user(create_delete_user):
    response = get_user_list()
    show_response_data(response)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert response.status_code == 200

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should have correct data"
    added_user = next((user for user in resp if user["id"] == create_delete_user["id"]), None)
    assert create_delete_user == added_user


# def test_get_user_list_edit_user(create_delete_user):



# def test_get_user_list_delete_user():