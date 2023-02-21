import configparser

class Config:
    __instance = None

    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance is not None:
            raise Exception("Only one instance of Config is allowed.")
        else:
            self._conf = configparser.ConfigParser()
            self._conf.read('bot.ini')
            self.TOKEN = self._conf['BOT']['TOKEN']
            Config.__instance = self
            
            
