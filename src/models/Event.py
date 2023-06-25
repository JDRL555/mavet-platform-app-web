from sqlalchemy.sql           import text
from src.models.mavet_models  import Event as Event_model

class Event:
  @classmethod 
  def createCourse(self, db, event):
    try:
      response = {"msg": "Evento registrado exitosamente", "error": False}
      
      new_course = Event_model(
        name=event["name"],
        description=event["description"],
        startdate=event["startdate"],
        enddate=event["enddate"],
        starttime=event["starttime"],
        endtime=event["endtime"],
        media=event["media"] or None,
        created_at=event["created_at"],
      )
      
      db.session.add(new_course)
      db.session.commit()
      
      return response
      
    except Exception as error:
      response = {"msg": error, "error": True}
      return response
    
  @classmethod
  def getAll(self, db):
    sql         = text("SELECT * FROM events;")
    events      = db.session.execute(sql)
    events      = tuple(events)
    
    data = []
    
    for row in events:
      data.append({
        "name": row[0],
        "description": row[1],
        "startdate": row[2],
        "enddate": row[3],
        "starttime": row[4],
        "endtime": row[5],
        "media": row[6],
        "created_at": row[7]
      })
      
      return data