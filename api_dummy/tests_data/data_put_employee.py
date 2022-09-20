schema_put_employee = {
    "type": "object",
    "properties": {
        "status": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "salary": {"type": "string"},
                "age": {"type": "string"}
            },
            "required": [
                "name",
                "salary",
                "age"
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
