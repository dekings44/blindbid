


bids = {}

bidding_completed = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount

            winner = bidder

    print(f'The winner is {winner} with a bid of £{highest_bid}')

while not bidding_completed:

    name = input('What is your name?\n')

    price = int(input('What is your bid? \n£'))

    bids[name] = price

    continued = input('Are there any other bidder? type "yes" or "no".')

    if continued == "no":
        bidding_completed = True
        find_highest_bidder(bids)
    elif continued == "yes":
        print('Please continue')
