"""Basic flask app"""
from flask import Flask

"""The module imported handles all the framework's operations, from routing to connecting temps."""

app = Flask(__name__)

"""Routing"""


@app.route("/", strict_slashes=False)
def index():
    """
    This is the default route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This is the /hbnb route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    This is the /c route
    """
    text_spaces = text.replace("_", " ")
    return f"C {text_spaces}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """
    This is the /python route
    """
    text_spaces = text.replace("_", " ")
    return f"Python {text_spaces}"


@app.route("/number", strict_slashes=False)
@app.route("/number/<int:n>", strict_slashes=False)
def n_int(n=0):
    """
    This is the /number route
    """
    return f"{n} is an number"
    # try:
    #     n = int(n)
    #     return f"{n} is an number"
    # except ValueError:
    #     return f"{n} is not a valid number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
