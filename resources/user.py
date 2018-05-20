import sqlite3
from flask_restful import Resource, reqparse
from models.user_model import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('firstname',
    type = str,
    required = True,
    help = 'please provide first name')
    parser.add_argument('lastname',
    type = str,
    required = True,
    help = 'please provide last name')
    parser.add_argument('password',
    type = str,
    required = True,
    help = 'please provide password')
    parser.add_argument('phonenumber',
    type = str,
    required = True,
    help = 'please provide phonenumber')
    parser.add_argument('avatar',
    type = str)

    def post(self):
        data = User.parser.parse_args()

        if UserModel.find_user_by_phonenumber(data['phonenumber']):
            return {'message': 'a user with the number {} already exusts'.format(data['phonenumber'])},400

        user = UserModel(data['firstname'], data['lastname'], data['password'], data['phonenumber'], data['avatar'])
        user.save_to_db()
        return {'message': 'user created successfully'}, 201
