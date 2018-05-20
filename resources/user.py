from flask import request
from flask_restful import Resource
from models.user_model import UserModel
from models.message_model import MessageModel

class User(Resource):

    def post(self):
        if UserModel.find_user_by_phonenumber(self.get_value('phonenumber')):
            return {'message': 'a user with the number {} already exists'.format(self.getValue('phonenumber'))},400

        user = UserModel(self.get_value('firstname'), self.get_value('lastname'), self.get_value('password'), self.get_value('phonenumber'), self.get_value('avatar'))
        user.save_to_db()
        return {'message': 'user created successfully'}, 201

    def get(self, user_id):
        user = UserModel.find_user_by_id(user_id)

        if user:
            return user.to_json(), 200
        return {'message': 'user not found'},404

    def put(self, user_id):
        user = UserModel.find_user_by_id(user_id)

        if user is None:
            return {'message': 'the user you are trying to edit doesn\'t exist' }

        firstname = self.get_value('firstname')
        lastname = self.get_value('lastname')
        avatar = self.get_value('avatar')

        if firstname:
            user.firstname = firstname
        if lastname:
            user.lastname = lastname
        if avatar:
            user.avatar = avatar

        user.save_to_db()
        return user.to_json()

    def get_value(self, key):
        return request.form.get(key)


class UserList(Resource):
    def get(self):
        return {'users': [user.to_json() for user in UserModel.query.all()]}


class UserByNumber(Resource):
    def get(self):
        phonenumber = request.args.get('phonenumber')
        user = UserModel.find_user_by_phonenumber(phonenumber)

        if user:
            return user.to_json(), 200
        return {'message': 'user not found'}, 404


class UserMessages(Resource):
    def get(self, user_id):
        return {'messages': [message.to_json() for message in MessageModel.list_messages_by_author(user_id)]}
