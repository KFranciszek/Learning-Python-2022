#1
#Take a list, say for example this one:  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras
#2 Write this in one line of Python.

#1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i < 5:
        b.append(i)
print(b)


#2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [i for i in a if i <5]
print(b)

