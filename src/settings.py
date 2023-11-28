import os
import dotenv
dotenv.load_dotenv()

TEMPLATE = os.getenv("TEMPLATE").strip()
MARKDOWN_TEMPLATE_PATH = os.getenv("MARKDOWN_TEMPLATE_PATH").strip()
AUDIT_CONFIG_FILES_PATH = os.getenv("AUDIT_CONFIG_FILES_PATH").strip()
