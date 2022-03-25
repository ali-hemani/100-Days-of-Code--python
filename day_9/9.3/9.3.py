import art

print(art.logo)
print("Welcome to the secret auction program.")
should_continue = True
all_bids = {}
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    all_bids[name] = bid
    input_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if input_continue.lower() == "no":
        should_continue = False
highest_bid = 0
highest_bid_name = ""
for key in all_bids:
    if highest_bid < all_bids[key]:
        highest_bid = all_bids[key]
        highest_bid_name = key
print(f"The highest bid is from {highest_bid_name} for ${highest_bid}")