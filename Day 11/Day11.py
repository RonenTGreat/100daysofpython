cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
def deal_card(cards):
  return random.choice(cards)


def calculate_score(player_score):
  if sum(player_score) == 21 and len(player_score) == 2:
    return 0

  for card in player_score:
    if card == 11 and sum(player_score) > 21:
      player_score.remove(card)
      player_score.append(1)
  return sum(player_score)


user_cards = []
computer_cards = []
is_game_over = False

for times in range(0, 2):
  user_cards.append(deal_card(cards))
  computer_cards.append(deal_card(cards))

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")


if user_score == 0 or user_score > 21 or computer_score == 0:
  is_game_over = True
else:
  another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if another_card == 'y':
    user_cards.append(deal_card(cards))
  else:
    is_game_over = True



#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
