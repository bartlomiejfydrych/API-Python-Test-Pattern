schema_post_employee = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "salary": {"type": "string"},
                "age": {"type": "string"},
                "id": {"type": "integer"}
            },
            "required": [
                "name",
                "salary",
                "age",
                "id"
            ]
        },
        "message": {"type": "string"}
    },
    "required": [
        "status",
        "data",
        "message"
    ]
}
