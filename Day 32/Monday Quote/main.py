import datetime as dt
import smtplib
import random
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".venv/.env")

MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASSWORD')


# Get current date and check if it's Monday (weekday == 0)
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    # Open and read quotes from the text file
    with open(r"Day 32/Monday Quote/quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).encode('ascii', 'ignore').decode('ascii')

    # Send email with the Monday motivation quote
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(user=MY_EMAIL, password=MY_PASSWORD)
        server.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
        print("Email sent successfully!")
