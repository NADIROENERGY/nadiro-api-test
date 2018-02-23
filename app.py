import os

from flask import Flask, request
from flask_restplus import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') # 2nd par used when URL not found
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemy has its own tracker, so deactivate Flask tracker
app.secret_key = 'asdaru347qcnz4r7r8527nftve8'
api = Api(app)

# ADD RESROUCES
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
jwt = JWT(app, authenticate, identity) # /auth
	
if __name__ == '__main__':
	from db import db
	db.init_app(app)

	if app.config['DEBUG']:
		@app.before_first_request
		def create_tables():
			db.create_all()

	app.run(port=5000)