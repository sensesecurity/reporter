import sys
import dotenv
import src.adapters.json as audit_json

dotenv.load_dotenv()


CLIENT_NOT_FOUND_ERROR = ("Error: When running reporter, make sure to inform the client config file python3 main.py [client-file]")


def main():
    if len(sys.argv) < 2:
        raise Exception(CLIENT_NOT_FOUND_ERROR)

    client = audit_json.load("sr")



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)