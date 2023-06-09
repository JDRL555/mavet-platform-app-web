from models.mavet_models  import Works_art as Works_art_model
from sqlalchemy.sql       import text
from flask_login          import current_user
from requests             import post 
from base64               import b64encode
from utils.var            import *
from json                 import loads
from PIL                  import Image
from io                   import BytesIO


class Works_art:
  @classmethod
  def createPost(self, db, post_info):
    response = {"msg": "", "error": False, "data": {}}
    
    file      = post_info["img"]
    
    #resize the image
    image     = Image.open(file)
    image     = image.resize((image.width // 2, image.height // 2))
    
    buffer = BytesIO()
    image.save(buffer, "jpeg")
    
    buffer.seek(0)
    
    resized_image = buffer.read()
    
    #saving the image to imgbb with the imgbb API
    img       = b64encode(resized_image)
    img_name  = post_info["title"]
    
    url = API_URL + API_KEY
    
    data = { "image": img, "name": img_name }
    
    result = post(url=url, data=data)
    
    if result.status_code != 200:
      response["error"] = True
      return response
  
    result_data       = result.content
    result_to_json    = loads(result_data)
    response["data"]  = result_to_json
    
    image_url = response["data"]["data"]["url"]
    
    new_post = Works_art_model(
      post_info["title"], 
      post_info["description"], 
      image_url, 
      post_info["category"],
      post_info["author"]
    )

    db.session.add(new_post)
    db.session.commit()
    
    buffer.close()
    return response
  
  @classmethod
  def getAll(self, db):
    sql = text('''
        SELECT users.username_user, works_art.title_work, works_art.description_work, works_art.category, works_art.img_work, users.avatar_user 
        FROM works_art 
        INNER JOIN users 
        ON works_art.author_id = users.id;
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
    