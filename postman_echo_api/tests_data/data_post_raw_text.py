class DataPostRawText:

    post_raw_text_schema = {
        "type": "object",
        "properties": {
            "args": {"type": "object"},
            "data": {"type": "string"},
            "files": {"type": "object"},
            "form": {
                "type": "object",
                "properties": {
                    "Wartość_1": {"type": "string"},
                    "Wartość 2": {"type": "string"},
                    "Wartość3": {"type": "string"}
                },
                "required": [
                    "Wartość_1",
                    "Wartość 2",
                    "Wartość3"
                ]
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
                    "content-type": {"type": "string"}
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
                    "content-type"
                ]
            },
            "json": {
                "type": "object",
                "properties": {
                    "Wartość_1": {"type": "string"},
                    "Wartość 2": {"type": "string"},
                    "Wartość3": {"type": "string"}
                },
                "required": [
                    "Wartość_1",
                    "Wartość 2",
                    "Wartość3"
                ]
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

    response = {
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
