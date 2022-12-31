#Write a program that asks the user for two numbers. Then ask them if they would like to add,
# subtract, divide, or multiply these numbers. Perform the chosen operation on the values,
# showing the operation being performed. Write four functions, one for each mathematical operation.
#Example: add(), subtract(), Multiply(), and Divide()

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

operation = int(input("Chose the operation: "))
number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

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
