from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}
SPORTS = [ "Soccer", "Basketball", "Hockey", "Volleyball", "Tennis"]

@app.route('/')
def index():
  return render_template("index.html", sports=SPORTS)

@app.route('/register', methods=["POST"])
def register():
  name = request.form.get("name")
  sport = request.form.get("sports")
  if not name or sport not in SPORTS:
    return render_template("failure.html")
  REGISTRANTS[name] = sport
  # return render_template("success.html")
  return redirect("/registrants")

@app.route('/registrants')
def registrants():
  return render_template("registrants.html", registrants=REGISTRANTS)