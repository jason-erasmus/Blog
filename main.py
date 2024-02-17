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
        "image_url": i["image_url"],
    }
    blog_objects.append(blog_obj)

# The line `print(blog_objects)` is printing the contents of the `blog_objects` list. It is used to
# display the data retrieved from the API in a readable format in the console.
print(blog_objects)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
