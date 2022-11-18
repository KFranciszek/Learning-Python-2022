#Write a Python script to display the various Date Time formats
#a) Current date and time
#b) Current year
#c) Month of year
#d) Week number of the year
#e) Weekday of the week
#f) Day of year
#g) Day of the month
#h) Day of week

import datetime
from datetime import date

a = datetime.datetime.now()
b = date.today()
c = date.today()
#d=  date.weekday()
e=  date.day
print(a,b.year,c.month, end="\n")