import pymysql
from configparser import ConfigParser


class Database:
    def __init__(self, config_file='config.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)
        self.connection = self.connect_db()
        self.dbcursor = self.connection.cursor()

    def connect_db(self):
        return pymysql.connect(
            host=self.config.get('Database', 'host', fallback='localhost'),
            user=self.config.get('Database', 'user', fallback='root'),
            password=self.config.get('Database', 'password', fallback=''),
            database=self.config.get('Database', 'database', fallback='movies_db')
        )

    def commit_db(self):
        self.connection.commit()

    def close_db(self):
        self.dbcursor.close()
        self.connection.close()