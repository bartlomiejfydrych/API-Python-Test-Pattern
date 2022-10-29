from pydantic import BaseModel, StrictStr

# SCHEMA:
schema_post_create_user = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "age": {"type": "integer"},
        "admin": {"type": "boolean"},
        "skills": {
            "type": "array",
            "items": {"type": "string"}
        },
        "location": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "street": {"type": "string"},
                "street_number": {"type": "string"}
            },
            "required": [
                "city",
                "street",
                "street_number"
            ]
        },
        "additional": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "key": {"type": "string"},
                    "value": {"type": "string"}
                },
                "required": [
                    "key",
                    "value"
                ]
            }
        }
    },
    "required": [
        "id",
        "username",
        "age",
        "admin",
        "skills",
        "location",
        "additional"
    ]
}

# VALIDATION ERROR RESPONSE:
response_validation_error_username = {
    "detail": [
        {
            "loc": [
                "body",
                "username"
            ],
            "msg": "none is not an allowed value",
            "type": "type_error.none.not_allowed"
        }
    ]
}

response_validation_error_age = {
    "detail": [
        {
            "loc": [
                "body",
                "age"
            ],
            "msg": "none is not an allowed value",
            "type": "type_error.none.not_allowed"
        }
    ]
}

response_validation_error_age_integer = {
    "detail": [
        {
            "loc": [
                "body",
                "age"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}

# DTO:


class Location(BaseModel):
    city: StrictStr
    street: StrictStr
    street_number: StrictStr


class AdditionalItem(BaseModel):
    key: StrictStr
    value: StrictStr


class CreateUserDTO(BaseModel):
    id: int
    username: StrictStr
    age: int
    admin: bool
    skills: list[StrictStr]
    location: Location
    additional: list[AdditionalItem]


# PAYLOADS:

