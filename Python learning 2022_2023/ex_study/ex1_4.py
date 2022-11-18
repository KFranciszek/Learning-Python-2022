#1 BMI Programm
weight  =  float(input("Enter your weight: "))
height = float(input("Enter your height:  " ))
bmi = round(weight /  height **2, 2)


if bmi < 16:
    score = "starvation"
elif bmi >= 16 and bmi <= 16.99:
    score = "outgrowth"
elif bmi >= 17 and bmi  <= 18.49:
    score = "underweight"
elif bmi >= 18.50 and bmi <= 24.99:
    score = "Good weight"
elif bmi >= 25 and bmi < 30:
    score = "overweight"

answer = f"Your bmi score is {bmi} you are {score}"

print(answer)

