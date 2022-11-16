d= int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter yers: "))

z = (y-1) if m < 3  else y
c = 0 if m  < 3 else 2

calender = ((23*m//9) +d +4 +y + (z//4) - (z//100) + (z//400 -c)) % 7

match calender:
    case  0:
         print(f"{d}-{m}-{y} is Sunday")
    case  1:
        print(f"{d}-{m}-{y} is Monday")
    case 2:
        print(f"{d}-{m}-{y} is  Tuesday")
    case 3:
        print(f"{d}-{m}-{y} is Wednesday")
    case 4:
        print(f"{d}-{m}-{y} is Thursday")
    case 5:
        print(f"{d}-{m}-{y} is Friday")
    case 6:
        print(f"{d}-{m}-{y} is Saturday")

