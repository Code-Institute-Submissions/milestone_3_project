import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/show_students")
def show_students():
    students = list(mongo.db.students.find())
    return render_template("students.html", students=students)


@app.route("/")
@app.route("/show_interventions")
def show_interventions():
    interventions = list(mongo.db.interventions.find())
    return render_template("interventions.html", interventions=interventions)


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("home.html")


@app.route("/")
@app.route("/sample_page")
def sample_page():
    return render_template("sample.html")


@app.route("/")
@app.route("/about_page")
def about_page():
    return render_template("about.html")


@app.route("/")
@app.route("/add_students")
def add_students():
    students = list(mongo.db.students.find())
    return render_template("add.html", students=students)


@app.route("/")
@app.route("/add_interventions")
def add_interventions():
    interventions = list(mongo.db.interventions.find())
    return render_template("add_interventions.html", interventions=interventions)


if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port=int(os.environ.get("PORT")),
            debug=True)
