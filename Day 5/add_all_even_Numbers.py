end_value = int(input("Bis wohin sollen die geraden Zahlen addiert werden?"))
summe = sum(range(0, end_value, 1)) - 50**2
summe2 = sum(range(0, end_value, 2))
print(f"summe:{summe} summe2:{summe2}")