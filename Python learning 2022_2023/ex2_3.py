week = ('Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
d= 13
y = int(input("Enter yers: "))

black = 0
for m in range (1, 13):
    z = (y - 1) if m < 3 else y
    c = 0 if m < 3 else 2
    calender = ((23 * m // 9) + d + 4 + y + (z // 4) - (z // 100) + (z // 400 - c)) % 7
    if calender == 5:
        black+=1

print(black)