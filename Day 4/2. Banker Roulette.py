# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
lenth = len(names)
random_number = random.randint(0, lenth-1)
chosen_name = names[random_number]
print(f"{chosen_name} is going to buy the meal today")

