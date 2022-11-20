#Find all of the words in a string that are less than 5 letters
str_con = "Find all of the words in a string that are less than 5 letters"

answer = [i for i in str_con.split(" ") if len(i)<5]
print(answer)