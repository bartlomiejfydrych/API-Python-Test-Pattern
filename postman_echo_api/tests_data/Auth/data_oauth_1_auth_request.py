class DataOauth1AuthRequest:
    data_oauth_1_auth_request_positive_schema = {
        "type": "object",
        "properties": {
            "status": {"type": "string"},
            "message": {"type": "string"}
        },
        "required": ["status", "message"]
    }

    data_oauth_1_auth_request_negative_schema = {
        "type": "object",
        "properties": {
            "status": {"type": "string"},
            "message": {"type": "string"},
            "base_uri": {"type": "string"},
            "normalized_param_string": {"type": "string"},
            "base_string": {"type": "string"},
            "signing_key": {"type": "string"}
        },
        "required": [
            "status",
            "message",
            "base_uri",
            "normalized_param_string",
            "base_string",
            "signing_key"
        ]
    }
