from flask                import Blueprint, request, redirect, flash
from src.models.Category  import Category
from src.utils.db         import db
import json

category_router = Blueprint("category", __name__)

@category_router.route("/category/new", methods=["POST"])
def category_new():
  try:
    category_info = {
      "Nombre": request.form["Nombre"], 
    } 
    
    print(category_info)
    
    old_columns         = list(category_info.keys())
    new_column          = Category.convertToColumn(old_columns[0])
    new_category_info   = {}
    
    
    for index, value in enumerate(category_info.values()): 
      if not value: 
        flash("Faltan campos por llenar")
        return redirect("/admin")
      new_category_info[new_column] = value
    
    category_info = new_category_info
    
    print(category_info)
    
    category_info = {
      "name": category_info["name_category"],
    }
    
    response = Category.createCategory(db=db, category=category_info["name"])
    
    flash(response["msg"])
    return redirect("/admin")
    
  except Exception as error:
    print("ERROR EN CONTROLADOR")
    print(error)
    return {"msg": "ERROR, intentelo mas tarde", "error": True}

@category_router.route("/category/edit")
def category_edit():
  category_info = request.args.get("info")
  category_info = json.loads(category_info)
  print(category_info)
  
  old_name      = category_info["old_name"]
  new_name      = category_info["new_name"]

  response  = Category.updateCategory(db=db, old_name=old_name, new_name=new_name)
  
  flash(response["msg"])
  return redirect("/admin")

@category_router.route("/category/delete")
def category_delete():
  try:
    name      = request.args.get("id")
    response  = Category.deleteCategory(db=db, name=name)
    
    flash(response["msg"])
    return redirect("/admin")
  except Exception as error:
    print(error)
    flash(response["msg"])
    return redirect("/admin")