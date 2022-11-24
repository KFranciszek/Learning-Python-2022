#Palindrom

#1
text = "Co mi dał duch? Cud, ład i moc"
text = list(text)
text[0]=text[-1]
text[-1]=text[0]
text = ''.join(i for i in text)
print(text)

#2
text = "Co mi dał duch? Cud, ład i moc"
palindrom=[i.lower() for i in text if i.isalpha()]
text_p =text=text[::-1]
print("".join(palindrom))