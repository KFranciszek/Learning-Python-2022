import random
from StorageApp.v5.dataBase_def import dataBases

class StorageProducts(dataBases):

    def __init__(self):
        self.base='databse_storage.db'
        self.open_connection(self.base)

    #def add_product()

    #def delete_product()

    #def history_price()

    #def alert_product()


    def show_all(self):
        self.cursor.execute(f"SELECT *  FROM  products")
        self.records = self.cursor.fetchall()

        for self.record in self.records:
            print(self.record)


    def duble_name(self):
        self.cursor.execute("SELECT a.* FROM products a JOIN (SELECT name, COUNT(*) FROM products GROUP BY name HAVING count(*) > 1) b ON a.name = b.name ORDER BY a.name")
        self.records = self.cursor.fetchall()
        for self.record in self.records:
            print(self.record)





