import os
from flask import Flask
from flask_restful import Api
from datetime import timedelta


from add import Get, Post, Delete1
from delete import Delete
from auth import Auth 



app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.secret_key="Matteo"
api=Api(app)
#app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"



#@app.before_first_request
#def create_table():
    #db.create_all()

api.add_resource(Get, "/get")
api.add_resource(Post, "/post")
api.add_resource(Delete1, "/delete")
api.add_resource(Delete, "/all")
api.add_resource(Auth, "/pwd")


if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
