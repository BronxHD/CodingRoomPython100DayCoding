year = int(input("Gib ein Jahr ein: "))
if (year % 4 == 0 and (not year % 100 == 0 or year%400 == 0)):
    print("leap year")
else:
    print("no leap year")

