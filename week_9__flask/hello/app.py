from flask import Flask, render_template, request # Flask is a function, render_template is a function, request is a variable

app = Flask(__name__) # assign the return value of the Flask() function to the variable app

@app.route('/') # decorator, which is a function that takes another function as an argument. The decorator is the @app route.

def index():
    # if "name" in request.args: #check if there's a key called name in the dictionary request.args
    #     name = request.args["name"]
    # else:
    #     name = "world"

    name = request.args.get("name", "world") # same as above, but shorter. World is the default value if there's no name in the dictionary request.args.

    return render_template("index.html", placeholder=name)