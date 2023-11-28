import sys
import src.settings as settings
import src.adapters.json as json_adapter
import src.adapters.markdown as markdown_adapter


CLIENT_NOT_FOUND_ERROR = (
    "Error: When running reporter, make sure to inform the client config file: python3 main.py [client-file]"
)

def main():

    if len(sys.argv) < 2:
        raise Exception(CLIENT_NOT_FOUND_ERROR)

    client = json_adapter.load_client(
        settings.AUDIT_CONFIG_FILES_PATH + sys.argv[1] + ".json"
    )

    # LOAD GITHUB ISSUES OBJECT

    markdown_adapter.hi(settings.MARKDOWN_TEMPLATE_PATH)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
