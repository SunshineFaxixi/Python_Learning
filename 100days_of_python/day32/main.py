##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import os
import random
import smtplib

MY_EMAIL = "xxhan2018@163.com"
MY_PASSWORD = "TXHTVGKIOLEHXVCI"

today = datetime.now()
today_tuple = (today.month, today.day)

all_birth_info = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in all_birth_info.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthday_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as data:
        content = data.read()
        content = content.replace("[NAME]", birthday_person["name"])
        # print(content)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.163.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{content}"
        )



