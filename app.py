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
@app.route("/home_page")
def home_page():
    return render_template("information_pages/home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    interventions = list(mongo.db.interventions.find({"$text": {"$search": query}}))
    return render_template("intervention_pages/interventions.html", interventions=interventions)


@app.route("/")
@app.route("/show_training")
def show_training():
    training = list(mongo.db.training.find())
    return render_template("training_pages/training.html", training=training)


@app.route("/")
@app.route("/show_interventions")
def show_interventions():
    interventions = list(mongo.db.interventions.find())
    return render_template("intervention_pages/interventions.html", interventions=interventions)


@app.route("/about_page")
def about_page():
    return render_template("information_pages/about.html")


@app.route("/help_page")
def help_page():
    return render_template("information_pages/help.html")


@app.route("/success_intervention")
def success_intervention():
    return render_template("intervention_pages/success_intervention.html")


@app.route("/success_training")
def success_training():
    return render_template("training_pages/success_training.html")


@app.route("/add_training", methods=["GET", "POST"])
def add_training():
    if request.method == "POST":
        training = {
            "name": request.form.get("name"),
            "type": request.form.get("type"),
            "delivery": request.form.get("delivery"),
            "start_date": request.form.get("start_date"),
            "duration": request.form.get("duration"),
            "area": request.form.get("area"),
            "qualification": request.form.get("qualification"),
            "cost": request.form.get("cost"),
            "provider": request.form.get("provider")
        }
        mongo.db.training.insert_one(training)
        flash("Training succesfully added!")
        return redirect(url_for("success_training"))
    else:
        return render_template("training_pages/add_training.html")


@app.route("/edit_training/<training_id>", methods=["GET", "POST"])
def edit_training(training_id):
    if request.method == "POST":
        update = {
            "name": request.form.get("name"),
            "type": request.form.get("type"),
            "delivery": request.form.get("delivery"),
            "start_date": request.form.get("start_date"),
            "duration": request.form.get("duration"),
            "area": request.form.get("area"),
            "qualification": request.form.get("qualification"),
            "cost": request.form.get("cost"),
            "provider": request.form.get("provider")
        }
        mongo.db.training.update({"_id": ObjectId(training_id)}, update)
        flash("Training Successfully Updated")
        return redirect(url_for("success_training"))
    training = mongo.db.training.find_one({"_id": ObjectId(training_id)})
    return render_template("training_pages/edit_training.html", training=training)


@app.route("/delete_training/<training_id>")
def delete_training(training_id):
    mongo.db.training.remove({"_id": ObjectId(training_id)})
    flash("training successfully deleted")
    return render_template("training_pages/delete_training.html")


@app.route("/add_interventions", methods=["GET", "POST"])
def add_interventions():
    if request.method == "POST":
        interventions = {
            "name": request.form.get("name"),
            "website": request.form.get("website"),
            "rating": request.form.get("rating"),
            "duration": request.form.get("duration"),
            "resources": request.form.get("resources"),
            "cost": request.form.get("cost")
        }
        mongo.db.interventions.insert_one(interventions)
        flash("Task Successfully Added")
        return redirect(url_for("success_intervention"))
    else:
        return render_template("intervention_pages/add_interventions.html")

    interventions = mongo.db.interventions.find().sort("name", 1)
    return render_template("intervention_pages/add_interventions", interventions=interventions)


@app.route("/edit_interventions/<interventions_id>", methods=["GET", "POST"])
def edit_interventions(interventions_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "website": request.form.get("website"),
            "rating": request.form.get("rating"),
            "duration": request.form.get("duration"),
            "resources": request.form.get("resources"),
            "cost": request.form.get("cost")
        }
        mongo.db.interventions.update({"_id": ObjectId(interventions_id)}, submit)
        flash("Task Successfully Updated")
        return redirect(url_for("show_interventions"))
    interventions = mongo.db.interventions.find_one({"_id": ObjectId(interventions_id)})
    return render_template("intervention_pages/edit_interventions.html", interventions=interventions)


@app.route("/delete_interventions/<interventions_id>")
def delete_interventions(interventions_id):
    mongo.db.interventions.remove({"_id": ObjectId(interventions_id)})
    flash("Intervention successfully deleted")
    return render_template("intervention_pages/delete_interventions.html")


@app.errorhandler(404)
def page_not_found(error):
    # note that we set the 404 status explicitly
    return render_template("error_pages/404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    # note that we set the 404 status explicitly
    return render_template("error_pages/500.html"), 500


if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port=int(os.environ.get("PORT")),
            debug=True)
