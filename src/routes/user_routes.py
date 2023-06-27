from flask                import Blueprint, render_template, redirect, flash, request, get_template_attribute, Response
from flask_login          import current_user
from datetime             import datetime
from src.models.Category  import Category
from src.models.Works_art import Works_art
from src.models.User      import User
from src.utils.db         import db
from src.utils.data       import data
import json
import re

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

@user_router.route("/users/filter", methods=["POST"])
def users_filter():
  filter_data  = request.get_json()
  
  if filter_data["filter_selected"] == "ID": 
    filter_data["filter_selected"] = "id"
    
    user = User.getById(db=db, id=filter_data["filter_value"]) 
    modal_content = get_template_attribute("macros/modal.html", "modal_content")
    
      
    columns_users   = data["modal"]["Usuarios"]["Listar"]["filters"]
    registers_users = [dict(register = list(user["user"].values()))]
    
    users_data = {
      "cols": columns_users,
      "rows": registers_users
    }

    modal_content = modal_content(users_data)
  else:  
    filter_data["filter_selected"] = User.convertToColumn(column=filter_data["filter_selected"])
    
    users = User.getByFilter(db=db, filter_data=filter_data)
    modal_content = get_template_attribute("macros/modal.html", "modal_content")
      
    columns_users   = data["modal"]["Usuarios"]["Listar"]["filters"]
    registers_users = [dict(register = list(register.values())) for register in users["users"]]
    
    users_data = {
      "cols": columns_users,
      "rows": registers_users
    }

    modal_content = modal_content(users_data)
  
  response = Response(modal_content, headers={'Access-Control-Allow-Origin': "*"})
  return response

@user_router.route("/user/edit")
def user_edit():
  user_info = request.args.get("user_info")
  user_info = json.loads(user_info) 
  id        = user_info["id"]
  user_info.pop("id") 
  columns   = User.convertToColumns(columns=list(user_info.keys()))
  values    = list(user_info.values())
  response  = User.editUser(db=db, id=id, columns=columns, values=values)
  
  flash(response["msg"])
  return redirect("/admin")

@user_router.route("/user/delete")
def user_delete():
  id = request.args.get("id")
  id = int(id)
  response = User.deleteUser(db=db, id=id)
  
  flash(response["msg"])
  return redirect("/admin")