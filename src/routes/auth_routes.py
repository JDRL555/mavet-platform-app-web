from flask                import Blueprint, render_template, request, redirect, flash
from flask_login          import login_user, logout_user, login_required, current_user
from models.User          import User
from utils.db             import db
from utils.data           import data 

auth_router = Blueprint("auth", __name__)

@auth_router.route("/signup", methods=["GET", "POST"])
def signup():
  try:
    if current_user.is_authenticated:
      return redirect("/posts")
    if request.method == "GET":
      return render_template("register.html", data=data['register'])
    
    user_info = {
      "name": request.form["name"],
      "lastname": request.form["lastname"],
      "datebirth": request.form["datebirth"],
      "username": request.form["username"],
      "phone": request.form["phone"],
      "email": request.form["email"],
      "password": request.form["password"],
      "confirm": request.form["confirm"],
    }
    
    response = User.register(db=db, user=user_info)
    
    if response["error"]:
      flash(response["msg"])
      return redirect("/signup")
    
    return redirect("/signin")
  except AttributeError:
    return redirect("/posts")

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