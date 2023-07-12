from flask            import Blueprint, request, redirect, flash
from src.models.Event import Event
from src.utils.db     import db
import json

event_router = Blueprint("event", __name__)

@event_router.route("/event/new" , methods=["POST"])
def event_new():
  try:
    event_info = {
      "Nombre": request.form["Nombre"], 
      "Descripcion": request.form["Descripcion"], 
      "Fecha de inicio": request.form["Fecha de inicio"], 
      "Fecha de finalizacion": request.form["Fecha de finalizacion"],
      "Hora de inicio": request.form["Hora de inicio"],  
      "Hora de finalizacion": request.form["Hora de finalizacion"],  
      "Multimedia": request.files["Multimedia"],  
    } 
    
    print(event_info)
    
    old_columns     = list(event_info.keys())
    new_columns     = Event.convertToColumns(old_columns)
    new_event_info  = {}
    
    
    for index, value in enumerate(event_info.values()): 
      if not value: 
        flash("Faltan campos por llenar")
        return redirect("/admin")
      new_event_info[new_columns[index]] = value
    
    event_info = new_event_info
    
    print(event_info)
    
    event_info = {
      "name": event_info["name_event"],
      "description": event_info["description_event"],
      "startdate": event_info["startdate_event"],
      "enddate": event_info["enddate_event"],
      "starttime": event_info["starttime_event"],
      "endtime": event_info["endtime_event"],
      "media": event_info["media_event"],
    }
    
    response = Event.createEvent(db=db, event=event_info)
    
    flash(response["msg"])
    return redirect("/admin")
    
  except Exception as error:
    print("ERROR EN CONTROLADOR")
    print(error)
    flash(error)
    return redirect("/admin")

@event_router.route("/event/edit")
def event_edit():
  event_info = request.args.get("info")
  event_info = json.loads(event_info) 
  id        = event_info["id"]
  event_info.pop("id") 
  columns   = Event.convertToColumns(columns=list(event_info.keys()))
  values    = list(event_info.values())
  response  = Event.updateEvent(db=db, id=id, columns=columns, values=values)
  
  flash(response["msg"])
  return redirect("/admin")

@event_router.route("/event/delete")
def event_delete():
  id = request.args.get("id")
  id = int(id)
  response = Event.deleteEvent(db=db, id=id)
  
  flash(response["msg"])
  return redirect("/admin")