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
    try:
      response = {"msg": "Categoria registrada exitosamente", "error": False}
      sql             = text(f"SELECT * FROM categories WHERE name_category = '{category}';")
      category_exists = db.session.execute(sql)
      category_exists = tuple(category_exists)
      if category_exists:
        response["msg"] = "La categoria ya existe"
        response["error"] = True

        return response
    
      new_category = Category_model(
        name=category
      )
      
      db.session.add(new_category)
      db.session.commit()
      
      return response  
    except Exception as error:
      print(error)
      response = {"msg": "ERROR, intentelo mas tarde", "error": True}
      return response

  @classmethod
  def updateCategory(self, db, old_name, new_name):
    try:
      response  = {"msg": "Editado exitosamente", "error": False}
      
      if not new_name:
        response["msg"]   = "No hay campos por modificar"
        response["error"] = True
      
        return response
      
      sql       = f"SELECT name_category FROM categories WHERE name_category = '{old_name}';"
      category  = db.session.execute(text(sql))
      category  = list(category)

      print(category)

      if not category:
        response["msg"]   = "Categoria no encontrada"
        response["error"] = True
        
        return response

      sql = f"UPDATE categories SET name_category = '{new_name}' WHERE name_category = '{category[0][0]}'"

      print(sql)

      db.session.execute(text(sql))
      db.session.commit()

      return response

    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}
    
  @classmethod
  def deleteCategory(self, db, name):
    try:
      response  = {"msg": "Eliminado exitosamente", "error": False}
      sql       = f"DELETE FROM categories WHERE name_category = '{name}';"
      
      db.session.execute(text(sql))
      db.session.commit()

      return response

    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}
    
  @classmethod
  def convertToColumn(self, column):
    column = "name_category" 
    
    return column