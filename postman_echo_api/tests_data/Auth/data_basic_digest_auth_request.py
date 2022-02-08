class DataBasicDigestAuthRequest:

    basic_auth_request_schema = {
        "type": "object",
        "properties": {
            "authenticated": {
                "type": "boolean",
                "default": True
            }
        },
        "required": ["authenticated"]
    }
