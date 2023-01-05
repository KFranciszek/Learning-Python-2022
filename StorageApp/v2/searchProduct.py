import  json
import  sys
def search_product():
    search_select = input("What product you looking: ")
    try:
        with open("prod_list.json", 'r') as f:
            data_open = f.read()
            data_search = json.loads(data_open)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    except  ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')

    found = False
    search_list = []
    while True:
        for i in data_search:
            if i["name"] == search_select:
                search_list.append(i)
                found = True
        print(search_list)
        break

    if not found:
       print("Product dont found")


search_product()