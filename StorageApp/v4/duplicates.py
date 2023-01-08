import sqlite3
def duplicates():
    conn = sqlite3.connect('databse_storage.db')
    cursor = conn.cursor()
    cursor.execute("SELECT a.* FROM products a JOIN (SELECT name, COUNT(*) FROM products GROUP BY name HAVING count(*) > 1) b ON a.name = b.name ORDER BY a.name")
    records = cursor.fetchall()

    for record in records:
        print(record)

    conn.close()


duplicates()

