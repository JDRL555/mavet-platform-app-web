from flask              import Blueprint, request, redirect, flash
from src.models.Course  import Course
from src.utils.db       import db
import json

course_router = Blueprint("course", __name__)

@course_router.route("/course/new")
def course_new():
  try:
    course_info = request.args.get("info")
    course_info = json.loads(course_info)
    
    old_columns   = list(course_info.keys())
    new_columns   = Course.convertToColumns(old_columns)
    new_course_info = {}
    
    for index, value in enumerate(course_info.values()): 
      if not value: 
        flash("Faltan campos por llenar")
        print(request.path)
        return redirect("/admin")
      new_course_info[new_columns[index]] = value
    
    course_info = new_course_info
    
    print(course_info)
    
    course_info = {
      "name": course_info["name_course"],
      "description": course_info["description_course"],
      "teacher": course_info["teacher_course"],
      "startdate": course_info["startdate_course"],
      "enddate": course_info["enddate_course"],
      "starttime": course_info["starttime_course"],
      "endtime": course_info["endtime_course"],
      "price": course_info["price_course"],
      "media": course_info["media_course"],
    }
    
    response = Course.createCourse(db=db, course=course_info)
    
    flash(response["msg"])
    return redirect("/admin")
    
  except Exception as error:
    print("ERROR EN CONTROLADOR")
    print(error)
    return {"msg": error, "error": True}

@course_router.route("/course/edit")
def course_edit():
  course_info = request.args.get("info")
  course_info = json.loads(course_info) 
  id        = course_info["id"]
  course_info.pop("id") 
  columns   = Course.convertToColumns(columns=list(course_info.keys()))
  values    = list(course_info.values())
  response  = Course.editCourse(db=db, id=id, columns=columns, values=values)
  
  flash(response["msg"])
  return redirect("/admin")

@course_router.route("/course/delete")
def course_delete():
  id = request.args.get("id")
  id = int(id)
  response = Course.deleteCourse(db=db, id=id)
  
  flash(response["msg"])
  return redirect("/admin")