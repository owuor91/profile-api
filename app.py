import os
from flask import Flask
from flask_restful import Api
from resources.user import User
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, '/user')

if __name__ == '__main__':
	# from db import db
	# db.init_app(app)
	app.run(port=5000, debug=True)
