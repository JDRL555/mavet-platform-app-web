from flask                import Blueprint, render_template, request, redirect, flash
from flask_login          import login_user, logout_user, login_required, current_user
from src.models.User      import User
from src.utils.db         import db
from src.utils.data       import data 
import json

auth_router = Blueprint("auth", __name__)

@auth_router.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("register.html", data=data['register'])
    

@auth_router.route("/signin", methods=["GET", "POST"])
def signin():
  try:
    if current_user.is_authenticated:
      return redirect("/posts")
    if request.method == "GET":
      return render_template("login.html", data=data['login'])

    user_info = {
      "email": request.form["email"],
      "password": request.form["password"]
    }
    response = User.login(db=db, user=user_info)
    
    if response["error"]:
      print("oh no")
      flash(response["msg"])
      return redirect("/signin")
    
    user = response["user"]
    user = User(user["id"], user["username"], user["email"])
    
    login_user(user)
    
    return redirect("/posts")
  except AttributeError:
    return redirect("/posts")

@auth_router.route("/signout")
def signout():
  logout_user()
  return redirect("/")