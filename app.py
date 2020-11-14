import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/sample_page")
def sample_page():
    return render_template("sample.html")


@app.route("/about_page")
def about_page():
    return render_template("about.html")


@app.route("/add_students", methods=["GET", "POST"])
def add_students():
    if request.method == "POST":
        students = {
            "name": request.form.get("name"),
            "class": request.form.get("class"),
            "sen": request.form.get("sen"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "intervention": request.form.get("intervention")
        }
        mongo.db.students.insert_one(students)
        flash("Student succesfully added!")
        return redirect(url_for("add_students"))
    else:
        return render_template("add_students.html")
        
    students = mongo.db.students.find().sort("name", 1)
    return render_template("add_students", students=students)


@app.route("/edit_students/<students_id>", methods=["GET", "POST"])
def edit_students(students_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "class": request.form.get("class"),
            "rsen": request.form.get("sen"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "intervention": request.form.get("intervention")
        }
        mongo.db.students.update({"_id": ObjectId(students_id)}, submit)
        flash("Students Successfully Updated")
    students = mongo.db.students.find_one({"_id": ObjectId(students_id)})
    return render_template("edit_students.html", students=students)


@app.route("/delete_students/<students_id>")
def delete_students(students_id):
    mongo.db.students.remove({"_id": ObjectId(students_id)})
    flash("student successfully deleted")
    return render_template("delete_students.html")


@app.route("/add_interventions", methods=["GET", "POST"])
def add_interventions():
    if request.method == "POST":
        interventions = {
            "name": request.form.get("name"),
            "sen": request.form.get("sen"),
            "rating": request.form.get("rating"),
            "duration": request.form.get("duration"),
            "resources": request.form.get("resources"),
            "cost": request.form.get("cost")
        }
        mongo.db.interventions.insert_one(interventions)
        flash("Task Successfully Added")
        return redirect(url_for("add_interventions"))
    else:
        return render_template("add_interventions.html")

    interventions = mongo.db.interventions.find().sort("name", 1)
    return render_template("add_interventions", interventions=interventions)


@app.route("/edit_interventions/<interventions_id>", methods=["GET", "POST"])
def edit_interventions(interventions_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "sen": request.form.get("sen"),
            "rating": request.form.get("rating"),
            "duration": request.form.get("duration"),
            "resources": request.form.get("resources"),
            "cost": request.form.get("cost")
        }
        mongo.db.interventions.update({"_id": ObjectId(interventions_id)}, submit)
        flash("Task Successfully Updated")
    interventions = mongo.db.interventions.find_one({"_id": ObjectId(interventions_id)})
    return render_template("edit_interventions.html", interventions=interventions)


@app.route("/delete_interventions/<interventions_id>")
def delete_interventions(interventions_id):
    mongo.db.interventions.remove({"_id": ObjectId(interventions_id)})
    flash("Intervention successfully deleted")
    return render_template("delete_interventions.html")

if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port=int(os.environ.get("PORT")),
            debug=True)
