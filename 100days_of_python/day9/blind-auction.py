# from replit import clear

loop_continue = True
auction_dict = {}
while loop_continue:
    name = input("What's your name?")
    price = int(input("How much do you bid? $"))
    auction_dict[name] = price
    person_remainer = input("Is there any other person?")
    if person_remainer == "no":
        loop_continue = False
    # elif person_remainer == "yes":
    #     clear()


def find_highest_bidder(bid_record):
    max_price = 0
    for key in bid_record:
        if auction_dict[key] > max_price:
            max_price = auction_dict[key]
            bid_name = key

    print(f"the winner is {bid_name}, the price is {max_price}")

find_highest_bidder(auction_dict)

