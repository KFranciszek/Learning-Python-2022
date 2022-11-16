# Write a Python program to lowercase first n characters in a string
st = input('Enter word: ')
if st[0].isupper():
    st = st[0].lower() + st[1:]

print(st)
