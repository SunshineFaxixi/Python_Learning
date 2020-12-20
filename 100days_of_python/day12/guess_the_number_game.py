import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess == answer:
        print("You are right")
    elif guess > answer:
        print("Too high")
        return turns - 1
    else:
        print("Too low")
        return turns - 1


# Make function to choose the difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
    return turns


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    # Repeat the guessing functionality if they get it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess the number
        guess = int(input("Please guess a number: "))

        # Track the number of turns and redundency if they get wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose")
            return


game()