from flask                import Blueprint, request, redirect, flash
from src.models.Category  import Category
from src.utils.db         import db
import json

category_router = Blueprint("category", __name__)

@category_router.route("/category/new")
def category_new():
  try:
    category_info = request.args.get("info")
    category_info = json.loads(category_info)
    
    old_columns   = list(category_info.keys())
    new_columns   = Category.convertToColumns(old_columns)
    new_category_info = {}
    
    for index, value in enumerate(category_info.values()): 
      if not value: 
        flash("Faltan campos por llenar")
        print(request.path)
        return redirect("/admin")
      new_category_info[new_columns[index]] = value
    
    category_info = new_category_info
    
    print(category_info)
    
    category_info = {
      "name": category_info["name_category"]
    }
    
    response = Category.createCategory(db=db, category=category_info)
    
    flash(response["msg"])
    return redirect("/admin")
    
  except Exception as error:
    print("ERROR EN CONTROLADOR")
    print(error)
    return {"msg": error, "error": True}

@category_router.route("/category/edit")
def category_edit():
  category_info = request.args.get("info")
  category_info = json.loads(category_info) 
  id        = category_info["id"]
  category_info.pop("id") 
  columns   = Category.convertToColumns(columns=list(category_info.keys()))
  values    = list(category_info.values())
  response  = Category.editCategory(db=db, id=id, columns=columns, values=values)
  
  flash(response["msg"])
  return redirect("/admin")

@category_router.route("/category/delete")
def category_delete():
  id = request.args.get("id")
  id = int(id)
  response = Category.deleteCategory(db=db, id=id)
  
  flash(response["msg"])
  return redirect("/admin")