import sqlite3


def changeProduct():
    conn = sqlite3.connect('databse_storage.db')
    cursor = conn.cursor()
    name = input("What produkt you want to change? ")
    cursor.execute(f'SELECT * FROM products WHERE name = "{name}"')
    change_product_list = cursor.fetchall()
    print(change_product_list)
    if len(change_product_list) > 1:
        chose_prod = input(f"Witch {name} update, tap barcode? ")
        fields = ['name', 'price', 'amount']
        chose_field = input(f"Witch fild you want to update:  name/price/amount/?")
        update_value = input("Tap update value")
        if chose_field in fields:
            cursor.execute(f'UPDATE products SET {chose_field} = "{update_value}" WHERE name = "{name}"')

    else:
        fields = ['name', 'price', 'amount']
        chose_field = input(f"Witch fild you want to update:  name/price/amount/?")
        update_value = input("Tap update value")
        if chose_field in fields:
            cursor.execute(f'UPDATE products SET {chose_field} = "{update_value}" WHERE name = "{name}"')

    conn.commit()
    conn.close()

changeProduct()

