from flask import Flask, request
from flask_restplus import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemy has its own tracker, so deactivate Flask tracker
app.secret_key = 'asdaru347qcnz4r7r8527nftve8'
api = Api(app)

@app.before_first_request # Flask functionality
def create_tables():
	db.create_all()

# ADD RESROUCES
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
jwt = JWT(app, authenticate, identity) # /auth

def runApp(HOST, PORT):
	db.init_app(app)
	app.run(host=HOST, port=PORT, debug=True)
	
if __name__ == '__main__':
	from db import db
	runApp('localhost', 5000)
