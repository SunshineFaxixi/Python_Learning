# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()  # no output


# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# play computer
# year = int(Input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("Your are a Gen z.")


# age = int(Input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")


# pages = 0
# word_per_page = 0
# pages = int(Input("Number of pages: "))
# word_per_page = int(Input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}0
# print(total_words)


# use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
