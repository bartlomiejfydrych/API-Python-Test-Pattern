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

