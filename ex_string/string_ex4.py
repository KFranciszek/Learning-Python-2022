#Write a Python program to accept a filename from the user and print the extension of that.

file = input("Enter file name: ")
f_ex = file.split('.')
f_p = f'File name is {file} and extension is {f_ex[-1]}'
print(f_p)
