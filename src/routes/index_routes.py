from flask import Blueprint, render_template, redirect
from flask_login import current_user

index_router = Blueprint("index", __name__)

@index_router.route("/")
def init():
  try:
    if current_user.is_authenticated:
      return redirect("/posts")
    return render_template("index.html")
  except AttributeError:
    return redirect("/posts")