from utils.db import db
import datetime

class Type_user(db.Model):
  __tablename__ = "type_users"
  name_type     = db.Column(db.String(50), default="Estandar", primary_key=True)
  created_at    = db.Column(db.Date, default=datetime.datetime.now())
  
  def __init__(self, name):
    self.name_type = name
    
class Specialty_user(db.Model):
  __tablename__   = "specialty_users"
  name_specialty  = db.Column(db.String(50), default="Estudiante", primary_key=True)
  created_at      = db.Column(db.Date, default=datetime.datetime.now())
  
  def __init__(self, name):
    self.name_specialty = name
    
class Category(db.Model):
  __tablename__ = "categories"
  name_category = db.Column(db.String(50), nullable=False, primary_key=True)
  created_at    = db.Column(db.Date, default=datetime.datetime.now())
  
  def __init__(self, name):
    self.name_category = name

class User(db.Model):
  __tablename__   = "users"
  id              = db.Column(db.Integer, primary_key=True)
  name_user       = db.Column(db.String(100), nullable=False)
  last_name_user  = db.Column(db.String(100), nullable=False)
  datebirth       = db.Column(db.Date, nullable=False)
  email_user      = db.Column(db.String(300), nullable=False, unique=True)
  avatar_user     = db.Column(db.String(255), default="")
  username_user   = db.Column(db.String(100), nullable=False)
  phone_user      = db.Column(db.String(11), nullable=False)
  password_user   = db.Column(db.String(255), nullable=False)
  created_at      = db.Column(db.Date, default=f"{datetime.datetime.now()}")
  type_id         = db.Column(db.String(50), db.ForeignKey("type_users.name_type", ondelete="CASCADE"), nullable=False)
  specialty_id    = db.Column(db.String(50), db.ForeignKey("specialty_users.name_specialty", ondelete="CASCADE"), nullable=False)
  
  type_user       = db.relationship("Type_user", passive_deletes=True, backref="type_users")
  specialty_user  = db.relationship("Specialty_user", passive_deletes=True, backref="specialty_users")

  def __init__(self, name, last_name, datebirth, username, phone, email, password, specialty_user, type_user):
    self.name_user      = name
    self.last_name_user = last_name
    self.datebirth      = datebirth
    self.email_user     = email
    self.phone_user     = phone
    self.username_user  = username
    self.password_user  = password
    self.specialty_id   = specialty_user
    self.type_id        = type_user
    
class Works_art(db.Model):
  __tablename__     = "works_art"
  
  id                = db.Column(db.Integer, primary_key=True)
  title_work        = db.Column(db.String(50), nullable=False)
  description_work  = db.Column(db.String(100), nullable=False)
  img_work          = db.Column(db.String(200), nullable=False)
  likes_work        = db.Column(db.Integer, default=0)
  category          = db.Column(db.String(50), db.ForeignKey("categories.name_category", ondelete="CASCADE"), nullable=False)
  author_id         = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  created_at        = db.Column(db.Date, default=f"{datetime.datetime.now()}")
  
  category_work_art = db.relationship("Category", passive_deletes=True, backref="categories")
  author_work_art   = db.relationship("User", passive_deletes=True, backref="users")
  
  def __init__(self, title, description, img, category, author_id):
    self.title_work       = title
    self.description_work = description
    self.img_work         = img
    self.category         = category
    self.author_id        = author_id

class Preview_works_art(db.Model):
  __tablename__     = "previews"
  
  id                = db.Column(db.Integer, primary_key=True)
  title_work        = db.Column(db.String(50), nullable=False)
  description_work  = db.Column(db.String(100), nullable=False)
  img_work          = db.Column(db.String(200), nullable=False)
  category          = db.Column(db.String(50), db.ForeignKey("categories.name_category", ondelete="CASCADE"), nullable=False)
  author_id         = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  created_at        = db.Column(db.Date, default=f"{datetime.datetime.now()}")
  
  category_work_art = db.relationship("Category", passive_deletes=True, backref="categories_preview")
  author_work_art   = db.relationship("User", passive_deletes=True, backref="users_preview")
  
  def __init__(self, title, description, img, category, author_id):
    self.title_work       = title
    self.description_work = description
    self.img_work         = img
    self.category         = category
    self.author_id        = author_id
    
class Event(db.Model):
  __tablename__     = "events"
  
  id                = db.Column(db.Integer, primary_key=True)
  name_event        = db.Column(db.String(100), nullable=False)
  description_event = db.Column(db.Text, nullable=False)
  startdate_event   = db.Column(db.Date, nullable=False)
  enddate_event     = db.Column(db.Date, nullable=False)
  starttime_event   = db.Column(db.Time, nullable=False)
  endtime_event     = db.Column(db.Time, nullable=False)
  media_event       = db.Column(db.String(200))
  created_at        = db.Column(db.Date, default=f"{datetime.datetime.now()}")
  
  def __init__(self, name, description, startdate, enddate, starttime, endtime, media):
    self.name_event         = name
    self.description_event  = description
    self.startdate_event    = startdate
    self.enddate_event      = enddate
    self.starttime_event    = starttime
    self.endtime_event      = endtime
    self.media_event        = media
  
class Course(db.Model):
  __tablename__     = "courses"
  
  id                  = db.Column(db.Integer, primary_key=True)
  name_course         = db.Column(db.String(100), nullable=False)
  description_course  = db.Column(db.Text, nullable=False)
  teacher_course      = db.Column(db.String(50), nullable=False)
  startdate_course    = db.Column(db.Date, nullable=False)
  enddate_course      = db.Column(db.Date, nullable=False)
  starttime_course    = db.Column(db.Time, nullable=False)
  endtime_course      = db.Column(db.Time, nullable=False)
  price               = db.Column(db.Float, nullable=False)
  media_course        = db.Column(db.String(200))
  created_at          = db.Column(db.Date, default=f"{datetime.datetime.now()}")
  
  def __init__(self, name, description, teacher, startdate, enddate, starttime, endtime, price, media):
    self.name_course          = name
    self.description_course   = description
    self.teacher_course       = teacher
    self.startdate_course     = startdate
    self.enddate_course       = enddate
    self.starttime_course     = starttime
    self.endtime_course       = endtime
    self.price                = price
    self.media_course         = media