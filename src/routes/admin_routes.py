from flask            import Blueprint, render_template, get_template_attribute, request, Response
from models.User      import User
from models.Event     import Event
from models.Course    import Course
from models.Category  import Category
from utils.db         import db
from utils.data       import data

admin_router = Blueprint("admin", __name__)

@admin_router.route("/admin")
def admin():
  data = {
    "buttons": ["Usuarios", "Eventos", "Cursos", "Categorias"],
    "options": ["Crear", "Listar", "Actualizar", "Eliminar"],
  }
  return render_template("admin.html", data=data)

@admin_router.route("/modal", methods=["POST"])
def modal():
  req   = request.get_json()
  modal = get_template_attribute("macros/modal.html", "modal")
  match req["from"]:
    case "Usuarios":
      if req["option"] == "Listar":  
        users = User.getAll(db=db)
        if not users: 
          data["modal"]["Usuarios"]["Listar"]["data"] = []
        else:  
          columns_users   = data["modal"]["Usuarios"]["Listar"]["filters"]
          registers_users = [dict(register = list(register.values())) for register in users]
          
          users_data = {
            "cols": columns_users,
            "rows": registers_users
          }
          
          data["modal"]["Usuarios"]["Listar"]["data"] = users_data
  
        modal = modal(data["modal"]["Usuarios"]["Listar"])
      if req["option"] == "Crear":      modal = modal(data["modal"]["Usuarios"]["Crear"])
      if req["option"] == "Actualizar": modal = modal(data["modal"]["Usuarios"]["Actualizar"])
      if req["option"] == "Eliminar":   modal = modal(data["modal"]["Usuarios"]["Eliminar"])
      
    case "Eventos":
      if req["option"] == "Listar":     
        events = Event.getAll(db=db)
        if not events: 
          data["modal"]["Eventos"]["Listar"]["data"] = []
        else:  
          columns_events   = data["modal"]["Eventos"]["Listar"]["filters"]
          registers_events = [dict(register = list(register.values())) for register in events]
          
          events_data = {
            "cols": columns_events,
            "rows": registers_events
          }
          
          data["modal"]["Eventos"]["Listar"]["data"] = events_data
  
        modal = modal(data["modal"]["Eventos"]["Listar"])
      if req["option"] == "Crear":      modal = modal(data["modal"]["Eventos"]["Crear"])
      if req["option"] == "Actualizar": modal = modal(data["modal"]["Eventos"]["Actualizar"])
      if req["option"] == "Eliminar":   modal = modal(data["modal"]["Eventos"]["Eliminar"])
      
    case "Cursos":
      if req["option"] == "Listar":     
        courses = Course.getAll(db=db)
        if not courses: 
          data["modal"]["Cursos"]["Listar"]["data"] = []
        else:
          columns_courses   = data["modal"]["Cursos"]["Listar"]["filters"]
          registers_courses = [dict(register = list(register.values())) for register in courses]
          
          courses_data = {
            "cols": columns_courses,
            "rows": registers_courses
          }
          
          data["modal"]["Cursos"]["Listar"]["data"] = courses_data
  
        modal = modal(data["modal"]["Cursos"]["Listar"])
      if req["option"] == "Crear":      modal = modal(data["modal"]["Cursos"]["Crear"])
      if req["option"] == "Actualizar": modal = modal(data["modal"]["Cursos"]["Actualizar"])
      if req["option"] == "Eliminar":   modal = modal(data["modal"]["Cursos"]["Eliminar"])
      
    case "Categorias":
      if req["option"] == "Listar":  
        categories = Category.getAll(db=db)
        if not categories: 
          data["modal"]["Categorias"]["Listar"]["data"] = []
        else:
          columns_categories   = data["modal"]["Categorias"]["Listar"]["filters"]
          registers_categories = [dict(register = list(register.values())) for register in categories]
          
          categories_data = {
            "cols": columns_categories,
            "rows": registers_categories
          }
          
          data["modal"]["Categorias"]["Listar"]["data"] = categories_data   
  
        modal = modal(data["modal"]["Categorias"]["Listar"])
      if req["option"] == "Crear":      modal = modal(data["modal"]["Categorias"]["Crear"])
      if req["option"] == "Actualizar": modal = modal(data["modal"]["Categorias"]["Actualizar"])
      if req["option"] == "Eliminar":   modal = modal(data["modal"]["Categorias"]["Eliminar"])
      
  response = Response(modal, headers={'Access-Control-Allow-Origin': "*"})
  return response