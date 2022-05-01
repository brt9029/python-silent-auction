from art import logo
import os

print(f"{logo}")


bidders = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidders[name] = price
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if add_bidder == "no":
        bidding_finished = True
        find_highest_bidder(bidders)
    elif add_bidder == "yes":
        os.system('cls')
