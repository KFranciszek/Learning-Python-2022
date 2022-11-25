#Write a function print_ odd that returns a list of odd numbers greater than zero and less than 20.
def odd_numbers(odd):
    even = []
    for i in range(odd+1):
        if i % 2 != 0:
            even.append(i)
    return  print(even)


odd_numbers(20)