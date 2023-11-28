import markdown
import datetime
import os

ERROR_FILE_NOT_FOUND = "Error: File not found"

# Placeholders
CLIENT_NAME_PLACEHOLDER = "$$[CLIENT-NAME]$$"
CLIENT_DESC_PLACEHOLDER = "$$[CLIENT-DESCRIPTION]$$"
CLIENT_SCOPE_PLACEHOLDER = "$$[CLIENT-CONTRACT-SCOPE]$$"
CLIENT_CONTENT_LIST_PLACEHOLDER = "$$[CLIENT-CONTRACT-AUDIT-CONTENT-LIST]$$"
CLIENT_ISSUES_PLACEHOLDER = "$$[CLIENT-CONTRACT-AUDIT-ISSUES]$$"


def build_from_template(client, issues, path, template, output_path):
    try:
        with open(os.path.join(path, template), "r", encoding="utf-8") as f:
            markdown_content = f.read()

        if CLIENT_NAME_PLACEHOLDER in markdown_content:
            markdown_content = markdown_content.replace(CLIENT_NAME_PLACEHOLDER, client.get("name"))

        if CLIENT_DESC_PLACEHOLDER in markdown_content:
            markdown_content = markdown_content.replace(CLIENT_DESC_PLACEHOLDER, client.get("description"))

        # Generate filename with client name and timestamp
        current_time = datetime.datetime.now()
        filename = f"{client.get('name')}_{current_time.strftime('%Y%m%d%H%M%S')}"

        if CLIENT_SCOPE_PLACEHOLDER in markdown_content:
            scope_table_content = "| File | \n"
            scope_table_content += "|-------| \n"

            for contract_url in client.get("scope"):
                scope_table_content += f"| {contract_url} | \n"

            markdown_content = markdown_content.replace(CLIENT_SCOPE_PLACEHOLDER, scope_table_content)

        if CLIENT_CONTENT_LIST_PLACEHOLDER in markdown_content:
            titles = ""

            # Loop through the issues
            for issue in issues:
                # Add a bullet point and the issue title to the string, followed by a newline
                titles += f"- {issue['title']}\n"

            markdown_content = markdown_content.replace(CLIENT_CONTENT_LIST_PLACEHOLDER, titles)

        if CLIENT_ISSUES_PLACEHOLDER in markdown_content:
            bodies = ""

            # Loop through the issues
            for issue in issues:
                # Get the issue title and body
                title = issue["title"]
                body = issue["body"]

                # Format the title as a level 2 heading with a newline
                title = f"## {title}\n"

                # Format the body as a paragraph with a newline
                body = f"{body}\n"

                # Print the title and body
                bodies += title+body

            markdown_content = markdown_content.replace(CLIENT_ISSUES_PLACEHOLDER, bodies)

        # Save the generated Markdown content to the output folder
        with open(os.path.join(output_path, f"{filename}.md"), "w", encoding="utf-8") as output_f:
            output_f.write(markdown_content)

    except FileNotFoundError:
        print(ERROR_FILE_NOT_FOUND)
