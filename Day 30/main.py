# FileNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dictinary = {"key": "value"}
#     value = a_dictinary["key"]
#     print(value)
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height / 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2

