alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(cipher_direction, start_text, shift_amount):
  end_text = ""
  for letter in start_text:
    position = alphabet.index(letter)
    if cipher_direction.lower() == 'encode':
      new_position = position + shift_amount
    elif cipher_direction.lower() == 'decode':
      new_position = position - shift_amount
    else:
      print("Please ")
    new_letter = alphabet[new_position]
    end_text += new_letter
  print(f"The {cipher_direction}d text is {end_text}")

caesar(cipher_direction=direction, start_text=text, shift_amount=shift)