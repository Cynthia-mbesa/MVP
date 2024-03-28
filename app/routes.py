from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user
from .models import User

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/login")
def login():
    # Implement Google Sign-In logic here
    # After successful login, retrieve user information from Google
    # For simplicity, we'll use a mock user for now
    user = User(id=1, username="example_user", role="student", age=12)
    login_user(user)
    return redirect(url_for("main.index"))

@main.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Extract user information from the signup form
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")  # "student", "teacher", or "parent"
        age = int(request.form.get("age"))

        # Validate and store the user information (database integration will be added later)
        user = User(id=1, username=username, role=role, age=age)
        login_user(user)
        return redirect(url_for("main.index"))

    return render_template("signup.html")
