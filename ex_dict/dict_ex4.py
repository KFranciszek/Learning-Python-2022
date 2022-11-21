#Write a Python script to check whether a given key/value  already exists in a dictionary.
#1
dict_long = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
check=dict_long.get(5)

#2
dict_long = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
if 5 in dict_long.keys():
    print("Key in dictionary")
else:
    print("Key not in dictionary")


#3

dict_long = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
if 50 in dict_long.values():
    print("Key in dictionary")
else:
    print("Key not in dictionary")

