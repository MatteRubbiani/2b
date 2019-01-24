import os

from flask import Flask
from flask_restful import Api
from datetime import timedelta


from add import Add



app= Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("HEROKU_POSTGRESQL_COBALT_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.secret_key="Matteo"
api=Api(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"



#@app.before_first_request
#def create_table():
    #db.create_all()

api.add_resource(Add, "/in")
#api.add_resource(CreateOrario, "/timetable/create")
#api.add_resource(OrarioGiorno, "/timetable/day")
#api.add_resource(Put, "/friend/put")


if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
