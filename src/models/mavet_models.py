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

  def __init__(self, name, last_name, datebirth, username, phone, email, password):
    self.name_user      = name
    self.last_name_user = last_name
    self.datebirth      = datebirth
    self.email_user     = email
    self.phone_user     = phone
    self.username_user  = username
    self.password_user  = password
    self.specialty_id   = "Estudiante"
    self.type_id        = "Estandar"
    
class Works_art(db.Model):
  __tablename__     = "works_art"
  
  id                = db.Column(db.Integer, primary_key=True)
  title_work        = db.Column(db.String(50), nullable=False)
  description_work  = db.Column(db.String(100), nullable=False)
  img_work          = db.Column(db.String(200), nullable=False)
  likes_work        = db.Column(db.Integer, default=0)
  category          = db.Column(db.String(50), db.ForeignKey("categories.name_category", ondelete="CASCADE"), nullable=False)
  author_id         = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  
  category_work_art = db.relationship("Category", passive_deletes=True, backref="categories")
  author_work_art   = db.relationship("User", passive_deletes=True, backref="users")
  
  def __init__(self, title, description, img, category, author_id):
    self.title_work       = title
    self.description_work = description
    self.img_work         = img
    self.category         = category
    self.author_id        = author_id