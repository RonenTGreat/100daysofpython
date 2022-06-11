import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 fro Scissors. "))

computer = random.randint(0, 2)

if player == computer:
  print(items[player])
  print(f"Computer chose: \n {items[computer]}")
  print("You draw")
elif player == 0:
  if computer == 2:
    print(items[player])
    print(f"Computer chose: \n {items[computer]}")
    print("You win")
  else: 
    print(items[player])
    print(f"Computer chose: \n {items[computer]}")
    print("You lose")
elif player == 1:
  if computer == 0:
    print(items[player])
    print(f"Computer chose: \n {items[computer]}")
    print("You win")
  else: 
    print(items[player])
    print(f"Computer chose: \n {items[computer]}")
    print("You lose")
elif player == 2:
  if computer == 1:
    print(items[player])
    print(f"Computer chose: \n {items[computer]}")
    print("You win")
  else:
    print(items[player])
    print(f"Computer chose: \n {items[computer]}")
    print("You lose")
