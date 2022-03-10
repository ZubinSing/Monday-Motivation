import smtplib
import datetime as dt
import random

my_email = "randomguyishere2001@gmail.com"
password = "foremail2001"
receiver = "shootygun20@gmail.com"

now = dt.datetime.now()
monday = dt.datetime(day=0)
today = now.weekday()
if today == monday:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Here is some Monday Motivation\n\n{quote}")