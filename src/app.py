from flask                import Flask
from routes.index_routes  import index_router
from routes.auth_routes   import auth_router
from routes.user_routes   import user_router
from routes.posts_routes  import posts_router 
from flask_sqlalchemy     import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABSE_URI'] = 'mysql://utkakmoxtialdqnv:9uRWwqQKRB6d77iszoqe@b5xhvnlvmlmy7habrfmu-mysql.services.clever-cloud.com:3306/b5xhvnlvmlmy7habrfmu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

@app.context_processor
def render_layout():
  data = {
    "navbar": ["¿Quiénes somos?", "¿Qué ofrecemos?", "Iniciar Sesión", "Registrarme"],
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