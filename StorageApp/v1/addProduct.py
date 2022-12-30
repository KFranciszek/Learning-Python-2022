class AddProduct():
    def __init__(self):
        self.prods_list  = []

    def add_prod(self, prod):
        self.prods_list.append(prod)

    def save_file_prod(self):
        with open("products_list.txt", "a") as f:
            for i in self.prods_list:
                f.write(i +"\n")

add_prod = AddProduct()
while True:
    insert_prod = input("Enter product (enter 'q' to quit): ").lower()
    if insert_prod == "q":
        break
    add_prod.add_prod(insert_prod)
add_prod.save_file_prod()