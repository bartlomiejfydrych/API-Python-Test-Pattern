import json

from requests import Response

from api_interview.requests.get_token import get_auth_token
from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper

url = f"{URL_BASE}users"


def post_create_user(
        token,
        username: str,
        age: int,
        admin: bool,
        skills: list[str],
        city: str,
        street: str,
        street_number: str,
        additional: list[dict]
) -> Response:
    payload = {
        "username": username,
        "age": age,
        "admin": admin,
        "skills": skills,
        "location": {
            "city": city,
            "street": street,
            "street_number": street_number
        },
        "additional": additional
    }
    # response_json_token = get_auth_token()
    # token = response_json_token["access_token"]
    auth_header = {"Authorization": f"Bearer {token}"}
    r = requests_wrapper.post(url, headers=auth_header, json=payload, timeout=1)
    return r


'''
Oryginalny payload ze Swaggera:
{
  "username": "string",
  "age": 0,
  "admin": true,
  "skills": [
    "string"
  ],
  "location": {
    "city": "string",
    "street": "string",
    "street_number": "string"
  },
  "additional": [
    {
      "key": "string",
      "value": "string"
    }
  ]
}
'''
