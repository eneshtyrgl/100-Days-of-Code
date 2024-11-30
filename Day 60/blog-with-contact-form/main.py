from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import requests
import json
import os

# Load environment variables from .env file
load_dotenv(".venv/.env")

OWN_EMAIL = os.getenv("EMAIL")
OWN_PASSWORD = os.getenv("PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")


# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
try:
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    print("Loaded posts from remote server.")
except Exception as error:
    print(f"An error occurred: {error}")
    with open("Day 59/upgraded-blog/static/assets/data.json") as file:
        posts = json.load(file)
        print("Loaded posts from local file.")


app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_EMAIL, msg=email_message)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
