import requests

def load_issues(base_uri, owner, repo_name, access_token):

    # Define the headers for authentication
    HEADERS = {"Authorization": f"token {access_token}"}

    # Define the endpoint for issues
    ISSUES_URL = f"{base_uri}/repos/{owner}/{repo_name}/issues"

    print(ISSUES_URL)