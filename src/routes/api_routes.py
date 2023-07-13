from flask          import Blueprint
from src.utils.data import data

api_router = Blueprint("api", __name__)

@api_router.route("/data")
def get_data():
  return data