from bcrypt                   import hashpw, checkpw, gensalt
from sqlalchemy.sql           import text
from flask_login              import UserMixin 
from src.models.mavet_models  import User as User_model

class User(UserMixin):
  def __init__(self, id, username, email):
    self.id       = id
    self.username = username
    self.email    = email
  @classmethod
  def register(self, db, user):
    print(user)
    response = {"msg": "Registrado exitosamente", "error": False}
    try:
      if not user['confirm']: user['confirm'] = user['password']
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
      print("ERROR EN MODELO")
      print(error)
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
      SELECT id, name_user, last_name_user, datebirth, email_user, username_user, phone_user, specialty_id, type_id, created_at FROM users;
    ''')
    
    users = db.session.execute(sql)
    users = list(users)
    
    data = []
    
    for row in users:
      data.append({
        "id": row[0],
        "name": row[1],
        "last_name": row[2],
        "datebirth": row[3],
        "email": row[4],
        "username": row[5],
        "phone": row[6],
        "specialty": row[7],
        "type": row[8],
        "created_at": row[9]
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
    
  @classmethod
  def getByFilter(self, db, filter_data):
    try:
      response = {"msg": "", "error": False, "users": []}
      sql = text(f'''
        SELECT id, name_user, last_name_user, datebirth, email_user, username_user, phone_user, specialty_id, type_id, created_at 
        FROM users
        WHERE {filter_data["filter_selected"]} 
        LIKE '%{filter_data["filter_value"]}%'
        ;
      ''')
      users = db.session.execute(sql)
      users = list(users)
      
      data = []
      
      for row in users:
        data.append({
          "id": row[0],
          "name": row[1],
          "last_name": row[2],
          "datebirth": row[3],
          "email": row[4],
          "username": row[5],
          "phone": row[6],
          "specialty": row[7],
          "type": row[8],
          "created_at": row[9]
        })
      
      response["users"] = data
      
      return response
      
    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}
  
  @classmethod
  def editUser(self, db, id, columns, values):
    response = {"msg": "Editado exitosamente", "error": False}
    user_sql  = text(f"SELECT name_user, last_name_user, datebirth, email_user, username_user, phone_user, specialty_id, type_id, created_at FROM users WHERE id = {id};")
    user      = db.session.execute(user_sql)
    user      = list(user)
    
    if not user:
      response = {"msg": "Usuario no encontrado", "error": True}
      return response
    
    user        = list(user[0])
    new_columns = []  
    new_values  = []  
    
    for index, value in enumerate(values):

      if type(user[index]) != str:
        user[index] = str(user[index])
      
      if user[index] != value:
        new_columns.append(columns[index])
        new_values.append(value)
        
    if not new_values:
      response = {"msg": "No hay valores nuevos", "error": True}
      return response
    
    sql = f"UPDATE users SET "
    for index, column in enumerate(new_columns):
      sql += f"{column} = '{new_values[index]}'"
      if index < len(new_columns) - 1: sql += ", "
    
    sql += f" WHERE id = {id};"
    
    db.session.execute(text(sql))
    db.session.commit()
    
    return response

  @classmethod
  def deleteUser(self, db, id):
    try:  
      response = {"msg": "Eliminado exitosamente", "error": False}
      
      sql = f"DELETE FROM users WHERE id = {id}"
      
      db.session.execute(text(sql))
      db.session.commit()
      
      return response
      
    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}
    
  @classmethod
  def convertToColumns(self, columns):
    for index, _ in enumerate(columns):
      if columns[index] == "Nombres":                   columns[index] = "name_user" 
      if columns[index] == "Apellidos":                 columns[index] = "last_name_user" 
      if columns[index] == "Fecha de Nacimiento":       columns[index] = "datebirth" 
      if columns[index] == "Correo":                    columns[index] = "email_user" 
      if columns[index] == "Nombre de usuario":         columns[index] = "username_user" 
      if columns[index] == "Telefono":                  columns[index] = "phone_user" 
      if columns[index] == "Especialidad del usuario":  columns[index] = "specialty_id" 
      if columns[index] == "Tipo de usuario":           columns[index] = "type_id" 
      if columns[index] == "Fecha de creacion":         columns[index] = "created_at" 
      if columns[index] == "Clave":                     columns[index] = "password_user" 
    
    return columns
  
  @classmethod
  def convertToColumn(self, column):
    
    if column == "Nombres":                   column = "name_user" 
    if column == "Apellidos":                 column = "last_name_user" 
    if column == "Fecha de Nacimiento":       column = "datebirth" 
    if column == "Correo":                    column = "email_user" 
    if column == "Nombre de usuario":         column = "username_user" 
    if column == "Telefono":                  column = "phone_user" 
    if column == "Tipo de Usuario":           column = "type_id" 
    if column == "Especialidad del usuario":  column = "specialty_id" 
    if column == "Fecha de creacion":         column = "created_at" 
    
    return column