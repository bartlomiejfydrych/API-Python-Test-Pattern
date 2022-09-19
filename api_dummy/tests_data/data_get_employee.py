schema_get_employee = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "data": {
            "type": ["object", "null"],
            "properties": {
                "id": {"type": "integer"},
                "employee_name": {"type": "string"},
                "employee_salary": {"type": "integer"},
                "employee_age": {"type": "integer"},
                "profile_image": {"type": "string"}
            },
            "required": [
                "id",
                "employee_name",
                "employee_salary",
                "employee_age",
                "profile_image"
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

response_get_employee = {
    "status": "success",
    "data": {
        "id": 4,
        "employee_name": "Cedric Kelly",
        "employee_salary": 433060,
        "employee_age": 22,
        "profile_image": ""
    },
    "message": "Successfully! Record has been fetched."
}
