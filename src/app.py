from flask                import Flask, render_template, redirect
from flask_login          import LoginManager
from models.User          import User
from routes.index_routes  import index_router
from routes.auth_routes   import auth_router
from routes.user_routes   import user_router
from routes.posts_routes  import posts_router 
from utils.db             import db
from utils.var            import *

app = Flask(__name__)

def notFound(error):
  return render_template("404.html")

def notAuthorized(error):
  return redirect("/signin")

app.secret_key                                = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']         = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

app.register_error_handler(401, notAuthorized)
app.register_error_handler(404, notFound)

db.init_app(app=app)

login_manager = LoginManager(app=app)
login_manager.init_app(app=app)

with app.app_context():
  db.create_all()
  
@login_manager.user_loader
def load_user(id):
  response = User.getById(db, id)
  return response["user"]

@login_manager.unauthorized_handler
def handle_unauthorized():
  return redirect("/signin")

@app.context_processor
def render_layout():
  data = {
    "navbar": [
      {"element": "Iniciar Sesión", "link": "/signin"},
      {"element": "Registrarme", "link": "/signup"},
    ],
    "contents": [
      {
        "title": "¿Quiénes somos?",
        "description": "Somos el MAVET, quien mas capo"
      },
      {
        "title": "¿Qué ofrecemos?",
        "description": "Cursos, eventos, lo que tu quieras papi uwu"
      },
      {
        "title": "Historia del MAVET",
        "description": "El MAVET es un museo XD"
      }
    ]
  }
    
  return dict(data=data)

app.register_blueprint(index_router)
app.register_blueprint(auth_router)
app.register_blueprint(user_router)
app.register_blueprint(posts_router)