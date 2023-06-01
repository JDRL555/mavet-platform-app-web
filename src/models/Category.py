from sqlalchemy.sql import text
from models.mavet_models import Category as Category_model

class Category:
  @classmethod
  def getAll(self, db):
    sql = text("SELECT * FROM categories;")
    categories = db.session.execute(sql)
    categories = tuple(categories)
    return categories
  @classmethod
  def insertOne(self, db, category):
    sql             = text(f"SELECT * FROM categories WHERE name_category = '{category}';")
    category_exists = db.session.execute(sql)
    category_exists = tuple(category_exists)
    if category_exists:
      return False
    
    new_category = Category_model(category)
    db.session.add(new_category)
    db.session.commit()
    return category
    