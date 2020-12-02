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

# Rendering home page


@app.route("/")
@app.route("/home_page")
def home_page():
    """
    Renders home page
    """
    return render_template("information_pages/home.html")


@app.route("/search_interventions", methods=["GET", "POST"])
def search_interventions():
    """
    Allows user to search within interventions
    Users search within name and area fields
    """
    interventions = list(mongo.db.interventions.find())
    query = request.form.get("query")
    interventions = list(mongo.db.interventions.find({"$text":
                                                     {"$search": str(query)}}))
    return render_template("intervention_pages/interventions.html",
                           interventions=interventions)


@app.route("/show_training")
def show_training():
    """
    Renders training pages
    """
    training = list(mongo.db.training.find())
    return render_template("training_pages/training.html", training=training)


@app.route("/show_interventions")
def show_interventions():
    """
    Retrieves MongoDb intervention collection to display on intervention page
    """
    interventions = list(mongo.db.interventions.find())
    return render_template("intervention_pages/interventions.html",
                           interventions=interventions)


@app.route("/about_page")
def about_page():
    """
    Renders About page for users
    """
    return render_template("information_pages/about.html")


@app.route("/help_page")
def help_page():
    """
    Renders help page for users
    """
    return render_template("information_pages/help.html")


@app.route("/success_intervention")
def success_intervention():
    """
    Renders page indicating successful intervention added
    """
    return render_template("intervention_pages/success_intervention.html")


@app.route("/success_training")
def success_training():
    """
    Renders page indicating successful training added
    """
    return render_template("training_pages/success_training.html")


@app.route("/add_training", methods=["GET", "POST"])
def add_training():
    """
    if statement allows user to add user Training data to page and MongoDB
    else statement returns back to add training page
    """
    if request.method == "POST":
        training = {
            "training_name": request.form.get("training_name"),
            "training_type": request.form.get("training_type"),
            "delivery_method": request.form.get("training_delivery"),
            "start_date": request.form.get("start_date"),
            "training_duration": request.form.get("training_duration"),
            "training_area": request.form.get("training_area"),
            "qualification": request.form.get("qualification"),
            "training_cost": request.form.get("training_cost"),
            "training_provider": request.form.get("training_provider")
        }
        mongo.db.training.insert_one(training)
        flash("Training succesfully added!")
        return redirect(url_for("success_training"))
    else:
        return render_template("training_pages/add_training.html")


@app.route("/edit_training/<training_id>", methods=["GET", "POST"])
def edit_training(training_id):
    """
    if statement allows user to edit user Training data to page and MongoDB
    """
    if request.method == "POST":
        update = {
            "training_name": request.form.get("training_name"),
            "training_type": request.form.get("training_type"),
            "delivery_method": request.form.get("delivery_method"),
            "start_date": request.form.get("start_date"),
            "training_duration": request.form.get("training_duration"),
            "training_area": request.form.get("training_area"),
            "qualification": request.form.get("qualification"),
            "training_cost": request.form.get("training_cost"),
            "training_provider": request.form.get("training_provider")
        }
        mongo.db.training.update({"_id": ObjectId(training_id)}, update)
        flash("Training Successfully Updated")
        return redirect(url_for("success_training"))
    training = mongo.db.training.find_one({"_id": ObjectId(training_id)})
    return render_template("training_pages/edit_training.html",
                           training=training)


@app.route("/delete_training/<training_id>")
def delete_training(training_id):
    """
    Renders page indicating delete function successful
    """
    mongo.db.training.remove({"_id": ObjectId(training_id)})
    flash("training successfully deleted")
    return render_template("training_pages/delete_training.html")


@app.route("/add_interventions", methods=["GET", "POST"])
def add_interventions():
    """
    if statement allows user to add user Intervention data to page and MongoDB
    else statement returns back to add training page
    """
    if request.method == "POST":
        interventions = {
            "intervention_name": request.form.get("intervention_name"),
            "intervention_area": request.form.get("intervention_area"),
            "intervention_website": request.form.get("intervention_website"),
            "intervention_rating": request.form.get("intervention_rating"),
            "intervention_duration": request.form.get("intervention_duration"),
            "intervention_resources": request.form.get
            ("intervention_resources"),
            "intervention_cost": request.form.get("intervention_cost")
        }
        mongo.db.interventions.insert_one(interventions)
        flash("Task Successfully Added")
        return redirect(url_for("success_intervention"))
    else:
        return render_template("intervention_pages/add_interventions.html")

    interventions = mongo.db.interventions.find().sort("name", 1)
    return render_template("intervention_pages/add_interventions",
                           interventions=interventions)


@app.route("/edit_interventions/<interventions_id>", methods=["GET", "POST"])
def edit_interventions(interventions_id):
    """
    if statement allows user to edit user Intervention data to page and MongoDB
    """
    if request.method == "POST":
        update = {
            "intervention_name": request.form.get("intervention_name"),
            "intervention_area": request.form.get("intervention_area"),
            "intervention_website": request.form.get("intervention_website"),
            "intervention_rating": request.form.get("intervention_rating"),
            "intervention_duration": request.form.get("intervention_duration"),
            "intervention_resources": request.form.get(
                "intervention_resources"),
            "intervention_cost": request.form.get("intervention_cost")
        }
        mongo.db.interventions.update({"_id": ObjectId
                                      (interventions_id)}, update)
        flash("Task Successfully Updated")
        return redirect(url_for("show_interventions"))
    interventions = mongo.db.interventions.find_one({"_id": ObjectId
                                                     (interventions_id)})
    return render_template("intervention_pages/edit_interventions.html",
                           interventions=interventions)


@app.route("/delete_interventions/<interventions_id>")
def delete_interventions(interventions_id):
    """
    function allows user to delete interventions
    """
    mongo.db.interventions.remove({"_id": ObjectId(interventions_id)})
    flash("Intervention successfully deleted")
    return render_template("intervention_pages/delete_interventions.html")


@app.errorhandler(404)
def page_not_found(error):
    """
    Function to render 404 error page
    """
    return render_template("error_pages/404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Function to render 404 error page
    """
    return render_template("error_pages/500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")),
            debug=True)
