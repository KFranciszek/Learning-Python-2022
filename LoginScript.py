name = input('Enter your login')
pasword = input('Enter your pasword')

if (len(name))   < 4:
    print("Twój login musi zawierać minimum 5 znaków")

if (len(pasword)) < 6:
    print('Twoje hasło musi zawierać minimum 6 znaków')
if "!" not in pasword:
    print("Twoje hasło musi zawierać znak specjalny")
# if duża litera
# if znaki specjalne
# if liczby 
