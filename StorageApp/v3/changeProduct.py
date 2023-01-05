import  sys
import json
class changeProducts():

    def load_data(self):
        try:
            with open("prod_list.json", 'r') as f:
                self.data_open = f.read()
                self.data_search = json.loads(self.data_open)

        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

        except  ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')

    # Method to update or delete product
    def change_product(self):
        self.change_option = ['delete','update']
        self.change_option_answer = input("What action you want to do:delete/update ").lower()

        # delete product logic
        found = False
        if self.change_option_answer == "delete":
            self.delete_item = ""
            self.delete_select = input("What product you want  delete: ")
            for i in self.data_search:
                if i["name"] == self.delete_select:
                    self.delete_item = input(f"Are you sure you want to remove {i}  ? ")
                    found = True
            if self.delete_item == "yes":
                self.data_search.remove(i)
                print("Product delete")


        # delete update logic
        elif self.change_option_answer == "update":
            self.update_select = input("What product you want  update: ")
            self.update = ""
            self.fild_update = ['name', 'price', 'amount']
            self.value_upadate = ""
            for i in self.data_search:
                if i["name"] == self.update_select:
                    self.update = input(f"Are you sure you want to update {i}  ? ")
                    found = True
                    if self.update == "yes":
                        self.fild_update_i = input("Witch fild update:? ")
                        if self.fild_update_i in self.fild_update:
                            self.value_upadate = input("Enter new value: ")
                            i[self.fild_update_i] = self.value_upadate
                            print("Value update: ", i)
                        else:
                            print("Key not in base")
        if not found:
            print("Product dont found")

    def save_data(self):
        with open("prod_list.json", 'w') as f:
            json.dump(self.data_search, f)



change_product = changeProducts()

change_product.load_data()
change_product.change_product()
change_product.save_data()
