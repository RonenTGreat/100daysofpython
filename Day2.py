

print("Welcome to the tip calculator.")

totatl_bill = input("What was the total bill? $")
totatl_bill = float(totatl_bill)

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

percentage = float(percentage / 100)

tip = (totatl_bill / number_of_people) + (totatl_bill / number_of_people * percentage)

tip = round(tip, 2)
tip = "{:.2f}".format(tip)

print(f"Each person should pay: ${tip}")
