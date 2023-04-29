from flask import Blueprint, render_template

index_router = Blueprint("index", __name__)

@index_router.route("/")
def init():
  return render_template("index.html")