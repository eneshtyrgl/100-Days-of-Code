from flask import Flask, render_template
import requests
import json

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


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)
