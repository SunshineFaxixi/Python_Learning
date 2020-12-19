import random

work_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(work_list)
print(f"the chosen word is {chosen_word}")
word_length = len(chosen_word)
lives = 6
display = []
for i in range(word_length):
    display += '_'
# print(display)

end_of_game = False
while not end_of_game:
    if not '_' in display:
        end_of_game = True
        print("You win!")
    guess = input("Please guess a letter: \n").lower()
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
    if guess not in display:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

print(display)