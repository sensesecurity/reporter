import markdown

ERROR_FILE_NOT_FOUND = "Error: File not found"

def build_from_template(client, path, template):
    with open(path+template, 'r', encoding='utf-8') as f:
        markdown_content = f.read()