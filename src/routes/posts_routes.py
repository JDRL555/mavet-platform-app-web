from flask                import Blueprint, render_template, redirect, request, flash, get_template_attribute, Response
from flask_login          import current_user
from models.Category      import Category
from models.Works_art     import Works_art
from models.User          import User
from utils.db             import db
from utils.data           import data

posts_router = Blueprint("posts", __name__)

@posts_router.route("/posts")
def renderPosts():  
  try:
    if not current_user["username"]:
      return redirect("/signin")
    categories      = Category.getAll(db=db)
    works_art       = Works_art.getPaginated(db=db)
    recent_artists  = User.getRecent(db=db)
    
    data["posts"]["inputs"][2]["options"]   = categories
    data["posts"]["works_art"]              = works_art
    data["posts"]["new"]["recent_artists"]  = recent_artists["users"]
    
    return render_template("posts.html", data=data["posts"])
  except TypeError:
    return redirect("/signin")

@posts_router.route("/new/post", methods=['POST'])
def createPost():
  try:
    post_info = {
      "title": request.form['title'],
      "description": request.form['description'],
      "category": request.form['category'],
      "img": request.files["img"],
      "author": current_user["id"]
    }
    
    response = Works_art.createPost(db=db, post_info=post_info)
    
    if response["error"]:
      flash("Error al subir tu publicación, Intenta nuevamente...")
      return redirect("/posts")

    return redirect("/posts")
  except TypeError:
    return redirect("/signin")

@posts_router.route("/post", methods=["POST"])
def post():
  page          = request.get_json()
  all_works_art = Works_art.getAll(db=db)

  if len(all_works_art) > page:
    post      = get_template_attribute("macros/post.html", "post")
    works_art = Works_art.getPaginated(db=db, page=page)
    res       = post(works_art, current_user)
    response  = Response(res, headers={'Access-Control-Allow-Origin': "*"})
    return response
  else:
    return []
    