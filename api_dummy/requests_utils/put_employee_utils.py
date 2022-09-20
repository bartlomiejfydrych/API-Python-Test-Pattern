from api_dummy.requests_endpoints.put_employee import put_employee_endpoint


def put_employee(employee_id, name, salary, age):
    payload = {
        "name": name,
        "salary": str(salary),
        "age": str(age)
    }
    r = put_employee_endpoint(employee_id, payload)
    return r
