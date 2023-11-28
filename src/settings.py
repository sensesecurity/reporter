import os
import dotenv
dotenv.load_dotenv()

GITHUB_BASE_URL = os.getenv("GITHUB_BASE_URL").strip() 
REPO_OWNER = os.getenv("REPO_OWNER").strip() 
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN").strip() 

TEMPLATE = os.getenv("TEMPLATE").strip()
MARKDOWN_TEMPLATE_PATH = os.getenv("MARKDOWN_TEMPLATE_PATH").strip()
AUDIT_CONFIG_FILES_PATH = os.getenv("AUDIT_CONFIG_FILES_PATH").strip()
REPORT_OUTPUT_PATH = os.getenv("REPORT_OUTPUT_PATH").strip()
