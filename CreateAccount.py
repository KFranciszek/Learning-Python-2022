import psycopg2
import  random
import base64
symbol =['!','@',"#","$","%","&","*","/","?"]
userid = random.getrandbits(10)
def account ():

    login = str(input("Your email"))

    while True:
        password = str(input("Your paswords, Must have 6 char, big lliter, special symbol"))
        if len(password)  < 6:
            print("Pasword must have minimum 6")

        elif sum(1 for i in password if i.isupper()) < 1:
            print("Password must have one big litter")
        elif sum(1 for i in password if i in symbol) < 1:
            print("Password must have special symbol")
        else:
            break

    conn = psycopg2.connect("dbname='bmi' user='xxx' host='xx' password='xxx'")
    print("Succes connect")
    cur = conn.cursor()
    password=base64.b64encode(bytes(password, 'utf8'))
    cur.execute("""INSERT INTO users(login, password, userid) VALUES (%(login)s,%(password)s,%(userid)s)""",
                {'login': login, 'password': password, 'userid':userid})
    conn.commit()
    cur.close()
  

account()
