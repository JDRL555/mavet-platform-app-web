from sqlalchemy.sql           import text
from src.models.mavet_models  import Specialty_user as Specialty_model

class Specialty_user:
  @classmethod
  def getAll(self, db):
    
    sql = text("SELECT * FROM specialty_users;")
    specialty_users = db.session.execute(sql)
    specialty_users = tuple(specialty_users)
    
    data = []
    
    for row in specialty_users:
      data.append({
        "name": row[0],
        "created_at": row[1]
      })
      
    return data
  
  @classmethod
  def createSpecialty(self, db, name_specialty):
    sql             = text(f"SELECT * FROM specialty_users WHERE name_specialty = '{name_specialty}';")
    specialty_exists = db.session.execute(sql)
    specialty_exists = tuple(specialty_exists)
    if specialty_exists:
      return False
    
    new_specialty = Specialty_model(name_specialty)
    db.session.add(new_specialty)
    db.session.commit()
    return name_specialty
    