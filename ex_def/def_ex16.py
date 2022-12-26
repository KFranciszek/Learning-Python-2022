##Write a program to remove characters from a string starting from zero up to n and return a new string.

#1
def remove_str (word,x):
    print("Orgin:", word)
    remove_word = word[x:]
    print(remove_word)

remove_str("Write a program to remove characters from a string starting from zero up to n and return a new string.",8)

#2
def remove_str (word,x,y):
    print("Orgin:", word)
    remove_word = word[x:y]
    print(remove_word)

remove_str("Write a program to remove characters from a string starting from zero up to n and return a new string.",8,-13)

