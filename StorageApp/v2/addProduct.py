import json
prod_list = []
def add_prod(prod_list):
    name = input("Add product name: ")
    price = float(input("Add product price: "))
    ammount = int(input("Add product ammount: "))
    prod_list.append({"name": name, "price": price, "amount": ammount})
try:
    with open("prod_list.json", "r") as f:
        prod_list = json.load(f)
except:
    pass


def save_prod_do(prod_list):
   with open("prod_list.json", "w") as f:
        json.dump(prod_list, f)


add_prod(prod_list)
save_prod_do(prod_list)
