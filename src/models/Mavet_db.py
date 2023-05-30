from utils.db import db

class Mavet_db(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    name_user      = db.Column(db.String(100) )
    last_name_user = db.Column(db.String(100) )
    email_user     = db.Column(db.String(100) )
    phone_user     = db.Column(db.String(100) )
    specialty_user = db.Column(db.String(100) )
    type_user      = db.Column(db.String(100) )
    avatar_user    = db.Column(db.String(100) )
    username_user  = db.Column(db.String(100) )
    password_user  = db.Column(db.String(100) )
    created_at     = db.Column(db.String(100) )

    def __init__(self, name_user, last_name_user, email_user, phone_user, specialty_user, type_user, avatar_user, username_user, password_user, created_at):
        self.name_user      = name_user
        self.last_name_user = last_name_user
        self.email_user     = email_user
        self.phone_user     = phone_user
        self.specialty_user = specialty_user
        self.type_user      = type_user
        self.avatar_user    = avatar_user
        self.username_user  = username_user
        self.password_user  = password_user
        self.created_at     = created_at
