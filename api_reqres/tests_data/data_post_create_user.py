schema_post_create_user = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ]
}
