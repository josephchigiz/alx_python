from flask import Flask, render_template, request

app = Flask(__name__)

MEMBERS = {}
SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    sport = request.form.get("sport")
    if sport not in SPORTS:
        return render_template("failure.html")
    MEMBERS[name] = sport
    return render_template("register.html", you=request.form.get("name", "Student."))


@app.route("/members")
def members():
    return render_template("members.html", members=MEMBERS)
