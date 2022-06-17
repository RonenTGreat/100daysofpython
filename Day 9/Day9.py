from bisect import bisect
from unicodedata import name
from art import logo
from os import system

print(logo)
print("Welcome to the secret auction program.")

bids = {}

def intro():
  name = input("What is your name?: ")
  bid = int(input("What's your bid? $"))
  bids[name] = bid

intro()

any_bidder = True
while any_bidder:
  any = input("Are there any other bidders? Type 'yes' or 'no'. \n")

  if any.lower() == 'yes':
    system('CLS')
    intro()
  else:
    any_bidder = False

higher = 0
for name in bids:
  if bids[name] > higher:
    higher = bids[name]

print(f"The winner is {name} with a bid of ${higher}.")