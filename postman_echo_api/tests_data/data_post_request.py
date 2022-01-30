class DataPostRequest:

    post_request_schema = {
        "type": "object",
        "properties": {
            "args": {"type": "object"},
            "data": {"type": ["object", "string"]},
            "files": {"type": "object"},
            "form": {
                "type": "object",
                "patternProperties": {
                    ".": {"type": ["string", "integer"]},
                },
                "additionalProperties": True
            },
            "headers": {
                "type": "object",
                "properties": {
                    "x-forwarded-proto": {"type": "string"},
                    "x-forwarded-port": {"type": "string"},
                    "host": {"type": "string"},
                    "x-amzn-trace-id": {"type": "string"},
                    "content-length": {"type": "string"},
                    "user-agent": {"type": "string"},
                    "accept-encoding": {"type": "string"},
                    "accept": {"type": "string"},
                },
                "required": [
                    "x-forwarded-proto",
                    "x-forwarded-port",
                    "host",
                    "x-amzn-trace-id",
                    "content-length",
                    "user-agent",
                    "accept-encoding",
                    "accept",
                ],
                "additionalProperties": {
                    "content-type": {"type": "string"}
                }
            },
            "json": {
                "type": ["object", "null"],
                "patternProperties": {
                    ".": {"type": ["string", "integer"]},
                },
                "additionalProperties": True
            },
            "url": {"type": "string"}
        },
        "required": [
            "args",
            "data",
            "files",
            "form",
            "headers",
            "json",
            "url"
        ]
    }

    post_response = {
        "args": {},
        "data": "",
        "files": {},
        "form": {
            "Wartość_1": "12żółć34",
            "Wartość 2": "12polska34",
            "Wartość3": "1bęc2()$%3"
        },
        "headers": {
            "x-forwarded-proto": "https",
            "x-forwarded-port": "443",
            "host": "postman-echo.com",
            "x-amzn-trace-id": "Root=1-61f406a6-17025d614bbeb28975eddf9e",
            "content-length": "122",
            "user-agent": "python-requests/2.26.0",
            "accept-encoding": "gzip, deflate",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded"
        },
        "json": {
            "Wartość_1": "12żółć34",
            "Wartość 2": "12polska34",
            "Wartość3": "1bęc2()$%3"
        },
        "url": "https://postman-echo.com/post"
    }

    params_args = {
        "status": "positive",
        "photos": "no duplicate",
        "region": "HKS 122",
        "ph": "Albert Gizmo"
    }
