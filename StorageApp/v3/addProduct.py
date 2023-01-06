import json
import sys
def add_prod(prod_list):
    try:
        with open("prod_list.json", "r") as f:
            prod_list = json.load(f)

    except (FileNotFoundError, ValueError,AttributeError,Exception) as e:
        print(f"An error occurred while reading the file: {e}")


    try:

        name = input("Add product name: ")
        for product in prod_list:
            if product["name"] == name:
                print("Product already exists in the list.")
                return

            else:

                price = float(input("Add product price: "))
                ammount = int(input("Add product ammount: "))
                prod_list.append({"name": name, "price": price, "amount": ammount})
                print(prod_list)
            break


    except Exception as e1:
        print(f"An error occurred: {e1}")

    if len(prod_list) == 0:
        return
    else:
        with open("prod_list.json", "w") as f:
            json.dump(prod_list, f)
            return prod_list

add_prod(prod_list)


