from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_guess(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make it repeatable.
while game_should_continue:
    # Generate random data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format.
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## Use if statement to check if user is correct.
    is_correct = check_guess(guess, a_follower_count, b_follower_count)

    clear()

    # Give user feedback on their guess.
    if is_correct:
        # Score keeping.
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")

    # Making account at position B become the next account at position A.

    # Clear the screen between rounds.
