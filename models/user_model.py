import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    password = db.Column(db.String)
    phonenumber = db.Column(db.String(80))
    avatar = db.Column(db.String)

    def __init__(self, firstname, lastname, password, phonenumber, avatar):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.phonenumber = phonenumber
        self.avatar = avatar

    @classmethod
    def find_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_user_by_phonenumber(cls, phonenumber):
        return cls.query.filter_by(phonenumber = phonenumber).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {'id':self.id, 'firstname': self.firstname, 'lastname': self.lastname, 'phonenumber': self.phonenumber, 'avatar': self.avatar}
