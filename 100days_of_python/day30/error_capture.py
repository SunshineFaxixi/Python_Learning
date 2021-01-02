# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["akhdi"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     connent = file.read()
#     print(connent)
# finally:
#     file.close()
#     print("File was closed.")


# height = float(input("Height:"))
# weight = int(input("Weight:"))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     global fruits
#     try:
#         fruits = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruits + " pie")
#
# make_pie(2)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_like = 0
for post in facebook_posts:
    try:
        total_like += post['Likes']
    except KeyError:
        pass

print(total_like)