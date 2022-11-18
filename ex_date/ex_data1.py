# Write a Python program to calculate number of days between two dates.

#1
import datetime
data2 = datetime.date(2022,11,25)
data1 = datetime.date(2022,11,18)
date_left = (data2-data1)
print(date_left.days)

