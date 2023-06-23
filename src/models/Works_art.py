from models.mavet_models  import Works_art as Works_art_model
from sqlalchemy.sql       import text
from utils.var            import *


class Works_art:
  @classmethod
  def createPost(self, db, post_info):
    response = {"msg": "", "error": False, "data": {}} 
    
    new_post = Works_art_model(
      title=post_info["title"], 
      description=post_info["description"], 
      img=post_info["img"], 
      category=post_info["category"],
      author_id=post_info["author"]
    )

    db.session.add(new_post)
    db.session.commit()
    
    return response
  
  @classmethod
  def getAll(self, db):
    sql = text(f'''
        SELECT users.username_user, works_art.title_work, works_art.description_work, works_art.category, works_art.img_work, users.avatar_user 
        FROM works_art 
        INNER JOIN users 
        ON works_art.author_id = users.id ORDER BY users.created_at;
    ''')
    
    works_art_data = db.session.execute(sql)
    works_art_data = list(works_art_data)
    
    data = []
    
    for row in works_art_data:
      data.append({
        "username": row[0],
        "title": row[1],
        "description": row[2],
        "category": row[3],
        "img_work": row[4],
        "img_user": row[5]
      })
    
    return data
  
  @classmethod
  def getPaginated(self, db, id = None, page = 0):
    if not id:
      sql = text(f'''
          SELECT users.username_user, works_art.title_work, works_art.description_work, works_art.category, works_art.img_work, users.avatar_user 
          FROM works_art 
          INNER JOIN users 
          ON works_art.author_id = users.id ORDER BY works_art.id DESC LIMIT {page}, 5;
      ''')
    else:
      sql = text(f'''
          SELECT users.username_user, works_art.title_work, works_art.description_work, works_art.category, works_art.img_work, users.avatar_user 
          FROM works_art 
          INNER JOIN users 
          ON works_art.author_id = users.id 
          WHERE works_art.author_id = {id}
          ORDER BY works_art.id DESC 
          LIMIT {page}, 5;
      ''')
    
    works_art_data = db.session.execute(sql)
    works_art_data = list(works_art_data)
    
    data = []
    
    for row in works_art_data:
      data.append({
        "username": row[0],
        "title": row[1],
        "description": row[2],
        "category": row[3],
        "img_work": row[4],
        "img_user": row[5]
      })
    
    return data
  
  @classmethod
  def getRelatedWith(self, db, id):
    sql = text(f'''
        SELECT users.username_user, works_art.title_work, works_art.description_work, works_art.category, works_art.img_work, users.avatar_user 
        FROM works_art 
        INNER JOIN users 
        ON works_art.author_id = users.id 
        WHERE works_art.author_id = {id}
        ORDER BY users.created_at;
    ''')
    
    works_art_data = db.session.execute(sql)
    works_art_data = list(works_art_data)
    data           = []
    
    for row in works_art_data:
      data.append({
        "username": row[0],
        "title": row[1],
        "description": row[2],
        "category": row[3],
        "img_work": row[4],
        "img_user": row[5]
      })
    return data
    