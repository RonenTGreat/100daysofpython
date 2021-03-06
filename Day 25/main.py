# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# # print(monday.condition)

# cel_to_feh = (int(monday.temp) * (9/5) + 32)
# print(cel_to_feh)

# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_date.csv ")

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
red = 0
gray = 0
black = 0
colour_list = squirrel_data['Primary Fur Color'].to_list()

for colour in colour_list[2:]:
    if colour == "Gray":
        gray += 1
    elif colour == "Black":
        black += 1
    elif colour == "Cinnamon":
        red += 1

colour_squirrel = {
    "Fur Colour": ["grey", "red", "black"],
    "Count": [gray, red, black]
}

data = pandas.DataFrame(colour_squirrel)
data.to_csv("squirrel_count.csv")
