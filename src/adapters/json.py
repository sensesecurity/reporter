import json

ERROR_FILE_NOT_FOUND = "Error: File not found"
ERROR_FILE_INVALID = "Error: Invalid JSON data"
ERROR_FILE_EMPTY = "Error: Empty JSON data"


def load_client(file_name):
    try:
        with open(file_name+".json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(ERROR_FILE_NOT_FOUND)
    except json.JSONDecodeError:
        raise ValueError(ERROR_FILE_INVALID)

    if not data:
        raise ValueError(ERROR_FILE_EMPTY)

    return data


def is_valid_json(file_name):
    try:
        load_client(file_name)
        return True
    except:
        return False
