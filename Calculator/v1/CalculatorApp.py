#Write a program that asks the user for two numbers. Then ask them if they would like to add,
# subtract, divide, or multiply these numbers. Perform the chosen operation on the values,
# showing the operation being performed. Write four functions, one for each mathematical operation.
#Example: add(), subtract(), Multiply(), and Divide()

import sys

def f_add (number1,number2):
    return number1+number2

def f_sub (number1,number2):
    return number1-number2

def f_multi (number1,number2):
    return number1*number2

def f_divi (number1,number2):
    return number1/number2

print("Operation symbol -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")

try:
    operation = int(input("Chose the operation: "))
    if operation > 4:
        print("Wrong context of operation ")
        sys.exit(1)
except ValueError:
    print("Must be int ")
    sys.exit(1)

#
try:
    number1 = float(input("Enter number 1: "))
except ValueError:
    print("Must be float.Please enter a valid float for the first number ")
    sys.exit(1)


try:
    number2 = float(input("Enter number 2: "))
except ValueError:
    print("Must be float. Please enter a valid float for the second number ")
    sys.exit(1)

if operation == 1:
    print(f_add(number1,number2))
elif operation == 2:
    print(f_sub(number1, number2))
elif operation == 3:
    print(f_multi(number1, number2))
elif operation == 4:
    print(f_divi(number1, number2))
else:
    print("Error")
