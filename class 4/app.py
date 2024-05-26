#pip install flask

from flask import Flask, render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trytosaveimage.db"

db = SQLAlchemy(app)

class Userinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Full_Name = db.Column(db.String)
    Phone_Number = db.Column(db.String)
    Image_path = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route("/")
def myform():
    return render_template("form.html")


@app.route("/show")
def showdata():
    all_data = Userinfo.query.all()

    return render_template("show.html", data = all_data)

@app.route("/savedata", methods = ["POST"])
def savinginfo():
    if request.method == "POST":
        full_name = request.form.get("fname")
        phone_number = request.form.get("pnumber")
        img = request.files.get("img")

        if img:
            img.save(os.path.join("static/userimages", img.filename))
            path = os.path.join("static/userimages", img.filename)
        
        data = Userinfo(Full_Name = full_name, Phone_Number = phone_number, Image_path = path)

        db.session.add(data)
        db.session.commit()

        return redirect("/show")


    return "data saved"



if __name__ == "__main__":
    app.run(debug = True)