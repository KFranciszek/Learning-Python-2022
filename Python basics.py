
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

#%%
list= ['sport','python','free','time']
string_list_join = "#".join(list)
print(string_list_join )
#%%

x = '123,785,45,5'
l = x.split(',')
print(l)


#%%
#Part 1

#Ask the user for their name, and then greet them using the phrase "Hello, NAME". Of course, NAME should be replaced by the name they've given you!



#Part 2

#Ask the user for their age, and then print out how many months that is. You only need to print the number of months out.

#Remember that for this you'll need to convert the user's input into a number by using int().

ask_age = int(input("What is your age"))*12
print (ask_age)
#%%
age_bolen1 = 34
age_up = age_bolen1 > 31
print (age_up)

#%%
age_bolen1 = 34
age_up = age_bolen1 > 31
print (age_up)
#%%
movies = [
    ("Inside Out", 2015, True),
    ("Toy Story 4", 2019, False),
    ("Up", 2009, True)
]

print(True) 

print(0 == "0") 

print (0==0)


a = [1, 2, 3]
b = a
c =[1, 2, 3] 
print(id(a))  # 139685763327296
print(id(b))  # 139685763327296

print(a == b)  # True
print(a is b)  # True

#%%

x = 0 or 35 
z = 0 and 35
print(x)
print(z)
#%%
A = {1,2,3,4,5,6,7}
B = {1,2,3,4}
C= {6,7,}
D={9}
C.issubset(B)
B.issubset(A)
B.isdisjoint(C)
C.issuperset(A)
A.issuperset(C) 
A.union(C,B,D)
A.intersection(C)

#%% tuple
empty_tuple = tuple()
print(empty_tuple)
a_tuple = ('John', 'Robrt')
b_tuple = ("Warsaw", "New Jork",1,3.56)
mix_tuple = (a_tuple,b_tuple,"Python")
mix_tuple2 = (mix_tuple,  ["Sword","Magic", 56])

#%%List 
print(dir(list))
list_test1 = [1,1,2,3,4,4,5,5.5,"Python 3.10"]
len(list_test1)
list_test2 = list_test1 + ["Sword", 1,1,1,2,2]
list_test3 = list_test2, ["SQL"]
list_test3[0]
list_test3[1]
list_test1[0]
list_test1[-1]
list_test1[-2]
numbers = [1,4,2,5]
letters = ["d","s","f"]
list_test5 = numbers + letters
print(list_test5)
numbers[0]
print(numbers)
numbers[0:4]
numbers[::-1]
numbers[0::3]
list_test1.index("Python 3.10")
ask_list = input("Do you no list?")
list_test1.append(ask_list)
print(list_test1)
numbers.extend("dwa")
numbers.extend([56.64])
print(numbers)
numbers.insert(0, "start_list")
print(numbers)
numbers.index(1)
numbers.index(ask_list)
list_test1.index(ask_list)
list_test1.count(2)
list_test1.count(4)

for i in list_test1:
        print(i,list_test1.count(i))
   
    
from collections import Counter
counter_list_test1 = Counter(list_test1)
print(counter_list_test1)

list_test4  = [1,1,1,1,2,2,3,4,5,6.5,"Sword","Car","Car"]   
counter_list = {}
for i in list_test4:
    if i not in counter_list :
        counter_list [i] = 0
    counter_list [i] += 1
counter_list            
        

