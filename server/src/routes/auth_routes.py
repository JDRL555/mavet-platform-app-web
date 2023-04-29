from flask import Blueprint

auth_router = Blueprint("auth", __name__)

@auth_router.route("/signup")
def signup():
  return "Registrando un nuevo usuario"

@auth_router.route("/signin")
def signin():
  return "Iniciando sesion"

@auth_router.route("/signout")
def signout():
  return "Cerrando sesion"