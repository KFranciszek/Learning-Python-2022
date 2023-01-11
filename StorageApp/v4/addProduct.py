import sqlite3
import  random
def addProduct():
    conn = sqlite3.connect('databse_storage.db')
    cursor = conn.cursor()
    name = input("Add product name: ").lower()
    cursor.execute(f'SELECT * FROM products WHERE name = "{name}"')
    check_duble =    cursor.fetchall()
    if len(check_duble) == 0:
        price = float(input("Add product price: "))
        amount = int(input("Add product ammount: "))
        barcode = ''.join(name + "_" + str(random.randint(10000,99999)))
        cursor.execute('INSERT INTO products (name,price,amount,barcode) VALUES (?,?,?,?)',(name,price,amount,barcode))
    else:
        print("Product on the list")
        prod_break = input("Do you want add product with same name but other barcode: yes/no ?")
        if prod_break == 'yes':
            price = float(input("Add product price: "))
            amount = int(input("Add product ammount: "))
            barcode = ''.join(name + "_" + str(random.randint(10000, 99999)))
            cursor.execute('INSERT INTO products (name,price,amount,barcode) VALUES (?,?,?,?)',(name, price, amount, barcode))
        else:
            pass



    conn.commit()
    conn.close()

addProduct()





