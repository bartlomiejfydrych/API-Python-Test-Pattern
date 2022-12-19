from requests import Response

from api_interview.requests.get_token import env_authorization
from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper


def put_edit_user(
        token,
        user_id,
        username: str,
        age: int,
        admin: bool,
        skills: list[str],
        city: str,
        street: str,
        street_number: str,
        additional: list[dict]
) -> Response:
    url = f"{URL_BASE}users/{user_id}"
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
    response = requests_wrapper.put(url, headers=auth_header, json=payload, timeout=1)
    return response


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