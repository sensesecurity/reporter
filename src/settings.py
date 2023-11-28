import os
import dotenv
dotenv.load_dotenv()

MARKDOWN_TEMPLATE_PATH = os.getenv("MARKDOWN_TEMPLATE_PATH")
AUDIT_CONFIG_FILES_PATH = os.getenv("AUDIT_CONFIG_FILES_PATH")
