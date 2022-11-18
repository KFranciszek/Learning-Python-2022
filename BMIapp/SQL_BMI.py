import psycopg2
from dicBMI  import team

try:
    for bmiDic  in team:
        conn = psycopg2.connect("dbname='XYZ' user='XYZ' host='localhost' password='XYZ'")
        print("Dobre połączenie do bazy postgres")
        cur = conn.cursor()
        cur.execute("""INSERT INTO bmi(name,weight,height,bmi, gender) VALUES (%(name)s,%(weight)s, %(height)s,%(bmi)s,%(gender)s)""", bmiDic)
        conn.commit()
        cur.close()

except:
    print ("I am unable to connect to the database")
