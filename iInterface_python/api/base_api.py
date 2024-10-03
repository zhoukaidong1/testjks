
import requests

class BaseApi:

    def request(self,datas: dict):
        #为了多协议支持，或者将来协议变更，或者将来方便用其他的http库，比如requests切换到其他lib
        if "url" in datas:
            return  self.http_request(datas)
        if "rpc" == datas.get("protocol"):
            return self.rpc_request(datas)

    def http_request(self,datas):
        r = requests.request(**datas)
        return r


    def rpc_request(self,datas):
        pass


    def tcp_request(self):
        pass