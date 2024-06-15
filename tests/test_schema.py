from shared_json_client import SharedJsonClient

def main():
    SERVER_HOST='localhost'
    SERVER_PORT=10000
    CLINET_USER1 = 'user2'

    TEST_DATA_NAME = '/debug/data/test2/'
    TEST_JSON_SCHAME = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "sample json schema",
        "type": "object",
        "required": [
            "member_str",
            "member_int",
        ],
        "properties": {
            "member_str": {
                "type": "string",
            },
            "member_int": {
                "type": "integer",
            }
        }
    }

    client = SharedJsonClient(SERVER_HOST,SERVER_PORT,CLINET_USER1)

    client.write_schema(TEST_DATA_NAME,TEST_JSON_SCHAME)
    print(client.read_schema(TEST_DATA_NAME))
    client.write_data(TEST_DATA_NAME,{"member_str":"test","member_int":1})
    try:
        print(client.write_data(TEST_DATA_NAME,{"member_str":"test","member_int":"error_str"}))
    except Exception as e:
        print(e)
    print(client.read_data(TEST_DATA_NAME))


if __name__ == "__main__":
    main()