import nt
import os

import requests
from dotenv import load_dotenv
from requests import Response
from requests.auth import HTTPBasicAuth

from api_interview.requests.url_base import URL_BASE
from api_interview.resources.files_config import ENV_FILE_PATH
from utils import requests_wrapper


def request_get_token(username: str, password: str) -> Response:
    url = f"{URL_BASE}token"
    data = {
        "username": username,
        "password": password
    }
    return requests_wrapper.post(url, data=data, timeout=1)


def get_token(token_file_path):
    load_dotenv(ENV_FILE_PATH)
    username = os.getenv("USER_USERNAME")
    password = os.getenv("USER_PASSWORD")
    response = request_get_token(username, password)
    assert response.status_code == 200
    response_json = response.json()
    token = response_json["access_token"]
    file = open(token_file_path, "r+")
    file.write(token)
    file.close()
    return token


def env_authorization():
    load_dotenv(ENV_FILE_PATH)
    username = os.getenv("USER_USERNAME")
    password = os.getenv("USER_PASSWORD")
    response = request_get_token(username, password)
    assert response.status_code == 200
    return response
