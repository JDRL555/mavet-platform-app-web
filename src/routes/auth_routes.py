from flask import Blueprint, render_template

auth_router = Blueprint("auth", __name__)

@auth_router.route("/signup")
def signup():
  data = {
    "msg": ""
  }
  return render_template("register.html", data=data)

@auth_router.route("/signin")
def signin():
  data = {
    "msg": ""
  }
  return render_template("login.html", data=data)

@auth_router.route("/signout")
def signout():
  return "Cerrando sesion"