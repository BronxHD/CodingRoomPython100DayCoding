import string
import random
low_case_symbols = string.ascii_lowercase
big_letters_symbols = string.ascii_uppercase
numbers = []
for i in range(0, 10):
    numbers.append(str(i))
special_characters = ["!", "\"", "$", "%", "&", "/", "(", "9"]
symbols = [low_case_symbols, big_letters_symbols, numbers, special_characters]

l = 10
u = 2
n = 3
s = 4

ls = [l, u, n, s]
c = 0
password = ""
for i in ls:
    for j in range(0, i):
        index = len(symbols[c])-1
        random_number = random.randint(0, index)
        password = password + symbols[c][random_number]
    c += 1

pass_len = len(password)
for i in range(0, pass_len):
    random_number = range(0, pass_len)
    temp = list(password).


print(password)