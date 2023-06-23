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
    try:
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
      
      if not user["specialty"]: user["specialty"] = "Estudiante"
      if not user["type"]:      user["type"]      = "Estandar"
      
      new_user = User_model(
        name=user["name"], 
        last_name=user["lastname"], 
        datebirth=user["datebirth"], 
        username=user["username"], 
        phone=user["phone"], 
        email=user["email"], 
        password=hashed_password,
        specialty_user=user["specialty"],
        type_user=user["type"]
      )
      
      db.session.add(new_user)
      db.session.commit()
    
      return response
    except Exception as error:
      response["msg"]   = error
      response["error"] = True
      return response
  
  @classmethod
  def login(self, db, user):
    response = {"msg": "", "error": False, "user": ""}
    try:
      sql = text(f'SELECT * FROM users WHERE email_user = "{user["email"]}";')
      user_exists  = db.session.execute(sql)
      user_exists  = tuple(user_exists)
      
      if not user_exists:
        response["msg"]   = "El correo es incorrecto o no está registrado"
        response["error"] = True
        return response
      
      password_hashed   = user_exists[0][8]
      match_password    = checkpw(user["password"].encode("UTF-8"), password_hashed.encode("UTF-8"))
      
      if not match_password:
        response["msg"]   = "Contraseña incorrecta"
        response["error"] = True
        return response
      
      response["user"] = {
        "id": user_exists[0][0],
        "name": user_exists[0][1],
        "last_name": user_exists[0][2],
        "datebirth": user_exists[0][3],
        "email": user_exists[0][4],
        "avatar": user_exists[0][5],
        "username": user_exists[0][6],
        "phone": user_exists[0][7],
        "type": user_exists[0][10],
        "specialty": user_exists[0][11]
      }
      return response
    except Exception as error:
      print(error)
      response["error"] = error
      return response
    
  @classmethod
  def getAll(self, db):
    sql = text('''
      SELECT name_user, last_name_user, datebirth, email_user, username_user, phone_user, specialty_id, type_id, created_at FROM users;
    ''')
    
    works_art_data = db.session.execute(sql)
    works_art_data = list(works_art_data)
    
    data = []
    
    for row in works_art_data:
      data.append({
        "name": row[0],
        "last_name": row[1],
        "datebirth": row[2],
        "email": row[3],
        "username": row[4],
        "phone": row[5],
        "specialty": row[6],
        "type": row[7],
        "created_at": row[8]
      })
    
    return data
  
  @classmethod
  def getById(self, db, id):
    response = {"msg": "Here's the users", "error": "", "user": {}}
    try:  
      sql   = text(f'SELECT * FROM users WHERE id = "{id}";')
      user  = db.session.execute(sql)
      user  = tuple(user)
      
      response["user"]  = {
        "id": user[0][0],
        "name": user[0][1],
        "last_name": user[0][2],
        "datebirth": user[0][3],
        "email": user[0][4],
        "avatar": user[0][5],
        "username": user[0][6],
        "phone": user[0][7],
        "type": user[0][10],
        "specialty": user[0][11]
      }
      return response
    except Exception as error:
      response["error"] = error
      return response
    
  @classmethod
  def getRecent(self, db):
    try:
      response = {"msg": "", "error": False, "users": []}
      sql = text('''
        SELECT * FROM users ORDER BY created_at DESC LIMIT 3;
      ''')
      users  = db.session.execute(sql)
      users  = tuple(users)
      
      data = []
      
      for row in users:
        data.append({
          "id": row[0],
          "name": row[1],
          "last_name": row[2],
          "datebirth": row[3],
          "email": row[4],
          "avatar": row[5],
          "username": row[6],
          "phone": row[7],
          "type": row[10],
          "specialty": row[11]
        })
      
      response["users"] = data
      return response
    except Exception as error:
      response["error"] = error
      return response
    
    
    