from Entities.OptParser import Command
from Entities.Kazoo import Zookeeper
from Entities.Models import FileParser
from Entities.RequestManager import RequestManager

command = Command()
zookeeper = Zookeeper()
fp = FileParser(command.getFilename())
manager = RequestManager(zookeeper)

zookeeper.set_env(command.getEnv())
zookeeper.start()
zookeeper.root_path_exists()
 
hosts = fp.getHosts()

for host in hosts:
    manager.get(host)

print(zookeeper.get_children())







