from requests import Response

from api_dummy.requests_endpoints.post_employee import post_employee_endpoint


def post_employee(name, salary, age) -> Response:
    payload = {
        "name": name,
        "salary": str(salary),
        "age": str(age)
    }
    r = post_employee_endpoint(payload)
    return r
