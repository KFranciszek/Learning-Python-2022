import sqlite3

def show_all():
    conn = sqlite3.connect('databse_storage.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT *  FROM  products")
    records = cursor.fetchall()

    for record in records:
        print(record)

    conn.close()


show_all()

