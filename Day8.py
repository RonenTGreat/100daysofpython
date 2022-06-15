from unittest import result
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(cipher_direction, start_text, shift_amount):
  end_text = ""
  if cipher_direction.lower() == 'encode' or cipher_direction.lower() == 'decode':
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        if cipher_direction.lower() == 'encode':
          new_position = position + shift_amount
          end_text += alphabet[new_position]
        elif cipher_direction.lower() == 'decode':
          new_position = position - shift_amount      
          end_text += alphabet[new_position]
      else:
        end_text += char
    print(f"The {cipher_direction}d text is {end_text}")
  else:
    print("Please enter 'encode' or 'decode'.")


should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()

  if result == "no":
    should_continue = False
    print("Thank you. Goodbye")