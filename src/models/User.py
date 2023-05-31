from bcrypt               import hashpw, checkpw, gensalt
from sqlalchemy.sql       import text
from flask_login          import UserMixin 
from models.mavet_models  import User as User_model

class User(UserMixin):
  def __init__(self, id, username, email):
    self.id       = id
    self.username = username
    self.email    = email
  @classmethod
  def register(self, db, user):
    response = {"msg": "", "error": False}
    
    if user["password"] != user["confirm"]:
      response["msg"]   = "Las contraseñas no coinciden"
      response["error"] = True
      return response
    
    if len(user["phone"]) != 11 or not user["phone"].startswith("04"):
      response["msg"]   = "Ingrese un número de teléfono válido"
      response["error"] = True
      return response
    
    sql = text(f'SELECT username_user FROM users WHERE username_user = "{user["username"]}";')
    username_exists   = db.session.execute(sql)
    username_exists   = tuple(username_exists)
    
    if username_exists:
      response["msg"]   = "El nombre de usuario ya está registrado"
      response["error"] = True
      return response
    
    sql = text(f'SELECT email_user FROM users WHERE email_user = "{user["email"]}";')
    email_exists  = db.session.execute(sql)
    email_exists  = tuple(email_exists)
    
    if email_exists:
      response["msg"]   = "Este correo ya está registrado"
      response["error"] = True
      return response
    
    hashed_password = hashpw(bytes(user["password"], "utf8"), gensalt())
      
    new_user = User_model(
      name=user["name"], 
      last_name=user["lastname"], 
      datebirth=user["datebirth"], 
      username=user["username"], 
      phone=user["phone"], 
      email=user["email"], 
      password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()
  
    return response
  
  @classmethod
  def login(self, db, user):
    response = {"msg": "", "error": False, "user": ""}
     
    sql = text(f'SELECT id, username_user, email_user FROM users WHERE email_user = "{user["email"]}";')
    user_exists  = db.session.execute(sql)
    user_exists  = tuple(user_exists)
    
    if not user_exists:
      response["msg"]   = "El correo es incorrecto o no está registrado"
      response["error"] = True
      return response
    
    sql               = text(f'SELECT password_user FROM users WHERE email_user = "{user["email"]}";')
    password_hashed   = tuple(db.session.execute(sql))[0][0]
    match_password    = checkpw(user["password"].encode("UTF-8"), password_hashed.encode("UTF-8"))
    
    if not match_password:
      response["msg"]   = "Contraseña incorrecta"
      response["error"] = True
      return response
    
    response["user"] = {
      "id": user_exists[0][0],
      "username": user_exists[0][1],
      "email": user_exists[0][2],
    }
    return response
  
  @classmethod
  def getById(self, db, id):
    sql   = text(f'SELECT username_user, email_user, type_id FROM users WHERE id = "{id}";')
    user  = db.session.execute(sql)
    user  = tuple(user)
    user  = {
      "username": user[0][0],
      "email": user[0][1],
      "type": user[0][2],
    }
    return user