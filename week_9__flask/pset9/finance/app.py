import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Create additional tables:
# Create the "stocks" table
db.execute("DROP TABLE IF EXISTS stocks;")
db.execute("CREATE TABLE stocks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, symbol TEXT, stock_name TEXT UNIQUE, price NUMERIC);")

# Create the "user_stocks" table
db.execute("DROP TABLE IF EXISTS user_stocks;")
db.execute("CREATE TABLE user_stocks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER UNIQUE, symbol TEXT UNIQUE, shares INTEGER, total_value NUMERIC, FOREIGN KEY(user_id) REFERENCES users(id));")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    symbol = db.execute("SELECT symbol FROM user_stocks WHERE user_id = '1';")
    name = db.execute("SELECT stock_name FROM stocks WHERE id = '1';")
    shares = db.execute("SELECT shares FROM user_stocks WHERE user_id = '1';")
    price = db.execute("SELECT price FROM stocks WHERE id = '1';")
    cash = db.execute("SELECT cash FROM users WHERE id = '1';")

    total_value = db.execute("SELECT total_value FROM user_stocks WHERE user_id = '1';")

    return render_template("index.html", symbol=symbol, name=name, shares=shares, price=price, total_value=total_value, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        user_cash = db.execute("SELECT users.cash FROM users WHERE users.id = '1';")
        current_cash = user_cash[0]["cash"]
      
        if not symbol or not shares:
            return apology("must provide symbol and shares", 400)
        # if shares is not an integer, throw type error:
        try:
            shares = int(shares)
        except ValueError:
            print("Must be numeric.")
            return apology("Must be numeric.")
        
        if shares <= 0:
            print("Must be positive.")
            return apology("Must be positive.")
        
        quote = lookup(symbol)

        if not quote:
            return apology("invalid symbol", 400)
        
        price = float(quote["price"])
        # price = lookup(symbol)["price"]
        stock_name = quote["name"]

        total = float(price*shares)

        db.execute("INSERT OR REPLACE INTO stocks (price, stock_name, symbol) VALUES (?, ?, ?)", 
                   price, stock_name, symbol)
        
        get_cash = db.execute("SELECT cash FROM users WHERE id = '1';")
        cash = get_cash[0]["cash"]

        if cash < total:
            return apology("Too little money, I'm afraid.")
            
        current_id = db.execute("SELECT id FROM users WHERE id = '1';")
        user_id = current_id[0]["id"]
        
        db.execute("INSERT OR REPLACE INTO user_stocks (user_id, symbol, shares, total_value) VALUES (?, ?, ?, ?)", 
                   user_id, symbol, shares, total)
        
        current_cash = cash - shares*price
        # update table users column cash with the value of current_cash:
        db.execute("UPDATE users SET cash = ? WHERE id = 1", current_cash)

        get_former_shares = db.execute("SELECT shares FROM user_stocks WHERE user_id = '1';")
        former_shares = get_former_shares[0]["shares"]

        new_shares = shares + former_shares

        db.execute("UPDATE user_stocks SET shares = ? WHERE user_id = 1", new_shares)
    
        return render_template("index.html", name=quote["name"], price=price, symbol=quote["symbol"], shares=shares, cash=cash, total=price*shares, current_cash=current_cash)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 400)
        else:
            quote = lookup(symbol)
            if not quote:
                return apology("invalid symbol", 400)
            else:
                name = quote["name"]
                price = float(quote["price"])

                return render_template("quoted.html", name=name, price=price)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password:
            return apology("must provide username", 400)
        elif db.execute("SELECT * FROM users WHERE username = ?", username):
            return apology("username already exists", 400)
        elif password != confirmation:
            return apology("passwords do not match", 400)
        else:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        
        return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        get_symbol = db.execute("SELECT symbol FROM user_stocks WHERE user_id = 1")
        symbol = get_symbol[0]["symbol"]
        
        return render_template("sell.html", symbol=symbol)
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        get_shares_user = db.execute("SELECT shares FROM user_stocks WHERE user_id = 1")
        shares_user = get_shares_user[0]["shares"]
        shares = int(request.form.get("shares"))

        if shares > shares_user:
            return apology("You don't have that many shares.")
        if not symbol or not shares:
            return apology("must provide symbol and shares", 400)
        
        if shares <= 0:
            print("Must be positive.")
            return apology("Must be positive.")
        
        price = lookup(symbol)["price"]
        
        get_cash = db.execute("SELECT cash FROM users WHERE id = '1';")
        cash = get_cash[0]["cash"]
        current_cash = cash + shares*price
        # update table users column cash with the value of current_cash:
        db.execute("UPDATE users SET cash = ? WHERE id = 1", current_cash)

        return render_template("index.html", symbol=symbol, shares=shares, price=price, cash=cash, total=price*shares)
