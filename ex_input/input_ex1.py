#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)

import  datetime
datetime.datetime.now()
year=datetime.datetime.now().year
name =input("Enter your name: " )
age = int(input("Enter your  age: " ))

answer = f"My name is: {name} a have {age} year old,  to 100 years  take me {100-age} years, 100 years I will have in year {100-age+year}"
print(answer)


