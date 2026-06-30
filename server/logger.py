import json


def log(message, data=None):
    if data is not None:
        print(f"[records] {message} {json.dumps(data)}")
    else:
        print(f"[records] {message}")
