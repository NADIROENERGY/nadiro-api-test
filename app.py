from flask import Flask, request
# from flask_restful import Api
from flask_restplus import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from database import Database

app = Flask(__name__)
# SQLAlchemy has its own tracker, so deactivate Flask tracker
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asdaru347qcnz4r7r8527nftve8'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# ADD RESROUCES
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

def runApp(HOST, PORT):
	from database import db
	db.init_app(app)
	Database.create_db()
	app.run(host=HOST, port=PORT, debug=True)
	
if __name__ == '__main__':
	runApp('localhost', 5000)
