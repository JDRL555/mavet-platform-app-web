from flask import Blueprint, render_template

posts_router = Blueprint("posts", __name__)

@posts_router.route("/posts")
def renderPosts():
  data = {
    "posts": [
      {
        "username": "JDRL",
        "title": "Nube Roja",
        "img_user": "https://i.ibb.co/bL41z0k/Perfil.jpg",
        "img_post": "https://i.ibb.co/DL4wsSt/cielito.jpg",
        "type": "Fotografia",
        "description": "Fotografia de nubes a pleno atarceder",   
      }
    ],
    "new": {
      "recent_artists": [
        {
          "username": "Carlos07",
          "img_user": "https://i.ibb.co/FzFcMT1/carlos.png"
        }
      ]
    }
  }
  return render_template("posts.html", data=data)