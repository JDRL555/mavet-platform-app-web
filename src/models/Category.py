from sqlalchemy.sql           import text
from src.models.mavet_models  import Category as Category_model

class Category:
  @classmethod
  def getAll(self, db):
    
    sql = text("SELECT * FROM categories;")
    categories = db.session.execute(sql)
    categories = tuple(categories)
    
    data = []
    
    for row in categories:
      data.append({
        "name": row[0],
        "created_at": row[1]
      })
      
    return data
  
  @classmethod
  def createCategory(self, db, category):
    response = {"msg": "Categoria registrado exitosamente", "error": False}
    try:
      sql             = text(f"SELECT * FROM categories WHERE name_category = '{category}';")
      category_exists = db.session.execute(sql)
      category_exists = tuple(category_exists)
      if category_exists:
        return {"msg": "La categoria ya existe", "error": True}
    
      
      new_category = Category_model(
        name=category["name"]
      )
      
      db.session.add(new_category)
      db.session.commit()
      
      return response  
    except Exception as error:
      response = {"msg": error, "error": True}
      return response
    
  @classmethod
  def convertToColumns(self, columns):
    columns[0] = "name_category" 
    
    return columns