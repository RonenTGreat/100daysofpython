# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }


# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)


# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     Access index and row
#     Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

NATO = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter: row.code for (index, row) in NATO.iterrows()}
print(nato_phonetic_dict)


word = input("Enter a word: ").upper()
result = [nato_phonetic_dict[letter] for letter in word]
print(result)
