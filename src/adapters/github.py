import requests

def load_issues(base_uri, owner, repo_name, access_token):
    # Define the headers for authentication
    HEADERS = {"Authorization": f"token {access_token}"}

    # Define the endpoint for issues
    ISSUES_URL = f"{base_uri}/repos/{owner}/{repo_name}/issues"

    # Define the parameter to get the body in Markdown format
    PARAMS = {"media": "application/vnd.github.v3.text+markdown"}

    # Make a GET request to the issues endpoint with the parameter
    response = requests.get(ISSUES_URL, headers=HEADERS, params=PARAMS)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        issues = response.json()
        
        # Define a dictionary to map the label names to numeric values
        label_values = {"high": 4, "medium": 3, "low": 2, "info": 1}

        # Define a function to sort the issues by label value
        def sort_by_label(issue):
            # Get the labels of the issue
            labels = issue["labels"]
            # Initialize the highest label value to zero
            highest_label_value = 0
            # Loop through the labels
            for label in labels:
                # Get the label name and convert it to lower case
                name = label["name"].lower()
                # If the lowercased name is in the label values dictionary, compare the value with the highest label value
                if name in label_values:
                    # If the value is greater than the highest label value, update the highest label value
                    if label_values[name] > highest_label_value:
                        highest_label_value = label_values[name]
            # Return the highest label value
            return highest_label_value

        # Sort the issues by label value in descending order
        issues.sort(key=sort_by_label, reverse=True)

        # Define a dictionary to keep track of the issue numbers for each label
        issue_numbers = {"high": 0, "medium": 0, "low": 0, "info" : 0}

        # Loop through the sorted issues
        for issue in issues:
            # Ensure there's at least one label to process
            if issue["labels"]:
                # Get the label name of the issue and convert it to lower case
                label_name = issue["labels"][0]["name"].lower()
                # If the lowercased label name is in the label values dictionary, increment the issue number for that label
                if label_name in label_values:
                    issue_numbers[label_name] += 1
                    # Generate the prefix with the letter and the number, capitalizing the first letter for consistency
                    prefix = f"[{label_name.capitalize()[0]}-{issue_numbers[label_name]:02d}]"
                    # Add the prefix to the issue title
                    issue["title"] = f"{prefix} {issue['title']}"
        
        # Return the sorted and modified issues
        return issues

    else:
        # Print the status code and error message
        print(f"Request failed: {response.status_code} - {response.reason}")
