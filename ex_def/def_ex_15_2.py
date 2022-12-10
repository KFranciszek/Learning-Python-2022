#Write a program that asks the user for two numbers. Then ask them if they would like to add,
# subtract, divide, or multiply these numbers. Perform the chosen operation on the values,
# showing the operation being performed. Write four functions, one for each mathematical operation.
#Example: add(), subtract(), Multiply(), and Divide()
global score
score =0

def f_add (number1,number2):
    return number1+number2

def f_sub (number1,number2):
    return number1-number2

def f_multi (number1,number2):
    return number1*number2

def f_divi (number1,number2):
    return number1/number2


def f_cal_loop():
    global  score
    print(score)
    operation = int(input("Chose the operation: "))
    number3 = float(input("Enter number 3: "))


    if operation == 1:
        print(f_add(score, number3))
        score =  f_add(score, number3)
    elif operation == 2:
        print(f_sub(score, number3))
        score = f_sub(score, number3)
    elif operation == 3:
        print(f_multi(score, number3))
        score = f_multi(score, number3)
    elif operation == 4:
        print(f_divi(score, number3))
        score = f_divi(score, number3)
    else:
        print("Error")
    con = input('Continue :?')
    if con == "No":
        exit()
    else:
        f_cal_loop()


print("Operation symbol -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")




while True:
    operation = int(input("Chose the operation: "))
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    if operation == 1:
        print(f_add(number1, number2))
        score = score + (f_add(number1, number2))
    elif operation == 2:
        print(f_sub(number1, number2))
        score = score + (f_sub(number1, number2))
    elif operation == 3:
        print(f_multi(number1, number2))
        score = score + (f_multi(number1, number2))
    elif operation == 4:
        print(f_divi(number1, number2))
        score = score + (f_divi(number1, number2))
    else:
        print("Error")

    con = input('Continue :?')
    if con == "No":
        end
    else:
        print(score)
        operation = int(input("Chose the operation: "))
        number3 = float(input("Enter number 3: "))

        if operation == 1:
            print(f_add(score, number3))
            score = f_add(score, number3)
        elif operation == 2:
            print(f_sub(score, number3))
            score = f_sub(score, number3)
        elif operation == 3:
            print(f_multi(score, number3))
            score = _multi(score, number3)
        elif operation == 4:
            print(f_divi(score, number3))
            score = f_divi(score, number3)
        else:
            print("Error")
        con = input('Continue :?')
        if con == "No":
            break
        else:
            f_cal_loop()

