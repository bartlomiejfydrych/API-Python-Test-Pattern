class DataGetRequest:

    get_request_schema = {
        "type": "object",
        "properties": {
            "args": {
                "type": "object",
                "properties": {
                    "foo1": {"type": "string"},
                    "foo2": {"type": "string"}
                },
                "required": ["foo1", "foo2"]
            },
            "headers": {
                "type": "object",
                "properties": {
                    "x-forwarded-proto": {"type": "string"},
                    "x-forwarded-port": {"type": "string"},
                    "host": {"type": "string"},
                    "x-amzn-trace-id": {"type": "string"},
                    "user-agent": {"type": "string"},
                    "accept-encoding": {"type": "string"},
                    "accept": {"type": "string"}
                },
                "required": [
                    "x-forwarded-proto",
                    "x-forwarded-port",
                    "host",
                    "x-amzn-trace-id",
                    "user-agent",
                    "accept-encoding",
                    "accept"
                ]
            },
            "url": {"type": "string"}
        },
        "required": ["args", "headers", "url"]
    }

    respone = {
        "args": {
            "foo1": "bar1",
            "foo2": "bar2"
        },
        "headers": {
            "x-forwarded-proto": "https",
            "x-forwarded-port": "443",
            "host": "postman-echo.com",
            "x-amzn-trace-id": "Root=1-61cb2fed-52002ffa01c736270f8b5c8b",
            "user-agent": "python-requests/2.26.0",
            "accept-encoding": "gzip, deflate",
            "accept": "*/*"
        },
        "url": "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
    }

"""
NOTES:
Zmiana jsona na DTO:
https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
"""