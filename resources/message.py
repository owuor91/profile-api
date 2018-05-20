from flask_restful import Resource
from models.message_model import MessageModel
from flask import request

class Message(Resource):
    def get(self, message_id):
        message = MessageModel.find_message_by_id(message_id)

        if message:
            return {'message':message.to_json()}, 200
        return {'message': 'message not found'}, 404

    def post(self):
        message = MessageModel(request.form.get('title'), request.form.get('body'), request.form.get('author_id'))
        message.save_to_db()
        return {'message': message.to_json()}, 201

    def put(self, message_id):
        title = request.form.get('title')
        body = request.form.get('body')

        message = MessageModel.find_message_by_id(message_id)

        if message is None:
            message = MessageModel(title, body, author_id)
        else:
            if title:
                message.title = title
            if body:
                message.body = body

        message.save_to_db()
        return {'message': message.to_json()}


    def delete(self, message_id):
        message = MessageModel.find_message_by_id(message_id)
        if message:
            message.delete_from_db()
        return{'message': 'item deleted'}

class Messages(Resource):
    def get(self):
        return {'messages': [message.to_json() for message in MessageModel.query.all()]}
