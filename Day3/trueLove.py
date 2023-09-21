# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

full_name = str(name1+name2).lower()
true = {"t", "r", "u", "e"}
love = {"l", "o", "v", "e"}
t = 0
l = 0
for i in true:
    for j in full_name:
        if i == j:
            t+=1

for i in love:
    for j in full_name:
        if i == j:
            l+=1

score = int(str(t)+str(l))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")