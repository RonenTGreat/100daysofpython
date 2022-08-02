import pandas
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    random_number = random.randint(1, 3)
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random_number}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    my_email = os.getenv("EMAIL")
    my_password = os.getenv("PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday \n\n{contents}")




