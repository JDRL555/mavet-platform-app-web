from sqlalchemy.sql import text
from models.mavet_models import Preview_works_art as Preview_model
import cloudinary.uploader

class Preview_works_art:
  @classmethod
  def createRequest(self, db, post_info):
    try:
      response = {"msg": "", "error": False}
      
      file  = post_info["img"]
      image = cloudinary.uploader.upload(file=file, quality=50) 
      
      new_post = Preview_model(
        title=post_info["title"], 
        description=post_info["description"], 
        img=image["url"], 
        category=post_info["category"],
        author_id=post_info["author"]
      )

      db.session.add(new_post)
      db.session.commit()
      
      response["msg"] = "Tu publicacion fue enviada al administrador. Si es aceptada, la podras visualizar!"
      
      return response  
    except Exception as error:
      return {"msg": error, "error": True}
    
  @classmethod
  def getPaginated(self, db, page = 0):
    try:
      sql = text(f'''
        SELECT previews.id, users.username_user, previews.title_work, previews.description_work, previews.category, previews.img_work, users.avatar_user 
        FROM previews 
        INNER JOIN users 
        ON previews.author_id = users.id ORDER BY previews.id DESC LIMIT {page}, 5;
      ''')
      
      works_art_data = db.session.execute(sql)
      works_art_data = list(works_art_data)
      
      data  = []
    
      for row in works_art_data:
        data.append({
          "id": row[0],
          "username": row[1],
          "title": row[2],
          "description": row[3],
          "category": row[4],
          "img_work": row[5],
          "img_user": row[6]
        })
    
      return data
    except Exception as error:
      return {"msg": error, "error": True}

  @classmethod
  def getById(self, db, id):
    try:
      response = {"msg": "Here's the post!", "error": False, "post": []}
      
      sql = text(f"SELECT * FROM previews WHERE id = {id};")
      post = db.session.execute(sql)
      post = list(post)
      
      if not post:
        response["msg"] = "La publicacion no fue encontrada, ingrese un id valido"
        response["error"] = True
        return response
      
      data = {}
      
      for row in post:
        data = {
          "title": row[1],
          "description": row[2],
          "img": row[3],
          "category": row[4],
          "author": row[5]
        }
      
      response["post"] = data
      
      return response
    except Exception as error:
      return {"msg": error, "error": True}
    
  @classmethod
  def deleteRequest(self, db, id):
    try:
      response = {"msg": "Eliminado exitosamente", "error": False}
      
      sql = text(f"DELETE FROM previews WHERE id = {id};")
      
      db.session.execute(sql)
      db.session.commit()
      
      
      return response
    except Exception as error:
      return {"msg": error, "error": True}
    
    
    
    