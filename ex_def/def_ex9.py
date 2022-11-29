#Using the map() function and a lambda expression, get a list containing the first three letters of each city.
#Print the resulting list to the console.

#1 Without lambda
cities = ['Warsaw', 'London', 'Berlin', 'New York']
for i in cities:
    print(i[0:4], end=' ')


#2 list comp

city1 = [i[0:4] for i in cities]
print(city1)


#3 lambda
cities = ['Warsaw', 'London', 'Berlin', 'New York']
list(map(lambda i: i[0:3], cities))
print(list(map(lambda i: i[0:3], cities)))

