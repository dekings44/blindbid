


bids = {}

bidding_completed = False

while not bidding_completed:

    name = input('What is your name?\n')

    price = input('What is your bid? \n£')

    bids[name] = price

    continued = input('Are there any other bidder? type "yes" or "no".')

    if continued == "no":
        bidding_completed = True


