# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# new_numbers
# Out[4]: [2, 3, 4]
# name = "Angela"
# new_list = [letter for letter in name]
# new_list
# Out[7]: ['A', 'n', 'g', 'e', 'l', 'a']
# numbers = [x ^ 2 for x in range(1, 5)]
# numbers
# Out[9]: [3, 0, 1, 6]
# numbers = [x * x for x in range(1, 5)]
# numbers
# Out[11]: [1, 4, 9, 16]
# numbers = [2 * x for x in range(1, 5)]
# numbers
# Out[13]: [2, 4, 6, 8]
# numbers = [2 * x for x in range(1, 5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# names
# Out[16]: ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# new_names = [name.upper() for name in names if len(name) > 5]
# new_names
# Out[18]: ['CAROLINE', 'ELEANOR', 'FREDDIE']

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)
# result = [num for num in numbers if num % 2 == 0]
# print(result)

with open("file1.txt") as f1:
    file1_list = f1.readlines()

with open("file2.txt") as f2:
    file2_list = f2.readlines()

result = [int(num.strip()) for num in file1_list if num in file2_list]
print(result)