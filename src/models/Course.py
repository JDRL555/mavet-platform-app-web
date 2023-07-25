from sqlalchemy.sql           import text
from src.models.mavet_models  import Course as Course_model
import cloudinary.uploader

class Course:
  @classmethod 
  def createCourse(self, db, course):
    try:
      response = {"msg": "Curso registrado exitosamente", "error": False}

      file  = course["media"]
      image = cloudinary.uploader.upload(file=file, quality=50) 

      
      new_course = Course_model(
        name=course["name"],
        description=course["description"],
        teacher=course["teacher"],
        startdate=course["startdate"],
        enddate=course["enddate"],
        starttime=course["starttime"],
        endtime=course["endtime"],
        price=course["price"],
        media=image["url"],
      )
      
      db.session.add(new_course)
      db.session.commit()
      
      return response
      
    except Exception as error:
      print(error)
      response = {"msg": "ERROR, intentelo mas tarde", "error": True}
      return response
    
  
  @classmethod
  def getAll(self, db):
    sql         = text("SELECT * FROM courses ORDER BY created_at DESC;")
    courses     = db.session.execute(sql)
    courses     = tuple(courses)
    
    data = []
    
    for row in courses:
      data.append({
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "teacher": row[3],
        "startdate": row[4],
        "enddate": row[5],
        "starttime": str(row[6]),
        "endtime": str(row[7]),
        "price": row[8],
        "created_at": row[10],
        "media": row[9],
      })
      
    return data

  @classmethod
  def updateCourse(self, db, id, columns, values):
    try:
      response  = {"msg": "Editado exitosamente", "error": False}
      sql = f'''
        SELECT name_course, description_course, teacher_course, startdate_course, enddate_course, starttime_course, endtime_course, price 
        FROM courses WHERE id = {id};
      '''
      
      course     = db.session.execute(text(sql))
      course     = list(course)

      print(course)

      if not course:
        response["msg"] = "Evento no encontrado"
        response["error"] = True
        
        return response
      
      course       = course[0]
      new_values  = []
      new_columns = []

      for index, row in enumerate(course):
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

      sql = "UPDATE courses SET "

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
  def deleteCourse(self, db, id):
    try:
      response  = {"msg": "Eliminado exitosamente", "error": True}
      sql       = f"DELETE FROM courses WHERE id = {id};"
      
      db.session.execute(text(sql))
      db.session.commit()

      return response

    except Exception as error:
      print(error)
      return {"msg": "ERROR, intentelo mas tarde", "error": True}  
  
  @classmethod
  def convertToColumns(self, columns):
    for index, _ in enumerate(columns):
      if columns[index] == "Nombre":                  columns[index] = "name_course" 
      if columns[index] == "Descripcion":             columns[index] = "description_course" 
      if columns[index] == "Profesor":                columns[index] = "teacher_course" 
      if columns[index] == "Fecha de inicio":         columns[index] = "startdate_course" 
      if columns[index] == "Fecha de finalizacion":   columns[index] = "enddate_course" 
      if columns[index] == "Hora de inicio":          columns[index] = "starttime_course" 
      if columns[index] == "Hora de finalizacion":    columns[index] = "endtime_course" 
      if columns[index] == "Precio":                  columns[index] = "price" 
      if columns[index] == "Multimedia":              columns[index] = "media_course" 
    
    return columns