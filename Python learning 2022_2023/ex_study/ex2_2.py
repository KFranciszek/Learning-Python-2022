week = ('Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

d= int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter yers: "))

z = (y-1) if m < 3  else y
c = 0 if m  < 3 else 2

calender = ((23*m//9) +d +4 +y + (z//4) - (z//100) + (z//400 -c)) % 7

print(week[calender])