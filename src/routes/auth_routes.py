from flask                import Blueprint, render_template, request, redirect
from flask_login          import login_user, logout_user, current_user
from utils.db             import db
from models.User          import User

auth_router = Blueprint("auth", __name__)

@auth_router.route("/signup", methods=["GET", "POST"])
def signup():
  if current_user.is_authenticated:
    return redirect("/posts")
  data = { 
    "msg": "",
    "inputs": [
      {"name": "name", "type": "text", "placeholder": "Nombres"},
      {"name": "lastname", "type": "text", "placeholder": "Apellidos"},
      {"name": "datebirth", "type": "text", "placeholder": "Fecha de nacimiento"},
      {"name": "username", "type": "text", "placeholder": "Nombre de usuario"},
      {"name": "phone", "type": "number", "placeholder": "Número de teléfono"},
      {"name": "email", "type": "email", "placeholder": "Correo electrónico"},
      {"name": "password", "type": "password", "placeholder": "Contraseña"},
      {"name": "confirm", "type": "password", "placeholder": "Confirmar contraseña"},
    ]
  }
  if request.method == "GET":
    return render_template("register.html", data=data)
  
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
    data["msg"] = response["msg"]
    return render_template("register.html", data=data)
  
  return redirect("/signin")

@auth_router.route("/signin", methods=["GET", "POST"])
def signin():
  if current_user.is_authenticated:
    return redirect("/posts")
  data = { 
    "msg": "",
    "inputs": [
      {"name": "email", "type": "email", "placeholder": "Correo electrónico"},
      {"name": "password", "type": "password", "placeholder": "Contraseña"}
    ]
  }
  if request.method == "GET":
    return render_template("login.html", data=data)

  user_info = {
    "email": request.form["email"],
    "password": request.form["password"]
  }
  response = User.login(db=db, user=user_info)
  
  if response["error"]:
    data["msg"] = response["msg"]
    return render_template("register.html", data=data)
  
  user = response["user"]
  user = User(user["id"], user["username"], user["email"])
  
  login_user(user)
  
  return redirect("/posts")

@auth_router.route("/signout")
def signout():
  logout_user()
  return redirect("/")