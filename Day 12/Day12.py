import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def generate_number():
  number = random.randint(1, 101)
  return number

random_number = generate_number()

print(f"Pssst, the correct answer is {random_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

running = True
def game_play(lives):
  while lives > 0:
    guess = int(input("Make a guess: "))
    if guess < random_number:
      print("Too low.")
      lives -= 1
      print(f"Guess again \nYou have {lives} attempts remaining to guess the number.") if lives != 0 else print(
          "You've run out of guesses, you lose.")
      continue
    elif guess > random_number:
      print("Too high.")
      lives -= 1
      print(f"Guess again \nYou have {lives} attempts remaining to guess the number.") if lives != 0 else print(
          "You've run out of guesses, you lose.")
      continue
    elif guess == random_number:
      print(f"You got it! The answer was {random_number}")
      break

if difficulty == 'easy':
  lives = 10
  print(f"You have {lives} attempts remaining to guess the number.")
  game_play(lives)

elif difficulty == 'hard':
  lives = 5
  print(f"You have {lives} attempts remaining to guess the number.")
  game_play(lives)
  
else:
  print("Please enter a valid input.")
