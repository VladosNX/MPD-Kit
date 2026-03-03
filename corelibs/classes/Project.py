from corelibs.classes.Configuration import Configuration
import corelibs.configparse.parser as configparser

class Project:
    path = '.'
    config = Configuration()

    def __init__(self, path):
        self.path = path

        config = configparser.parse_config(self.path)