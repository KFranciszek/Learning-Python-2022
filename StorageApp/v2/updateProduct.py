import  json
import  sys
def update_product():
    update_select = input("What product you want  update: ")

    try:
        with open("prod_list.json", 'r') as f:  #We check that the product is on file without changing its

            data_open = f.read()
            data_search = json.loads(data_open)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    except  ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')

    found = False
    update = ""
    fild_update = ['name','price','amount']
    value_upadate = ""
    for i in data_search:
        if i["name"] == update_select:
            update= input(f"Are you sure you want to update {i}  ? ")
            found = True
            if update == "yes":
                fild_update_i = input("Witch fild update:? ")
                if fild_update_i  in fild_update:
                    value_upadate = input("Enter new value: ")
                    i[fild_update_i] = value_upadate
                    print("Value update: ",i)
                else:
                    print("Key not in base")

    with open("prod_list.json", 'w') as f:
        json.dump(data_search, f)




    if not found:
       print("Product dont found")

update_product()