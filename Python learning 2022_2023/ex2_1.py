#1
text = "United Nations Educational, Scientific and Cultural Organization"
for i in text:
    if  i.isupper():
        print(i, end = "")


#2
text = "United Nations Educational, Scientific and Cultural Organization"
shortcut = ''
for i in text:
    if  i.isupper():
        shortcut +=  i

print(f'{shortcut}: {text}')


#3

text = "United Nations Educational, Scientific and Cultural Organization"
text_list = list(text)
[print(i, end= "") for i in text_list if i.isupper]