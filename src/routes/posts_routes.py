from flask               import Blueprint, render_template, redirect, request
from flask_login         import current_user
from models.Category     import Category
from models.mavet_models import Works_art
from utils.db            import db

posts_router = Blueprint("posts", __name__)

@posts_router.route("/posts")
def renderPosts():  
  try:
    if not current_user["username"]:
      return redirect("/signin")
    result = Category.getAll(db=db)
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
          "options": result, 
          "label": "Categoría de la obra"
        },{
          "name": "img", 
          "type": "file", 
          "label": "Adjunta la imagen de la obra"
        },
      ],
      "posts": [
        {
          "username": "JDRL",
          "title": "Nube Roja",
          "img_user": "https://i.ibb.co/bL41z0k/Perfil.jpg",
          "img_post": "https://i.ibb.co/DL4wsSt/cielito.jpg",
          "type": "Fotografia",
          "description": "Fotografia de nubes a pleno atarceder",   
        }
      ],
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
    result = Category.getAll(db=db)
    data = {
      "inputs": [
        {"name": "title", "type": "text", "label": "Titulo de la obra"},
        {"name": "description", "type": "text", "label": "Descripción de la obra"},
        {"name": "category", "options": result, "label": "Categoría de la obra"},
        {"name": "img", "type": "file", "label": "Adjunta la imagen de la obra"},
      ]
    }

    post_info = {
      "title": request.form['title'],
      "description": request.form['description'],
      "category": request.form['category'],
      "img": request.form['img']
    }

    new_post = Works_art(post_info['title'], post_info['description'], post_info['category'], post_info['img'])

    db.session.add(new_post)
    db.session.commit()

    return redirect("/posts")

  except TypeError:
    return redirect("/signin")