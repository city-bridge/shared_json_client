from shared_json_client import SharedJsonClient

SERVER_HOST='localhost'
SERVER_PORT=10000

client = SharedJsonClient(SERVER_HOST,SERVER_PORT,'user1')
client2 = SharedJsonClient(SERVER_HOST,SERVER_PORT,'user2')

print(client.release_data('/debug/data/test/'))
print(client2.release_data('/debug/data/test/'))

client.debug_notify(['aaa','bbb'])
#print(client.echo({'test':'tst'}))
#client.set_data('debug.data.test',[1,2,3])
print(client.get_data('/debug/data/test/'))
client.write_data('/debug/data/test/',["aaa"])
print(client.read_data('/debug/data/test/'))
print(client.read_data('/debug/data/undefined/'))
print(client2.lock_data('/debug/data/test/'))
print(client.lock_data('/debug/data/test/'))
