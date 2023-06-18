from flask            import Blueprint, render_template, redirect, request
from flask_login      import current_user
from datetime         import datetime
from models.Category  import Category
from models.Works_art import Works_art
from utils.db         import db

user_router = Blueprint("user", __name__)

@user_router.route("/users")
def loadUsers():
  return "Loading users..."

@user_router.route("/user/<id>")
def loadUser(id):
  # try:
  if not current_user["username"]:
    return redirect("/signin")
  datebirth   = current_user["datebirth"]
  today       = datetime.today().date()
  age_user    = today.year - datebirth.year - ((today.month, today.day) < (datebirth.month, datebirth.day))
  categories  = Category.getAll(db=db)
  works_art   = Works_art.getRelatedWith(db=db, id=id)
  data = {
    "works_art": works_art,
    "age_user": age_user,
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
  }
  return render_template("user.html", data=data)
  # except TypeError:
  #   return redirect("/signin")