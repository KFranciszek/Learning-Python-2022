import sqlite3
class dataBases():
    def open_connection(self,base):
        self.conn = sqlite3.connect(base)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()


base='databse_storage.db'
db = dataBases()
db.open_connection(base)
db.close_connection()