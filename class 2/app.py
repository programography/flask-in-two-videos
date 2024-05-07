
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request

main = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myflaskweb.db"

db = SQLAlchemy(main)


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String)
    Message = db.Column(db.Text)
    Added_time = db.Column(db.DateTime, server_default=db.func.now())


with main.app_context():
    db.create_all()


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
    all_data = ContactUs.query.all()

    # print(all_data)
    return render_template("services.html", mydata = all_data)

@main.route("/savethisdata", methods = ["POST"])
def saveinfo():
    if request.method == "POST":
        fu_name = request.form.get("fname")
        email = request.form.get("email")
        phne_num = request.form.get("pnumber")
        msg = request.form.get("msg")

        data = ContactUs(fullname = fu_name, email = email, phone_number = phne_num, Message = msg)

        db.session.add(data)
        db.session.commit()

        return redirect("/services")

    return "data saved"


@main.route("/deletethisdata/<int:xyz>")
def deletethis(xyz):
    data = ContactUs.query.get(xyz)
    # print(data, "xxxxxxxxxx")
    db.session.delete(data)
    db.session.commit()

    return redirect("/services")



@main.route("/updatedata/<int:abc>")
def updatedata(abc):
    data = ContactUs.query.get(abc)
    return render_template("contactusupdate.html", mydata = data)



@main.route("/savethisdatanow/<int:a>", methods = ["POST"])
def sabethisdata(a):
    data = ContactUs.query.get(a)
    if request.method == "POST":
        fu_name = request.form.get("fname")
        email = request.form.get("email")
        phne_num = request.form.get("pnumber")
        msg = request.form.get("msg")

        data.fullname = fu_name
        data.email = email
        data.phone_number = phne_num
        data.Message = msg
        db.session.commit()

        return redirect("/services")



if __name__ == "__main__":
    main.run(port = 1000, debug = True)