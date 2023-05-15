import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if not name or not month or not day:
            flash("You must provide all the information.")
            return redirect("/")
        else:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        return redirect("/")

    else:

        birthday_list = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthday_list)

@app.route("/remove_birthday", methods=["POST"])
def remove_birthday():
    name = request.form.get("name")
    db.execute("DELETE FROM birthdays WHERE name == ?", name)
    return redirect("/")


