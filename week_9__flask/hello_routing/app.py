from flask import Flask, render_template, request # Flask is a function, render_template is a function, request is a variable

app = Flask(__name__) # assign the return value of the Flask() function to the variable app

@app.route('/', methods=["GET", "POST"]) 

def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", placeholder=request.form.get("name"))
    else:
        return "No route here."