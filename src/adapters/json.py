import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON data in file: {file_path}")

    if not data:
        raise ValueError(f"Empty JSON data in file: {file_path}")

    return data

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def is_valid_json(file_path):
    try:
        load_json(file_path)
        return True
    except:
        return False