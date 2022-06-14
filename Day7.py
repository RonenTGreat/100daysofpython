import random
from turtle import clear
from hangman_art import logo, stages
from hangman_words import word_list


print(logo)
print("\n")
chosen_word = random.choice(word_list)
lives = 6

display = []

for dash in chosen_word:
    display.append('_')
print(display)

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  print("\033[H\033[J")

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")
    print(stages[lives])

  print(f"{''.join(display)}")
  if "_" not in display:      
    end_of_game = True
    print("You win.")
  
