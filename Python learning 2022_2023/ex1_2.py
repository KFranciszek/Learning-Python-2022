balance  = float(input("Enter your balance: "))
rate =  float(input("Enter your account rate: "))
rate_numer = rate / 100
years = int(input("How  log  will you put money: "))

interest  = round(balance * years  * rate_numer,2)
invest = round(balance + balance * years  * rate_numer,2)
print(f"Your deposit increase by  {interest}  You wi ll have {invest}")