import json
import os

ERROR_FILE_NOT_FOUND = "Error: File not found"
ERROR_FILE_INVALID = "Error: Invalid JSON data"
ERROR_FILE_EMPTY = "Error: Empty JSON data"

audit_config_files_path = os.getenv("AUDIT_CONFIG_FILES_PATH")


def build_path(file_name):
    audit_config_files_path = os.getenv("AUDIT_CONFIG_FILES_PATH")
    return os.path.join(audit_config_files_path, file_name + '.json')


def load_json(file_name):
    file_path = build_path(file_name)
    print(file_path)

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(ERROR_FILE_NOT_FOUND)
    except json.JSONDecodeError:
        raise ValueError(ERROR_FILE_INVALID)

    if not data:
        raise ValueError(ERROR_FILE_EMPTY)

    return data


def is_valid_json(file_name):
    file_path = build_path(file_name)

    try:
        load_json(file_name)
        return True
    except:
        return False