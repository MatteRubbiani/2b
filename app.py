import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from resources.add import Add
from resources.delete import Delete
#from resources.auth import Auth
from resources.register import Register
from security import identity, authenticate
from resources.name import Name
from resources.confirm_mail import ConfirmMail
#from resources.createclass import CreateClass
#from resources.joinclass import JoinClass
from resources.total import Total
from resources.total_admin import TotalAdmin
from resources.erase import Erase
from resources.remote import SelfDistruct
from resources.delete_user import DeleteUser
from resources.addAdmin import AddAdmin

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.secret_key="Matteo"
api=Api(app)
#app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"

jwt = JWT (app, authenticate, identity)
app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)

#@app.before_first_request
#def create_table():
    #db.create_all()

api.add_resource(Add, "/add")
api.add_resource(Delete, "/all")
#api.add_resource(Auth, "/pwd")
api.add_resource(Register, "/register")
api.add_resource(Name, "/name")
api.add_resource(ConfirmMail, "/confirm/<string:token>")
#api.add_resource(CreateClass, "/class/create")
#api.add_resource(JoinClass, "/class/join")
api.add_resource(Total, "/total")
api.add_resource(TotalAdmin, "/total/admin")
api.add_resource(Erase, "/erase")
api.add_resource(SelfDistruct, "/nobuonaidea")
api.add_resource(DeleteUser, "/deleteuser")
api.add_resource(AddAdmin, "/add/admin")


if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
