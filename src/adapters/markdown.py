import markdown

ERROR_FILE_NOT_FOUND = "Error: File not found"

def build_from_template(path, data):
    with open('markdown_file.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()