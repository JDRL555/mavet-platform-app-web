from flask                import Flask, render_template, redirect, request
from flask_login          import LoginManager, current_user
from models.User          import User
from routes.index_routes  import index_router
from routes.auth_routes   import auth_router
from routes.user_routes   import user_router
from routes.posts_routes  import posts_router 
from utils.db             import db

app = Flask(__name__)

def notFound(error):
  return render_template("404.html")

def notAuthorized(error):
  return redirect("/signin")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://utkakmoxtialdqnv:9uRWwqQKRB6d77iszoqe@b5xhvnlvmlmy7habrfmu-mysql.services.clever-cloud.com:3306/b5xhvnlvmlmy7habrfmu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 's3cr3tk3y'

app.register_error_handler(401, notAuthorized)
app.register_error_handler(404, notFound)

db.init_app(app=app)

login_manager = LoginManager(app=app)
login_manager.init_app(app=app)

with app.app_context():
  db.create_all()
  
@login_manager.user_loader
def load_user(id):
  return User.getById(db, id)

@login_manager.unauthorized_handler
def handle_unauthorized():
  if current_user.is_authenticated:
    return redirect("/posts")
  else:
    return redirect("/signin")

@app.context_processor
def render_layout():
  data = {
    "navbar": [
      {"element": "¿Quiénes somos?", "link": "/"},
      {"element": "¿Qué ofrecemos?", "link": "/"},
      {"element": "Iniciar Sesión", "link": "/signin"},
      {"element": "Registrarme", "link": "/signup"},
    ],
    "contents": [
      {
        "title": "¿Quiénes somos?",
        "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Facilis officia ea explicabo maiores dolorem provident, aut, sequi ad, vero velit cupiditate repellendus iusto repellat numquam dolores voluptates tempora voluptate! Ab incidunt cum aspernatur dignissimos dolorum ipsam ducimus repellendus eum. Veniam ullam eum ut debitis in distinctio nihil minus repellat accusamus commodi exercitationem ipsam tempora harum, laboriosam facere repellendus explicabo impedit itaque laborum temporibus quasi nam. Maxime nisi ullam tempora, magnam sed veritatis optio laborum inventore. Eaque, architecto obcaecati? Sed totam ipsam omnis laudantium laborum perspiciatis, error earum rerum optio! Quisquam similique, nisi maiores asperiores amet rerum eveniet ducimus vitae sed?"
      },
      {
        "title": "¿Qué ofrecemos?",
        "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Facilis officia ea explicabo maiores dolorem provident, aut, sequi ad, vero velit cupiditate repellendus iusto repellat numquam dolores voluptates tempora voluptate! Ab incidunt cum aspernatur dignissimos dolorum ipsam ducimus repellendus eum. Veniam ullam eum ut debitis in distinctio nihil minus repellat accusamus commodi exercitationem ipsam tempora harum, laboriosam facere repellendus explicabo impedit itaque laborum temporibus quasi nam. Maxime nisi ullam tempora, magnam sed veritatis optio laborum inventore. Eaque, architecto obcaecati? Sed totam ipsam omnis laudantium laborum perspiciatis, error earum rerum optio! Quisquam similique, nisi maiores asperiores amet rerum eveniet ducimus vitae sed?"
      }
    ]
  }
    
  return dict(data=data)

app.register_blueprint(index_router)
app.register_blueprint(auth_router)
app.register_blueprint(user_router)
app.register_blueprint(posts_router)