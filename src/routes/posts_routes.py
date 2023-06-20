from flask                import Blueprint, render_template, redirect, request, flash, get_template_attribute, Response
from flask_login          import current_user
from models.Category      import Category
from models.Works_art     import Works_art
from utils.db             import db
import json

posts_router = Blueprint("posts", __name__)

@posts_router.route("/posts")
def renderPosts():  
  try:
    if not current_user["username"]:
      return redirect("/signin")
    categories  = Category.getAll(db=db)
    works_art   = Works_art.getPaginated(db=db)
    data = {
      "inputs": [
        {
          "name": "title", 
          "type": "text", 
          "label": "Titulo de la obra"
        },{
          "name": "description", 
          "type": "text", 
          "label": "Descripción de la obra"
        },{
          "name": "category", 
          "options": categories, 
          "label": "Categoría de la obra"
        },{
          "name": "img", 
          "type": "file", 
          "label": "Adjunta la imagen de la obra"
        },
      ],
      "posts": works_art,
      "new": {
        "recent_artists": [
          {
            "username": "Carlos07",
            "img_user": "https://i.ibb.co/FzFcMT1/carlos.png"
          }
        ]
      }
    }
    return render_template("posts.html", data=data)
  except TypeError:
    return redirect("/signin")

@posts_router.route("/new/post", methods=['POST'])
def createPost():
  try:
    post_info = {
      "title": request.form['title'],
      "description": request.form['description'],
      "category": request.form['category'],
      "img": request.files["img"],
      "author": current_user["id"]
    }
    
    response = Works_art.createPost(db=db, post_info=post_info)
    
    if response["error"]:
      flash("Error al subir tu publicación, Intenta nuevamente...")
      return redirect("/posts")

    return redirect("/posts")
  except TypeError:
    return redirect("/signin")

@posts_router.route("/post", methods=["POST"])
def post():
  page          = request.get_json()
  all_works_art = Works_art.getAll(db=db)

  if len(all_works_art) > page:
    post      = get_template_attribute("macros/post.html", "post")
    works_art = Works_art.getPaginated(db=db, page=page)
    res       = post(works_art, current_user)
    response  = Response(res, headers={'Access-Control-Allow-Origin': "*"})
    return response
  else:
    return []
    