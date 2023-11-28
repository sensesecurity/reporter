import json

audit_config_files_path = os.getenv("AUDIT_CONFIG_FILES_PATH")

def build_path(file_name):
    audit_config_files_path = os.getenv("AUDIT_CONFIG_FILES_PATH")
    return os.path.join(audit_config_files_path, file_name)

def load_json(file_name):
    file_name = build_path(file_name);

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_name}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON data in file: {file_name}")

    if not data:
        raise ValueError(f"Empty JSON data in file: {file_name}")

    return data

def is_valid_json(file_name):
    file_name = build_path(file_name);

    try:
        load_json(file_name)
        return True
    except:
        return False