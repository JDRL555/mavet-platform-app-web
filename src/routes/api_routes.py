from flask                        import Blueprint

from src.utils.data               import data
from src.utils.db                 import db
from src.models.Works_art         import Works_art
from src.models.User              import User
from src.models.Category          import Category
from src.models.Course            import Course
from src.models.Event             import Event
from src.models.Specialty         import Specialty_user
from src.models.Type              import Type_user
from src.models.Preview_works_art import Preview_works_art

api_router = Blueprint("api", __name__)

@api_router.route("/api/data")
def get_data():
  return data

@api_router.route("/api/works_art")
def get_works_art():
  works_art = Works_art.getAll(db)
  return works_art

@api_router.route("/api/users")
def get_users():
  users = User.getAll(db)
  return users

@api_router.route("/api/categories")
def get_categories():
  categories = Category.getAll(db)
  return categories

@api_router.route("/api/courses")
def get_courses():
  courses = Course.getAll(db)
  return courses

@api_router.route("/api/events")
def get_events():
  events = Event.getAll(db)
  return events

@api_router.route("/api/specialties")
def get_specialties():
  specialties = Specialty_user.getAll(db)
  return specialties

@api_router.route("/api/types")
def get_types():
  types = Type_user.getAll(db)
  return types

@api_router.route("/api/previews")
def get_previews():
  previews = Preview_works_art.getAll(db)
  return previews

