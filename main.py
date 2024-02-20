import smtplib

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/ca9dd2cf4f4c1caebf94").json()


MY_EMAIL = "useremail"
PASSWORD = "password"


@app.route("/")
def home():
    return render_template("index.html", blog_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone_number"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = (
        f"Subject: New Subscriber\n\n{name}\n{email}\n{phone}\n{message}\n",
    )
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
