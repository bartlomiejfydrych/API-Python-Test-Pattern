from jsonschema.validators import validate

from api_interview.requests.get_version import get_version
from utils.tests_info import show_tests

from api_interview.tests_data.data_get_version import GetVersionDTO, schema_get_version
from utils.response_show import show_response_data


def test_get_version(auth):
    response = get_version(auth)
    resp = response.json()

    # ----------------------
    # Basic response tests:
    # ----------------------
    test_a = "Response should have status code 200"
    assert response.status_code == 200

    test_b = "Response should have correct Schema"
    validate(resp, schema_get_version)

    test_c = "Response should have correct Data Transfer Object (DTO)"
    GetVersionDTO.validate(resp)

    # ----------------------
    # Detailed tests:
    # ----------------------
    test_1 = "Response should return correct version"
    assert resp == {
        "version": "1.0.22"
    }

    # ----------------------
    # Wyświetlenie testów:
    # ----------------------
    show_tests(test_a, test_b, test_c, test_1)
