import random
options = ["stein", "schere", "papier"]
random_zahl = random.randint(0, 2)
eingabe = int(input("stein(1), schere(2), papier(3): "))-1

spieler = options[eingabe]
computer = options[random_zahl]

if spieler == computer:
    print("gleich")
elif (spieler == "schere" and computer == "papier") or (spieler == "stein" and computer == "schere") or (spieler == "papier" and computer == "stein"):
    print(f"computer: {computer} vs spieler: {spieler}\nSpieler hat gewonnen")
else:
    print(f"computer: {computer} vs spieler: {spieler}\nComputer hat gewonnen")



