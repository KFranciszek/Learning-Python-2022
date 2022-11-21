#Write a Python script to add a key to a dictionary
#1
Sample = {0: 10, 1: 20}
Sample[2] = 30
print(Sample)

#2
Sample = {0: 10, 1: 20}
new_number = {4:40}
Sample.update(new_number)
print(Sample)

