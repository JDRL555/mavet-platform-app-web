from sqlalchemy.sql           import text
from src.models.mavet_models  import Course as Course_model

class Course:
  @classmethod 
  def createCourse(self, db, course):
    try:
      response = {"msg": "Curso registrado exitosamente", "error": False}
      
      new_course = Course_model(
        name=course["name"],
        description=course["description"],
        teacher=course["teacher"],
        startdate=course["startdate"],
        enddate=course["enddate"],
        starttime=course["starttime"],
        endtime=course["endtime"],
        price=course["price"],
        created_at=course["created_at"],
      )
      
      db.session.add(new_course)
      db.session.commit()
      
      return response
      
    except Exception as error:
      response = {"msg": error, "error": True}
      return response
    
  
  @classmethod
  def getAll(self, db):
    sql         = text("SELECT * FROM courses;")
    courses     = db.session.execute(sql)
    courses     = tuple(courses)
    
    data = []
    
    for row in courses:
      data.append({
        "name": row[0],
        "description": row[1],
        "teacher": row[2],
        "startdate": row[3],
        "enddate": row[4],
        "starttime": row[5],
        "endtime": row[6],
        "price": row[7],
        "created_at": row[8]
      })
      
      return data
  @classmethod
  def convertToColumns(self, columns):
    if columns[0] == "Nombre":                  columns[0] = "name_course" 
    if columns[1] == "Descripcion":             columns[1] = "description_course" 
    if columns[2] == "Profesor":                columns[2] = "teacher_course" 
    if columns[3] == "Fecha de inicio":         columns[3] = "startdate_course" 
    if columns[4] == "Fecha de finalizacion":   columns[4] = "enddate_course" 
    if columns[5] == "Hora de inicio":          columns[5] = "starttime_course" 
    if columns[6] == "Hora de finalizacion":    columns[6] = "endtime_course" 
    if columns[7] == "Precio":                  columns[7] = "price" 
    if columns[8] == "Multimedia":              columns[8] = "media_course" 
    
    return columns