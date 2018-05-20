from db import db

class MessageModel(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('UserModel')

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id

    def to_json(self):
        return {'id': self.id, 'title': self.title, 'body': self.body, 'author_id': self.author_id, 'author': self.author.to_json()}

    @classmethod
    def find_message_by_id(cls, message_id):
        return cls.query.filter_by(id=message_id).first()

    @classmethod
    def list_messages_by_author(cls, author_id):
        return cls.query.filter_by(author_id = author_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
