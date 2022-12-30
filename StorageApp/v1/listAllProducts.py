def list_all():
    with open("products_list.txt") as f:
        for i in f:
            print(i.rstrip())

list_all()