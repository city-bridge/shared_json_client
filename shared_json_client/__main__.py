import sys
from .shared_json_client import SharedJsonClient

def main():
    if len(sys.argv) >= 5:
        host = sys.argv[1]
        port = int(sys.argv[2])
        name = sys.argv[3]
        cmd = sys.argv[4]

        client = SharedJsonClient(host,port,name)
        if cmd == 'stop':
            ret = client.server_stop()
            print(ret)
        elif cmd == 'echo':
            ret = client.echo({'message':sys.argv[5]})
            print(ret)
        else:
            print('unkown command')
    else:
        print('usage [host] [port] [name] [cmd] [args...]')


if __name__ == '__main__':
    main()