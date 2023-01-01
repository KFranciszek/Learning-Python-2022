import  json
def search_product():
    search_select = input("What product you looking: ")
    with open("prod_list.json", 'r') as f:
        data_open = f.read()
        data_search = json.loads(data_open)
    for i in data_search:
        if i["name"] == search_select:
            print(i)
    else:
        print("Product not find")

search_product()