#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

number  = int(input("Enter int number: "))
module = number % 2
if module ==  0:
    print("even number")
else:
    print("odd number")

    