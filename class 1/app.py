
from flask import Flask, render_template

main = Flask(__name__)


@main.route("/")
def homepage():
    return render_template("home.html")


@main.route("/about")
def aboutthis():
    return render_template("about.html")


@main.route("/contact")
def contactthis():
    return render_template("contactus.html")


@main.route("/blog")
def blogthis():
    return render_template("blog.html")


@main.route("/services")
def servicesthis():
    return render_template("services.html")




if __name__ == "__main__":
    main.run(port = 1000, debug = True)