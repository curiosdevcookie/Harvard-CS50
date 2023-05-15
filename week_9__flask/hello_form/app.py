from flask import Flask, render_template, request # Flask is a function, render_template is a function, request is a variable

app = Flask(__name__) # assign the return value of the Flask() function to the variable app

@app.route('/') # decorator, which is a function that takes another function as an argument. The decorator is the @app route.

def index():
    return render_template("index.html")

@app.route('/greet', methods=["POST"])

def greet():
    return render_template("greet.html", placeholder=request.args.get("name", "world"))