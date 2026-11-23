from flask import Flask,request,render_template
from markupsafe import escape
app=Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    if request.method == "POST":
        # parsing parameter dari form (method POST)
        nama = escape(request.form.get("nama", "").strip())
    return render_template("index.html", nama=nama)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <img src='https://upload.wikimedia.org/wikipedia/en/9/97/Barbie_-_Big_City%2C_Big_Dreams.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled.jpg' />"

@app.route("/home")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {escape(name)}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

if __name__ == "__main__":
    app.run(debug=True)