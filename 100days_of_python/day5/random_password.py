import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# res = ''
# for i in range(nr_letters):
#     # random_num = random.randint(0, 51)
#     # res += letters[random_num]
#     res += random.choice(letters)
# for j in range(nr_symbols):
#     # random_num_1 = random.randint(0, 8)
#     # res += symbols[random_num_1]
#     res += random.choice(symbols)
# for k in range(nr_numbers):
#     # random_num_2 = random.randint(0, 9)
#     # res += numbers[random_num_2]
#     res += random.choice(numbers)
#
#
# print(res)

password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char
print(password)