import random
from StorageApp.v6.dataBase_def import dataBases
class StorageProducts(dataBases):

    def __init__(self):
        self.base='databse_storage.db'
        self.open_connection(self.base)

    def check_exist_product(self,barcode):
        self.cursor.execute(f'SELECT * FROM products WHERE barcode = "{barcode}"')
        check_exist=self.cursor.fetchall()
        if len(check_exist) >=1:
            return True
        else:
            print("Product dont exist")
            self.conn.close()
            return False

    def check_duble_name(self,name):
        self.cursor.execute(f'SELECT * FROM products WHERE name = "{name}"')
        check_duble=self.cursor.fetchall()
        if len(check_duble) == 0:
            return True
            print("New product")
        else:
            return False

    def create_barcode(self,name):
        self.barcode = ''.join(self.name.replace(' ', '_') + "_" + str(random.randint(10000, 99999)))

    def add_product(self, name, price, amount):
        if not name  or not isinstance(name, str) or not name.strip():
            print("Invalid input for name")
            return
        try:
            price = float(price)
            if price <= 0:
                print("Invalid input for price")
                return
        except (ValueError, TypeError):
            print("Invalid input for price")
            return
        try:
            amount = int(amount)
            if amount < 0:
                print("Invalid input for amount")
                return

        except (ValueError, TypeError):
            print("Invalid input for amount")
            return

        if self.check_duble_name(name) == True:
            self.name = str(name)
            self.price = float(price)
            self.amount = int(amount)
            self.create_barcode(name)
            self.cursor.execute('INSERT INTO products (name,price,amount,barcode) VALUES (?,?,?,?)',
                                (self.name, self.price, self.amount, self.barcode))
            self.cursor.fetchall()
            self.conn.commit()
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

            self.conn.close()




    def update_name(self,name,barcode):
        self.cursor.execute(f'UPDATE products SET name = "{name}" WHERE barcode = "{barcode}"')
        self.cursor.fetchall()
        self.conn.commit()

    def update_price(self,price,barcode):
        self.cursor.execute(f'UPDATE products SET price = "{price}" WHERE barcode = "{barcode}"')
        self.cursor.fetchall()
        self.conn.commit()

    def update_amount(self,amount,barcode):
        self.cursor.execute(f'UPDATE products SET amount = "{amount}" WHERE barcode = "{barcode}"')
        self.cursor.fetchall()
        self.conn.commit()

    def update_product(self,barcode,name=None,price=None,amount=None):
        if self.check_exist_product(barcode) == True:
            if name:
                self.update_name(name,barcode)
            if price:
                self.update_price(price,barcode)
            if amount:
                self.update_amount(amount,barcode)
            self.conn.close()


    def delete_product(self,barcode):
        if self.check_exist_product(barcode) == True:
           self.cursor.execute(f'Delete FROM products WHERE barcode = "{barcode}"')

        else:
            print("Product dont exist")
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

storage = StorageProducts()
storage.add_product(name='coffe VIP premium',price=45,amount=45)
