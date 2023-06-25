from flask                      import Flask, render_template, redirect
from flask_login                import LoginManager
from cloudinary                 import config
from .models.User                import User
from .routes.index_routes        import index_router
from .routes.auth_routes         import auth_router
from .routes.user_routes         import user_router
from .routes.posts_routes        import posts_router 
from .routes.post_request_routes import post_request_router
from .routes.admin_routes        import admin_router
from .utils.db                   import db
from .utils.data                 import data 
from .utils.var                  import *

def create_app():
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
    return dict(data=data['index'])

  config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY_C,
    api_secret=API_SECRET
  )

  app.register_blueprint(index_router)
  app.register_blueprint(auth_router)
  app.register_blueprint(user_router)
  app.register_blueprint(posts_router)
  app.register_blueprint(post_request_router)
  app.register_blueprint(admin_router)

  return app