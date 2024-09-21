import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
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
    rows = db.execute("SELECT id_users, stock, SUM(shares) as total_shares, history, cash, price FROM data  INNER JOIN users ON data.id_users = users.id WHERE id_users = ? GROUP BY stock ", session["user_id"])
    x = db.execute("SELECT shares, price FROM data WHERE id_users = ?", session["user_id"])
    if rows:
        razem = 0
        for row in x:
            razem = razem + float(row["shares"]) * float(row["price"])
        cash = rows[0]["cash"]
        stock = rows[0]["stock"]
        shares = rows[0]["total_shares"]
        notowania = lookup(stock)
        price = notowania["price"]
        total = int(shares) * int(price)
        new_rows = []
        for row in rows:
            stock = row["stock"]
            shares = row["total_shares"]
            notowania = lookup(stock)
            price = notowania["price"]
            total = int(shares) * float(price)
            row["total"] = float(total)
            new_rows.append(row)
        razem = razem + cash
        return render_template("index.html", rows=new_rows, cash=cash, total=total, razem=razem)
    a = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cash = a[0]["cash"]
    return render_template("log.html", cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stock_info = lookup(request.form.get("symbol"))
        number_of_shares = request.form.get("shares")
        if stock_info is None:
            return apology("invalid symbol", 400)
        try:
            number_of_shares = int(number_of_shares)
        except ValueError:
            return apology("invalid number of shares", 400)

        if stock_info is not None:
            price_per_share = stock_info["price"]
            stock_symbol = stock_info["symbol"]
            num_shares = int(request.form.get("shares"))
            total_cost = price_per_share * num_shares
            current_datetime = datetime.now()
            history = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            x = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            if x[0]['cash'] >= total_cost:
                y = x[0]['cash'] - total_cost
                db.execute("UPDATE users SET cash = ? WHERE id = ?", y, session["user_id"])
                db.execute("INSERT INTO data (id_users, stock, shares, price, history) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock_symbol, num_shares, price_per_share, history)

                rows = db.execute("SELECT id_users, stock, SUM(shares) as total_shares, history, cash, price FROM data INNER JOIN users ON data.id_users = users.id WHERE id_users = ? GROUP BY stock", session["user_id"])
                x = db.execute("SELECT shares, price FROM data WHERE id_users = ?", session["user_id"])
                if rows:
                    razem = 0
                    for row in x:
                        razem = razem + float(row["shares"]) * float(row["price"])
                    cash = rows[0]["cash"]
                    stock = rows[0]["stock"]
                    shares = rows[0]["total_shares"]
                    notowania = lookup(stock)
                    price = notowania["price"]
                    total = int(shares) * float(price)
                    new_rows = []
                    for row in rows:
                        stock = row["stock"]
                        shares = row["total_shares"]
                        notowania = lookup(stock)
                        price = notowania["price"]
                        total = int(shares) * float(price)
                        row["total"] = float(total)
                        new_rows.append(row)
                    razem = razem + cash
                    return render_template("index.html", rows=new_rows, cash=cash, total=total, razem=razem)
                a = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
                cash = a[0]["cash"]
                return render_template("log.html", cash=cash)

                return render_template("index.html", rows=new_rows)
            else:
                return apology("Not enough cash", 400)
    return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    data = db.execute("SELECT stock, shares, price, history FROM data WHERE id_users=?", session["user_id"])
    if data:
        symbol = data[0]["stock"]
        shares = data[0]["shares"]
        price = data[0]["price"]
        transacted = data[0]["history"]
        return render_template("history.html", data=data )
    return render_template("hist.html")


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        print(stock)
        if stock is None:
            return apology("invalid symbol", 400)
        return render_template("quoted.html", price = stock["price"], symbol = stock["symbol"])
    if request.method == "GET":
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method =="POST":
        username = request.form.get("username")
        xhash = request.form.get("password")
        if not username:
            return apology("Please provide Username")
        if not xhash:
            return apology("Please provide Password")
        if not request.form.get("confirmation"):
            return apology("Please provide Password (again)")
        if xhash != request.form.get("confirmation"):
            return apology("Password are diffrents")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 0:
            return apology("That username already exists")
        hash = generate_password_hash(xhash)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":


        symbol = request.form.get("symbol")
        rows = db.execute("SELECT id_users, stock, SUM(shares) as total_shares FROM data WHERE id_users = ? AND stock = ? GROUP BY stock ", session["user_id"], symbol)
        total_shares = 0
        shares = int(request.form.get("shares"))
        stock_info = lookup(request.form.get("symbol"))
        price = stock_info["price"]
        if stock_info is None:
            return apology("invalid symbol", 400)

        for row in rows:
            total_shares = row["total_shares"]

        if shares > int(total_shares):
            return apology("Too less share", 400)
        additiona_cash = float(price) * float(shares)
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        new_cash = additiona_cash + float(cash[0]["cash"])
        db.execute("UPDATE users SET cash = ? WHERE id = ? ", new_cash, session["user_id"])

        current_datetime = datetime.now()
        history = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        akcje = -(shares)
        db.execute("INSERT INTO data (id_users, stock, shares, price, history) VALUES (?, ?, ?, ?, ?)", session["user_id"], symbol, akcje, price, history)

        rows = db.execute("SELECT id_users, stock, SUM(shares) as total_shares, history, cash, price FROM data  INNER JOIN users ON data.id_users = users.id WHERE id_users = ? GROUP BY stock ", session["user_id"])
        x = db.execute("SELECT shares, price FROM data WHERE id_users = ?", session["user_id"])
        razem = 0
        for row in x:
            razem = razem + float(row["shares"]) * float(row["price"])
        cash = rows[0]["cash"]
        stock = rows[0]["stock"]
        shares = rows[0]["total_shares"]
        notowania = lookup(stock)
        price = notowania["price"]
        total = int(shares) * int(price)
        new_rows = []
        for row in rows:
            stock = row["stock"]
            shares = row["total_shares"]
            notowania = lookup(stock)
            price = notowania["price"]
            total = int(shares) * float(price)
            row["total"] = float(total)
            new_rows.append(row)
        razem = razem + cash



        return render_template("index.html", rows=new_rows, cash=cash, total=total, razem=razem)



    if request.method == "GET":
        rows = db.execute("SELECT id_users, stock, SUM(shares) as total_shares, price  FROM data WHERE id_users = ? GROUP BY stock ", session["user_id"] )
        return render_template("sell.html", rows=rows)

@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        add_cash = request.form.get("add_cash")
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = float(cash[0]["cash"])
        new_cash = 0
        new_cash = float(add_cash) + cash
        db.execute("UPDATE users SET cash = ? WHERE id = ? ", new_cash, session["user_id"])


        rows = db.execute("SELECT id_users, stock, SUM(shares) as total_shares, history, cash, price FROM data  INNER JOIN users ON data.id_users = users.id WHERE id_users = ? GROUP BY stock ", session["user_id"])
        x = db.execute("SELECT shares, price FROM data WHERE id_users = ?", session["user_id"])
        if rows:
            razem = 0
            for row in x:
                razem = razem + float(row["shares"]) * float(row["price"])
            cash = rows[0]["cash"]
            stock = rows[0]["stock"]
            shares = rows[0]["total_shares"]
            notowania = lookup(stock)
            price = notowania["price"]
            total = int(shares) * int(price)
            new_rows = []
            for row in rows:
                stock = row["stock"]
                shares = row["total_shares"]
                notowania = lookup(stock)
                price = notowania["price"]
                total = int(shares) * float(price)
                row["total"] = float(total)
                new_rows.append(row)
            razem = razem + cash
            return render_template("index.html", rows=new_rows, cash=cash, total=total, razem=razem)
        a = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        cash = a[0]["cash"]
        return render_template("log.html", cash=cash)


    return render_template("add_cash.html")
