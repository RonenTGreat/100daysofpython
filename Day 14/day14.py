import random
from game_data import data
from art import logo, vs
from os import system
current_score = 0

random_people_2 = random.choice(data)


print(logo)
game_should_continue = True
while game_should_continue:
  random_people_1 = random_people_2
  random_people_2 = random.choice(data)

  if random_people_1 == random_people_2:
      random_people_2 = random.choice(data)

  print(f"Compare A: {random_people_1['name']}, a {random_people_1['description']}, from {random_people_1['country']}")
  a =random_people_1['follower_count']
  print(a)
  print(vs)

  print(f"Against B: {random_people_2['name']}, a {random_people_2['description']}, from {random_people_2['country']}")
  b = random_people_2['follower_count']
  print(b)

  answer = input("Who has more followers? Tpye 'A' or 'B': ").lower()
  system("CLS")
  print(logo)


  if a > b and answer == 'a':
    current_score += 1
    print(f"You are correct! Current score: {current_score}")

  elif a < b and answer == 'b':
    current_score += 1
    print(f"You are correct! Current score:{current_score}")
  else:
    game_should_continue = False
    print(f"Sorry, that was wrong. Final score: {current_score}.")

