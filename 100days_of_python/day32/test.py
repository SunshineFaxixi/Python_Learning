import datetime as dt
import random
import smtplib

with open("quotes.txt", "rb") as data:
    quote_list = data.readlines()
    # print(quote_list)
    quote = random.choice(quote_list)
    # print(quote)

day_of_week = dt.datetime.now().weekday()
if day_of_week == 6:
    my_email = "xxhan2018@163.com"
    password = "TXHTVGKIOLEHXVCI"

    with smtplib.SMTP("smtp.163.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xxhan2018@163.com",
            msg=f"Subject:keep going\n\n{quote}."
        )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)