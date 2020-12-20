# game_level = 3
# enemies = ['aaa', 'bbb', 'ccc']
# def create_enermy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#
# # print(new_enemy)


enermies = 1
def increase_enermies():
    global enermies
    enermies += 1
    print(f"enermies inside function: {enermies}")


increase_enermies()
print(f"enermies outside function: {enermies}")