from pydantic import BaseModel, StrictStr

schema_get_version = {
    "type": "object",
    "properties": {
        "version": {"type": "string"}
    },
    "required": [
        "version"
    ]
}


class GetVersionDTO(BaseModel):
    version: StrictStr
