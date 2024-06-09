from cbpyjsonrpc import JsonRPCClientUDP

class SharedJsonClient:
    lock_name:str
    _json_rpc_client:JsonRPCClientUDP

    def __init__(self,host:str,port:int,lock_name:str) -> None:
        self.lock_name = lock_name
        self._json_rpc_client = JsonRPCClientUDP(host,port)
        self._json_rpc_client.settimeout(4)
    
    def echo(self,params:dict)->dict:
        return self._json_rpc_client.request_method('echo',params)

    def echo_error(self):
        return self._json_rpc_client.request_method('echo_error',None)
    
    def server_stop(self):
        return self._json_rpc_client.request_method('server_stop',None)
    
    def debug_notify(self,text_list:list):
        return self._json_rpc_client.request_notify('debug_notify',text_list)

    def set_data(self,data_name:str,data:dict):
        return self._json_rpc_client.request_method('set_data',{
            'data_name':data_name,
            'data':data,
            'lock_name':self.lock_name
        })
    def get_data(self,data_name:str):
        return self._json_rpc_client.request_method('get_data',{
            'data_name':data_name,
            'lock_name':self.lock_name
        })
    def write_data(self,data_name:str,data:dict):
        return self._json_rpc_client.request_method('write_data',{
            'data_name':data_name,
            'data':data,
            'lock_name':self.lock_name
        })
    def read_data(self,data_name:str):
        return self._json_rpc_client.request_method('read_data',{
            'data_name':data_name,
            'lock_name':self.lock_name
        })
    def lock_data(self,data_name:str):
        return self._json_rpc_client.request_method('lock_data',{
            'data_name':data_name,
            'lock_name':self.lock_name
        })
    def release_data(self,data_name:str):
        return self._json_rpc_client.request_method('release_data',{
            'data_name':data_name,
            'lock_name':self.lock_name
        })

