from kazoo.client import KazooClient, KazooState



class Zookeeper:

    def __init__(self):
        self.zk = KazooClient()

    def start(self):
        self.zk.start()

    def set_env(self, env):
        if env == "prod":
            self.zk.set_hosts('zookeeper.default.svc.cluster.local:2181')
        elif env == "dev":
            self.zk.set_hosts('host.docker.internal:2181')
        else:
            return self.zk.set_hosts('')

    def get_children(self):
        return self.zk.get_children("RoomR/Services/")

    def exists(self, serviceName):
        return self.zk.exists("RoomR/Services/" + serviceName)

    def get_service_name(self, serviceName):
        data, stat = self.zk.get("RoomR/Services/" + serviceName)
        return data.decode("utf-8")
 
    def root_path_exists(self):
        return self.zk.ensure_path("/RoomR/Services")

    def create_ephemeral_node(self, serviceName, serviceAddress):
        self.zk.create("/RoomR/Services/" + serviceName, ephemeral=False, value=serviceAddress.encode('utf-8'))

    def delete_node(self, serviceName):
        self.zk.delete("/RoomR/Services/" + serviceName)


