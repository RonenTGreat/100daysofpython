PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as starting_file:
    sentences = starting_file.read()
    for name in names:
        name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
            letter.write(sentences.replace(PLACEHOLDER, name))
