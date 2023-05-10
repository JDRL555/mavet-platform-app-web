from flask                import Flask
from routes.index_routes  import index_router
from routes.auth_routes   import auth_router
from routes.user_routes   import user_router

app = Flask(__name__)

app.register_blueprint(index_router)
app.register_blueprint(auth_router)
app.register_blueprint(user_router)