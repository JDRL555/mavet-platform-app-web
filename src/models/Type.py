from sqlalchemy.sql           import text
from src.models.mavet_models  import Type_user as Type_model

class Type_user:
  @classmethod
  def getAll(self, db):
    
    sql = text("SELECT * FROM type_users;")
    type_users = db.session.execute(sql)
    type_users = tuple(type_users)
    
    data = []
    
    for row in type_users:
      data.append({
        "name": row[0],
        "created_at": row[1]
      })
      
    return data
  
  @classmethod
  def createType(self, db, name_type):
    sql             = text(f"SELECT * FROM type_users WHERE name_type = '{name_type}';")
    type_exists = db.session.execute(sql)
    type_exists = tuple(type_exists)
    if type_exists:
      return False
    
    new_type = Type_model(name_type)
    db.session.add(new_type)
    db.session.commit()
    return name_type
    