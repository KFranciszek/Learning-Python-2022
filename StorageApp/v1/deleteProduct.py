def delete_product():
    delete_item = input("Enter item to delete: ").lower()
    with open("products_list.txt", "r") as f:
          products = f.readlines()
          for i in products:
              if delete_item in i:
               print("Product on the list")
               delete_ask = input("You what to delete if yes tab yes quir tab q ?  ")
               if delete_ask == "q":
                   break
               else:
                   products.remove(i)
                   with open("products_list.txt", "w") as f:
                       f.write("\n".join(products))
                       print("Product delete")





delete_product()