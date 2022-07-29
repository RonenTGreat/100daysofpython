import smtplib

my_email = "ronenh53@gmail.com"
my_password = "werilnphzbagjsjt"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ronenhammond@gmail.com",
                        msg="Subject:Greeting \n\nThis is the body of my email.")
