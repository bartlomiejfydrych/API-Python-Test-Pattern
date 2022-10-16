from requests import Response

from api_interview.requests.url_base import URL_BASE
from utils import requests_wrapper

url = f"{URL_BASE}users"


def post_create_user(
        username: str,
        age: int,
        admin: bool,
        skills: list,
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
    return requests_wrapper.post(url, data=payload, timeout=1)


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
