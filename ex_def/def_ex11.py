#Write a function count_kwargs , which will return the number of passed so-called 'keyword arguments'
# (arguments that you provide using a variable name) when calling the function.


#Example:
#count_kwargs(a=1, b=2, c=3) -> 3
#count_kwargs(10, a=1, b=2) -> 2

#1
def count_kwargs(**kwargs):
    return len(kwargs)

print(count_kwargs(a=1, b=2, c=3))
count_kwargs2 = count_kwargs(c='', a=1, b=2)

#2
def count_kwargs(*args,**kwargs):
    return len(kwargs)+len(args)

print(count_kwargs(a=1, b=2, c=3))
count_kwargs2 = count_kwargs("Cat",4,c='', a=1, b=2)
print(count_kwargs2)
