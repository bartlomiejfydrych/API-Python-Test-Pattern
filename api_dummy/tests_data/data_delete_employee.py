schema_delete_employee = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "data": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": [
        "status",
        "data",
        "message"
    ]
}
