import sqlite3
from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/home.html")
def home1():
    return render_template ("home.html")

@app.route("/html/AboutUS.html")
def AboutUs():
    return render_template ("AboutUS.html")

@app.route("/html/FindYourAdventure.html")
def FindYourAdventure():
    return render_template ("FindYourAdventure.html")

@app.route("/html/GoldenGate.html")
def GoldenGate():
    return render_template ("GoldenGate.html")

@app.route("/html/Login.html")
def Login():
    return render_template ("Login.html")

@app.route("/html/NiagraFalls.html")
def NiagraFalls():
    return render_template ("NiagraFalls.html")

@app.route("/html/PaymentMethod.html")
def PaymentMethod():
    return render_template ("PaymentMethod.html")

@app.route("/html/Signup.html")
def Signup():
    return render_template ("Signup.html")

@app.route("/html/StatueOfLiberty.html")
def StatueOfLiberty():
    return render_template ("StatueOfLiberty.html")


@app.route("/db")
def testg_db():
    conn = sqlite3.connect("database.db")
    print("Opened database successfully", flush=True)

    conn.execute("DROP TABLE IF EXISTS newuser")
    conn.commit()
    conn.execute("create table newuser(fullname TEXT, email TEXT, password TEXT)")
    print("Tables created successfully", flush=True)
    conn.close()
    return "Tables Created Successfully"


@app.route("/addrec", methods=["POST", "GET"])
def addrec():
    if request.method == "POST":
        try:
            fullname = request.form["name"]
            email = request.form["mail"]
            password = request.form["pass"]

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO newuser(fullname,email,password)VALUES (?,?,?)",
                    (fullname, email, password),
                )
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in database"
        finally:
            con.close()
            return render_template ("login.html")
        
@app.route("/sign", methods=["POST", "GET"])
def sign():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            query = (
                "select email,password from newuser where email = '"
                + email
                + "' and password = '"
                + password
                + "'"
            )
            cur.execute(query)
            row = cur.fetchone()
            if row is not None:
                return render_template("home.html")
            else:
                error = "Invalid email or password"
                return render_template ("login.html")


