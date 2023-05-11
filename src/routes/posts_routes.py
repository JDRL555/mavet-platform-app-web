from flask import Blueprint, render_template

posts_router = Blueprint("posts", __name__)

@posts_router.route("/posts")
def renderPosts():
  data = {
    "img": "https://i.ibb.co/bL41z0k/Perfil.jpg",
    "titulo": "Nube Roja",
    "usuario": "JDRL",
    "tipo": "Fotografia",
    "descripcion": "Fotografia de nubes a pleno atarceder",
    "recent_user": "Carlos07",
    "recent_img": "https://i.ibb.co/FzFcMT1/carlos.png"
  }
  return render_template("posts.html", data=data)