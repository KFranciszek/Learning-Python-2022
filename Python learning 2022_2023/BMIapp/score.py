# def scoreBMI_data (bmi):

#     if bmi <= 19:
#         return "Niedowaga"

#     elif  bmi <= 25:
#         return "Norma"

#     elif bmi >= 26:
#         return "Nadwaga"

    if bmi <= 19 and  gender == 'Male':
        return "Niedowaga"
    elif bmi <= 19 and gender == 'Famale':
        return "Norma"
    elif bmi < 18 and gender == 'Famale':
        return "Niedowaga"
    if bmi <= 25 and gender == 'Male':
        return "Norma"
    elif bmi <= 25 and gender == 'Famale':
        return "Nadwaga"
    if bmi >= 26 and gender == 'Male':
        return "Nadwaga"
    elif bmi >= 26 and gender == 'Famale':
        return "Otyłość"
