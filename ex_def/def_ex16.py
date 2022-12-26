##Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_str (word,x):
    print("Orgin:", word)
    remove_word = word[x:]
    print(remove_word)

remove_str("Write a program to remove characters from a string starting from zero up to n and return a new string.",8)