import random

names_str = input("please entry the names with comma: \n")
names_list = names_str.split(", ")
# print(names_list)
# index = random.randint(0, len(names_list) - 1)
# print(f"{names_list[index]} will pay the bill")

random_name = random.choice(names_list)
print(f"{random_name} will pay the bill")