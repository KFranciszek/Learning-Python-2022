import random
from StorageApp.v5.dataBase_def import dataBases

class StorageProducts(dataBases):

    def __init__(self):
        self.base='databse_storage.db'
        self.open_connection(self.base)

    def add_product(self,name,price,amount):
        self.cursor.execute(f'SELECT * FROM products WHERE name = "{name}"')
        self.check_duble = self.cursor.fetchall()
        if len(self.check_duble) == 0:
            self.name = name
            self.price = price
            self.amount = amount
            barcode = ''.join(self.name.replace(' ','_') + "_" + str(random.randint(10000, 99999)))
            self.cursor.execute('INSERT INTO products (name,price,amount,barcode) VALUES (?,?,?,?)',
                           (name, price, amount, barcode))
            self.cursor.fetchall()
            self.conn.commit()
            self.conn.close()

        else:
            add_duble= str(input("Product duble on the list, you want to add with the same same name but other barcode? "))
            if add_duble == 'y':
                self.name = name
                self.price = price
                self.amount = amount
                barcode = ''.join(self.name.replace(' ','_') + "_" + str(random.randint(10000, 99999)))
                self.cursor.execute('INSERT INTO products (name,price,amount,barcode) VALUES (?,?,?,?)',
                                    (name, price, amount, barcode))
                self.cursor.fetchall()
                self.conn.commit()
                self.conn.close()
            else:
                self.conn.close()



    def update_product(self,barcode,name=None,price=None,amount=None):
        self.cursor.execute(f'SELECT * FROM products WHERE barcode = "{barcode}"')
        up_product=self.cursor.fetchall()
        if len(up_product) == 1:
            if name:
                self.cursor.execute(f'UPDATE products SET name = "{name}" WHERE barcode = "{barcode}"')
                self.cursor.fetchall()
                self.conn.commit()
                self.conn.close()

            if  price:
                self.cursor.execute(f'UPDATE products SET price = "{price}" WHERE barcode = "{barcode}"')
                self.cursor.fetchall()
                self.conn.commit()
                self.conn.close()

            if  amount:
                self.cursor.execute(f'UPDATE products SET amount = "{amount}" WHERE barcode = "{barcode}"')
                self.cursor.fetchall()
                self.conn.commit()
                self.conn.close()
        else:
            print("Product dont exist")
            exit()

    def delete_product(self,barcode):
        self.cursor.execute(f'Delete FROM products WHERE barcode = "{barcode}"')
        self.conn.commit()
        self.conn.close()


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


    def search_product(self,search_field=None,search_value=None):
        if search_field not in ['name','price','amount','barcode']:
            print("Field dont exist")
            return
        self.cursor.execute(f"SELECT * FROM products WHERE {search_field} = '{search_value}'")
        search_result = self.cursor.fetchall()
        print(search_result)
        self.conn.commit()
        self.conn.close()

