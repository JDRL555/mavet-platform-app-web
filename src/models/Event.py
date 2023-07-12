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
      response = {"msg": "ERROR, intentelo mas tarde", "error": True}
      return response
    
  @classmethod
  def getAll(self, db):
    sql         = text("SELECT * FROM events ORDER BY created_at DESC;")
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
  def updateEvent(self, db, id, columns, values):
    try:
      response  = {"msg": "Editado exitosamente", "error": False}
      sql = f'''
        SELECT name_event, description_event, startdate_event, enddate_event, starttime_event, endtime_event 
        FROM events WHERE id = {id};
      '''
      
      event     = db.session.execute(text(sql))
      event     = list(event)

      print(event)

      if not event:
        response["msg"] = "Evento no encontrado"
        response["error"] = True
        
        return response
      
      event       = event[0]
      new_values  = []
      new_columns = []

      for index, row in enumerate(event):
        print(row)
        print(values[index])

        if type(row) != str:
          row = str(row) 

        if row != values[index]:
          new_values.append(values[index])
          new_columns.append(columns[index])

      print(new_values)
      print(new_columns)

      if not len(new_values):
        response["msg"]   = "No hay campos por modificar"
        response["error"] = True
        
        return response

      sql = "UPDATE events SET "

      for index, column in enumerate(new_columns):
        sql += f"{column} = '{new_values[index]}'"

        if index != len(new_values) - 1: sql += ", "

      sql += f" WHERE id = {id}"

      print(sql)

      db.session.execute(text(sql))
      db.session.commit()

      return response

    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}
    
  @classmethod
  def deleteEvent(self, db, id):
    try:
      response  = {"msg": "Eliminado exitosamente", "error": True}
      sql       = f"DELETE FROM events WHERE id = {id};"
      
      db.session.execute(text(sql))
      db.session.commit()

      return response

    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}
  
  @classmethod
  def convertToColumns(self, columns):
    try:
      for index, _ in enumerate(columns):
        if columns[index] == "Nombre":                  columns[index] = "name_event" 
        if columns[index] == "Descripcion":             columns[index] = "description_event" 
        if columns[index] == "Fecha de inicio":         columns[index] = "startdate_event" 
        if columns[index] == "Fecha de finalizacion":   columns[index] = "enddate_event" 
        if columns[index] == "Hora de inicio":          columns[index] = "starttime_event" 
        if columns[index] == "Hora de finalizacion":    columns[index] = "endtime_event" 
        if columns[index] == "Multimedia":              columns[index] = "media_event" 
    
      return columns
    except Exception as error:
      print("ERROR EN EL MODELO")
      print(error)