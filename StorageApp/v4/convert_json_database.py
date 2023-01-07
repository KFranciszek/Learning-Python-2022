import json
import sqlite3
import random

with open('prod_list.json', 'r') as f:
    dane = json.load(f)

conn = sqlite3.connect('databse_storage.db')
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE products (name TEXT, price INTEGER, amount INTEGER, barcode TEXT)")

except:
    pass

for item in dane:
    barcode = ''.join([item["name"].replace(" ","_")] + [str(x) for x in str(random.randint(10000,99999))])
    cursor.execute("INSERT INTO products (name, price, amount, barcode) VALUES (?, ?, ?, ?)", (item['name'], item['price'], item['amount'], barcode))



conn.commit()
conn.close()