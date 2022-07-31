import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("./quotes.txt") as file_data:
    quotes = file_data.readlines()
    quote = random.choice(quotes)

    if day_of_week == 5:
        my_email = "ronenh53@gmail.com"
        my_password = "werilnphzbagjsjt"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ronenhammond@gmail.com",
                                msg=f"Subject:Motivational Quotes \n\n {quote}")


