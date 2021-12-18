import csv


class Host:
    def __init__(self, args):
        self.name = args[0].strip(" ")
        self.address = args[1].strip((" "))


class FileParser:
    def __init__(self, filename):
        self._filename = filename

    def openHosts(self):
        try:
            return open(self._filename, mode="r")
        except FileNotFoundError as e:
            print(e)
            return None
           
    def getHosts(self):
        hosts = self.openHosts()
        reader = csv.reader(hosts)
        if not hosts:
            return []
        return [ Host(row) for row in reader]

