import requests
from requests import Response

from api_dummy.requests_endpoints.url_base import UrlBase


class EndpointGetEmployee:

    employee_id = 4
    url = f"{UrlBase.URL_BASE}employee/{employee_id}"
    url_no_exist_id = f"{UrlBase.URL_BASE}employee/9999"
    headers = {'user-agent': 'Chrome/105.0.0.0'}

    @staticmethod
    def get_employee() -> Response:
        return requests.get(EndpointGetEmployee.url, headers=EndpointGetEmployee.headers, timeout=1)

    @staticmethod
    def get_employee_no_exist_id() -> Response:
        return requests.get(EndpointGetEmployee.url_no_exist_id, headers=EndpointGetEmployee.headers, timeout=1)
