#Write a program to create function func1() to accept a variable length of arguments and print their value.

#1
def func1(a):
      return  print(len(a))



func1(a=input("Enter the word: "))

#2
def func1(b):
      counter_word = 0
      for i in b:
            if i != " ":
                  counter_word=counter_word+1
      return print(counter_word)

func1(b=input("Enter the word: "))



