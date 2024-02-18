from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get("https://api.npoint.io/ca9dd2cf4f4c1caebf94").json()
blog_objects = []
for i in response:
    blog_obj = {
        "id": i["id"],
        "title": i["title"],
        "subtitle": i["subtitle"],
        "body": i["body"],
        "author": i["author"],
        "image_url": i["image_url"],
    }
    blog_objects.append(blog_obj)

# The line `print(blog_objects)` is printing the contents of the `blog_objects` list. It is used to
# display the data retrieved from the API in a readable format in the console.

@app.route("/")
def home():
    return render_template("index.html", posts=blog_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_objects:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html",post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
