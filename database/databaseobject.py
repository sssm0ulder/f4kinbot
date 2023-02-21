import sqlite3

class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Only one instance of Database is allowed.")
        else:
            self.connection = sqlite3.connect('database.sqlite3')
            Database.__instance = self

    def get_forms(data: )
