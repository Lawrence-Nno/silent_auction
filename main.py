def secret_auction():
    """
    This python function runs and powers a secret auction
    :return: A string, The winner of the auction and his/her bid amount.
    """
    gavel_ascii_art = """
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"'"'''"(
                             /_________\\
                             `'-------'`
                           .-------------.
                          /_______________\\
    """

    auction_dict = {}
    # The loop that runs the auction till the last bidder bids
    bidding = True
    # Prints the gavel ascii art above
    print(gavel_ascii_art)
    # Welcome message
    print("Welcome to the Secret Auction Program")

    # Ensures the auction continues till the last bidder
    while bidding:
        new_bidder_name = input("What is your name?\n")

        # Ensures a valid figure is inputted as a bid amount
        while True:
            try:
                new_bidder_amount = float(input("What's your bid?\n"))
            except ValueError:
                print("Your bid has to be a number or a decimal")
            else:
                break
        # Checks if there is a previous bidder with the same name and appends a '_1' if there is.
        if new_bidder_name in auction_dict:
            new_bidder_name = new_bidder_name + '_1'

        # Assigns the bid amount next to the bidder's name in the python dict 'auction_dict' above.
        auction_dict[new_bidder_name] = new_bidder_amount

        # Checks if there is a bidder that is yet to bid
        another_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
        if another_bidder == 'no':
            break

    # Confirms and highest bidder and returns/prints it
    max_key = max(auction_dict, key=auction_dict.get)
    print(f"The highest bidder is {max_key} with ${auction_dict[max_key]}")
    return f"The highest bidder is {max_key} with ${auction_dict[max_key]}"


if __name__ == '__main__':
    secret_auction()


