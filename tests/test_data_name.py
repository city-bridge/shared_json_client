from shared_json_client import SharedJsonClient

def main():
    SERVER_HOST='localhost'
    SERVER_PORT=10000
    CLINET_USER1 = 'user2'

    client = SharedJsonClient(SERVER_HOST,SERVER_PORT,CLINET_USER1)

    print(client.get_data_name_tree())



if __name__ == "__main__":
    main()