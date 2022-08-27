
#
age  = 20
gender = 'facet'
print ("Mam", age,  "lat")
print (f"Mam {age} lat i jestem {gender}")
print ("Mam {} lat i jestem {}".format(age,gender))
print ("Mam {} lat i jestem {}".format(gender,gender))
#


# Ćwiczenia  string 2
string1 = 'Python'
string2 =  '3.8'
#

print(f"Uczę się jezyka {string1} w wersji {string2}")
print('Uczę się języka {} w wersji {}'.format(string1, string2))
print('Uczę się języka {} w wersji {}'.format(string2, string2))

#Ćwiczenia  string 3
price = 199.8654
ile = "Produkt kosztuje"
print("Produkt kosztuje", price)
print(f"Produkt kosztuje {price}")
#######

#Ćwiczenia string 4
price2 = 39.99
waga = 10
print(f"Cena:{price2} za {waga} kg")

print(10 // 3)
print(10 // 3)

print(25 % 4)

print("cytat")
print('"cytat"')
print("I'm the master")
print("wyrzuć w nowej lini \n to włansie")
print("'I love Python!'")
print("\tI love python")
print('https://www.udemy.com/course/programowanie-w-jezyku-python/learn/lecture/15714542#questions')
print(r'https://www.udemy.com/course/programowanie-w-jezyku-python/learn/lecture/15714542#questions')
import  os
print(os.getcwd())
print('Kocham',  'Python')
nazwa = 'Python'
print("Czesć,", nazwa)

##
kwota_poczatkowa = 1000
stopa_procentowa = 0.05
okres_trwania = 2
fv = kwota_poczatkowa * (1+stopa_procentowa)** okres_trwania
print(fv)

## Approximation of a numerical result

pi = 3.1415926535
print(round(pi))

## Breake the line
print("%.2f"% pi)
print("%.d"% pi)
print("----------------------------------------\nWERSJA: 1.0.1\n----------------------------------------")
print("========================================\nautor: jannowak@poczta.com\ndata: 01-01-2021\n========================================")

## Separator and replace
print("Python","Pool", sep='|')

s = 'summer#time#holiday'
print(s.replace("#", " "))


