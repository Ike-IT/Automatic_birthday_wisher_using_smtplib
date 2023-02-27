import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "lesspython48@gmail.com"
MY_PASSWORD = YOUR PASSWORD


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Wednesday Motivation\n\n{quote}")










# import smtplib
#
# my_email = "agu.odogwu@yahoo.com"
# my_password = "smiles143"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="lesspython48@gmail.com",
#         msg="Subject:Hello\n\nThis this the body of my email"
#     )
#
#

import datetime as dt

now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# # print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=1997, month=5, day=10)
# print(date_of_birth)




