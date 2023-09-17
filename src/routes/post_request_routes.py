from flask                        import Blueprint, render_template, request, redirect, flash
from flask_login                  import current_user
from src.models.Preview_works_art import Preview_works_art
from src.models.Works_art         import Works_art 
from src.utils.db                 import db

post_request_router = Blueprint("post_request", __name__)

@post_request_router.route("/post/request")
def post_request():
  posts_request = Preview_works_art.getPaginated(db=db, page=0)
  return render_template("posts_request.html", posts_request=posts_request, admin=True)

@post_request_router.route("/new/post/request", methods=["POST"])
def new_post_request():
    post_info = {
      "title": request.form['title'],
      "description": request.form['description'],
      "category": request.form['category'],
      "img": request.files["img"],
      "author": current_user["id"]
    }
    
    response = Preview_works_art.createRequest(db=db, post_info=post_info)
    
    if response["error"]:
      flash(response["msg"])
      return redirect("/posts")
    
    flash(response["msg"])
    return redirect("/posts")

@post_request_router.route("/post/response")
def post_response():
  id              = request.args.get("id")
  admin_res       = request.args.get("res")
  post_response   = Preview_works_art.getById(db=db, id=id)

  if post_response["error"]:
    flash(post_response["msg"])
    return redirect("/post/request")
  
  if admin_res == "accept":    
    post                = post_response["post"]
    works_art_response  = Works_art.createPost(db=db, post_info=post)
    
    if works_art_response["error"]:
      flash(works_art_response["msg"])
      return redirect("/post/request")
    
    flash("La publicacion fue aceptada exitosamente!")
  else: flash("La publicacion fue denegada exitosamente!")
  
  deleted_request_response = Preview_works_art.deleteRequest(db=db, id=id)
  
  if deleted_request_response["error"]:
    flash(deleted_request_response["msg"])
    return redirect("/post/request")
    
  return redirect("/post/request")