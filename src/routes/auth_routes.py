from flask        import Blueprint, render_template, request, redirect
from models.Mavet import User
from utils.db     import db
from bcrypt       import hashpw, checkpw, gensalt

auth_router = Blueprint("auth", __name__)

@auth_router.route("/signup", methods=["GET", "POST"])
def signup():
  
  if request.method == "GET":
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
    return render_template("register.html", data=data)
  
  name      = request.form["name"]
  lastname  = request.form["lastname"]
  datebirth = request.form["datebirth"]
  username  = request.form["username"]
  phone     = request.form["phone"]
  email     = request.form["email"]
  password  = request.form["password"]
  confirm   = request.form["confirm"]
  
  if password != confirm:
    data = { 
      "msg": "las contraseñas no coinciden",
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
    return render_template("register.html", data=data)
  
  if len(phone) < 11 or not phone.startswith("04"):
    data = { 
      "msg": "Ingrese un número de teléfono válido",
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
    return render_template("register.html", data=data)
  
  hashed_password = hashpw(bytes(password), gensalt())
    
  new_user  = User(name=name, last_name=lastname, datebirth=datebirth, username=username, phone=phone, email=email, password=hashed_password)
  print(new_user)
  db.session.add(new_user)
  db.session.commit()
  
  return redirect("/signin")

@auth_router.route("/signin", methods=["GET", "POST"])
def signin():
  if request.method == "GET":
    data = { 
      "msg": "",
      "inputs": [
        {"name": "email", "type": "email", "placeholder": "Correo electrónico"},
        {"name": "name", "type": "password", "placeholder": "Contraseña"}
      ]
    }
    return render_template("login.html", data=data)
  return "Iniciando sesion..."

@auth_router.route("/signout")
def signout():
  return "Cerrando sesion"