from api_dummy.requests_endpoints.get_employees import GetEmployees
from utils.response_show import ResponseShow


def test_get_employees_show():
    r = GetEmployees.get_employees()
    ResponseShow.show_r(r)
    ResponseShow.show_optional(r)
