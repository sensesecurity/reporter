import markdown

ERROR_FILE_NOT_FOUND = "Error: File not found"

# Placeholders
CLIENT_NAME_PLACEHOLDER = "$$[CLIENT-NAME]$$"
CLIENT_DESC_PLACEHOLDER = "$$[CLIENT-DESCRIPTION]$$"
CLIENT_SCOPE_PLACEHOLDER = "$$[CLIENT-CONTRACT-SCOPE]$$"
CLIENT_CONTENT_LIST_PLACEHOLDER = "$$[CLIENT-CONTRACT-AUDIT-CONTENT-LIST]$$"
CLIENT_ISSUES_PLACEHOLDER = "$$[CLIENT-CONTRACT-AUDIT-ISSUES]$$"


def build_from_template(client, path, template):
    try:
        with open(path + template, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        if CLIENT_NAME_PLACEHOLDER in markdown_content:
            markdown_content = markdown_content.replace(
                CLIENT_NAME_PLACEHOLDER, client.get("client_name")
            )


        print(markdown_content)

        
    except FileNotFoundError:
        print(ERROR_FILE_NOT_FOUND)
