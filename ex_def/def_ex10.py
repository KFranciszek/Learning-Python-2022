#Write a function count_average that counts the average of any number of passed arguments.

#1
def average_numbers(*args):
    return  sum(args) / len(args)

print(average_numbers(2,2,2,5,6,7,8,44,643))