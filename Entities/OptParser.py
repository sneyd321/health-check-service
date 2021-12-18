from optparse import OptionParser





class Command:


    def __init__(self):
        self.parser = OptionParser()
        self.filename = self.parser.add_option("-f", "--filename", action="store", type="string", dest="filename")
        self.env = self.parser.add_option("-e", "--environment", action="store", type="string", dest="environment")


    def getFilename(self):
        options, args = self.parser.parse_args()
        return options.filename

    def getEnv(self):
        options, args = self.parser.parse_args()
        return options.environment