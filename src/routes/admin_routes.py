from flask            import Blueprint, render_template, get_template_attribute, request, Response
from src.models.User      import User
from src.models.Event     import Event
from src.models.Course    import Course
from src.models.Category  import Category
from src.utils.db         import db
from src.utils.data       import data

admin_router = Blueprint("admin", __name__)

@admin_router.route("/admin")
def admin():
  return render_template("admin.html", data=data["admin"])

@admin_router.route("/modal", methods=["POST"])
def modal():
  req_from  = request.get_json()
  modal     = get_template_attribute("macros/modal.html", "modal")
  
  if req_from == "Usuarios":
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
    
  if req_from == "Eventos":
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
      
  if req_from == "Cursos":
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
    
  if req_from == "Categorias":
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
    
  response = Response(modal, headers={'Access-Control-Allow-Origin': "*"})
  return response