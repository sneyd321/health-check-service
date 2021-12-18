import requests


class RequestManager:
    def __init__(self, zk):
        self.zk = zk
 
    def get(self, host):
        try:
            response = requests.get("http://" + host.address + "/Health")
            if response.ok and self.zk.exists(host.name):
                print(host.name + " Exists")
                return
            if response.ok and not self.zk.exists(host.name):
                self.zk.create_ephemeral_node(host.name, host.address)
                print(host.name + " Node Created")
                return
            if not response.ok and self.zk.exists(host.name):
                self.zk.delete_node(host.name)
                print(host.name + " Node Deleted")
                return
        except requests.exceptions.ConnectionError:
            if self.zk.exists(host.name):
                self.zk.delete_node(host.name)
            print(host.name + " No Found")
            return