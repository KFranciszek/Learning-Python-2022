from scoreBMI import scoreBMI_data
team = []
def DicBMI_data():
    member = True
    while member:
        gender = input('Podaj płeć')  
        name = input('Podaj imie')
        while True:
            try:
                weight = int(input('Podaj swoją wage'))
                break
            except ValueError:
                print("ERROR")
        while True:
           try:
                height = float(input('Podaj swój wzrost'))
                break
           except ValueError:
                print("ERROR")
        bmi = weight//(2*height)
        bmiinfo2=scoreBMI_data(bmi, gender)

        bmiDic = {'gender': gender,'name': name, 'weight': weight, 'height':height,'bmi': bmi, 'score': bmiinfo2}

        team.append(bmiDic)

        pytanie = input('Czy policzyć jeszcze raz  T/N')
        if pytanie == 'N':
            member = False

    return  (team,member)


BMI_data=DicBMI_data()
