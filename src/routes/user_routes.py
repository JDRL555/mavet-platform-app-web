from flask            import Blueprint, render_template, redirect, flash
from flask_login      import current_user
from datetime         import datetime
from models.Category  import Category
from models.Works_art import Works_art
from models.User      import User
from utils.db         import db
from utils.data       import data

user_router = Blueprint("user", __name__)

@user_router.route("/users")
def loadUsers():
  return "Loading users..."

@user_router.route("/user/<id>")
def loadUser(id):
  if not current_user["username"]:
    return redirect("/signin")
  user = [current_user]
  if id != current_user["id"]:
    response = User.getById(db=db, id=id)
    if response["error"]:
      flash(response["msg"])
      return redirect("/posts")
    user.clear()
    user.append(response["user"])
  user        = user[0]
  
  datebirth   = user["datebirth"]
  today       = datetime.today().date()
  age_user    = today.year - datebirth.year - ((today.month, today.day) < (datebirth.month, datebirth.day))
  user["age_user"] = age_user
  
  categories  = Category.getAll(db=db)
  works_art   = Works_art.getRelatedWith(db=db, id=id)
  
  data["posts"]["inputs"][2]["options"] = categories
  data["posts"]["works_art"]            = works_art
  data["user"]                          = user
  
  return render_template("user.html", data=data)