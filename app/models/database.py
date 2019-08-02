import sqlite3
from .sql_queries import tables

class Database:
    def __init__(self):

        self.conn =sqlite3.connect('patwa.db',check_same_thread=False)
        self.c=self.conn.cursor()
    # def connection_(self):
    #     conn = sqlite3.Connection()
    #     c = conn.cursor()
    #     return c

    def execute(self):
        c = self.c
        for table in tables:
            c.execute(table)
    # @staticmethod
    # def register(self, va
    
    def query_(self, query, value):
        try:
            c=self.c
            c.execute(query, (value,))
            m = c.fetchall()
            return m
        except Exception as e :
            return "{}".format(e)

    # def insert_(self, )

def initalize():
    c =Database()
    c.execute()

if __name__ == "__main__":
    initalize()
