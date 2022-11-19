#Write a Python script to display the various Date Time formats
#a) Current date and time
#b) Current year
#c) Month of year
#d) Week number of the year
#e) Weekday of the week
#f) Day of year
#g) Day of the month
#h) Day of weekimport datetime
from datetime import date
from datetime import datetime

a = datetime.now()
b = date.today()
c = date.today()
d=  datetime.now().strftime("%W")
e=  datetime.now().strftime("%A")
f = datetime.now().strftime("%j")
g = datetime.now().strftime("%d")
print(a,b.year,c.month,d,e,f,g)

