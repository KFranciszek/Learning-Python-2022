
#1
from math import  factorial
numbers = int(input("Enter your numeber: "))
numbers_all = 49
opportunity = factorial(numbers_all) //  (factorial(numbers)  * (factorial(numbers_all-numbers)))
print(opportunity)

#2
import  math
numbers = int(input("Enter your numeber: "))
numbers_all = 49

opportunity =  math.comb(numbers,numbers_all)
