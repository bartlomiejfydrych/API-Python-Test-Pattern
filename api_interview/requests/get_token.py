import os

from dotenv import load_dotenv
from requests import Response
from requests.auth import HTTPBasicAuth

from api_interview.requests.url_base import URL_BASE
from api_interview.resources.files_config import ENV_FILE_PATH
from utils import requests_wrapper

url = f"{URL_BASE}token"


def get_token(username: str, password: str) -> Response:
    data = {
        "username": username,
        "password": password
    }
    return requests_wrapper.post(url, data=data, timeout=1)


def get_auth_token():
    load_dotenv(ENV_FILE_PATH)
    user_name = os.getenv("USERNAME")
    username = user_name.lower()
    password = os.getenv("PASSWORD")
    response = get_token(username, password)
    assert response.status_code == 200
    return response.json()
