from sqlalchemy.sql           import text
from src.models.mavet_models  import Event as Event_model
import cloudinary.uploader

class Event:
  @classmethod 
  def createEvent(self, db, event):
    try:
      response = {"msg": "Evento registrado exitosamente", "error": False}
      
      file = event["media"]
        
      image = cloudinary.uploader.upload(file=file, quality=50) 
      
      new_course = Event_model(
        name=event["name"],
        description=event["description"],
        startdate=event["startdate"],
        enddate=event["enddate"],
        starttime=event["starttime"],
        endtime=event["endtime"],
        media=image["url"],
      )
      
      db.session.add(new_course)
      db.session.commit()
      
      return response
      
    except Exception as error:
      print("ERROR EN EL MODELO")
      print(error)
      response = {"msg": error, "error": True}
      return response
    
  @classmethod
  def getAll(self, db):
    sql         = text("SELECT * FROM events;")
    events      = db.session.execute(sql)
    events      = tuple(events)
    
    print(events)
    
    data = []
    
    for row in events:
      data.append({
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "startdate": row[3],
        "enddate": row[4],
        "starttime": row[5],
        "endtime": row[6],
        "created_at": row[8],
        "media": row[7],
      })
      
    return data
  
  @classmethod
  def convertToColumns(self, columns):
    try:
      if columns[0] == "Nombre":                  columns[0] = "name_event" 
      if columns[1] == "Descripcion":             columns[1] = "description_event" 
      if columns[2] == "Fecha de inicio":         columns[2] = "startdate_event" 
      if columns[3] == "Fecha de finalizacion":   columns[3] = "enddate_event" 
      if columns[4] == "Hora de inicio":          columns[4] = "starttime_event" 
      if columns[5] == "Hora de finalizacion":    columns[5] = "endtime_event" 
      if columns[6] == "Multimedia":              columns[6] = "media_event" 
    
      return columns
    except Exception as error:
      print("ERROR EN EL MODELO")
      print(error)