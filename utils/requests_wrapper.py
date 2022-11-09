import requests

from utils.response_info import log_extra_response_info


def post(url, data=None, json=None, **kwargs):
    response = requests.post(url, data, json, **kwargs)
    log_extra_response_info(response)

    return response


def put(url, data=None, **kwargs):
    response = requests.put(url, data, **kwargs)
    log_extra_response_info(response)

    return response


def get(url, params=None, **kwargs):
    response = requests.get(url, params, **kwargs)
    log_extra_response_info(response)

    return response


def delete(url, **kwargs):
    response = requests.delete(url, **kwargs)
    log_extra_response_info(response)

    return response


'''
# użycie przed
def get_employee_endpoint(employee_id) -> Response:
    url = f"{URL_BASE}employee/{employee_id}"
    return requests.get(url, headers=headers, timeout=1)


# użycie po
def get_employee_endpoint(employee_id) -> Response:
    url = f"{URL_BASE}employee/{employee_id}"
    return requests_wrapper.get(url, headers=headers, timeout=1)
'''
