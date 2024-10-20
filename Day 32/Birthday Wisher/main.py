from datetime import datetime
import pandas
import random
import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASSWORD')


today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("Day 32/Birthday Wisher/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    filepath = f"Day 32/Birthday Wisher/Letter Templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user=MY_EMAIL, password=MY_PASSWORD)
        server.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
