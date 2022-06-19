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


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw🤗."
  elif computer_score == 0:
    return "You lose. Opponent has blackjack😲"
  elif user_score == 0:
    return "You win with a blackjack🤑"
  elif user_score > 21:
    return "You went over, you lose😪"
  elif computer_score > 21:
    return "Opponent went over, you win😋"
  elif user_score > computer_score:
    return "You win🤩"
  else:
    return "You lose😫"

user_cards = []
computer_cards = []
is_game_over = False

for times in range(0, 2):
  user_cards.append(deal_card(cards))
  computer_cards.append(deal_card(cards))

while not is_game_over:
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

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card(cards))
  computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {user_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
