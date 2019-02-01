import os
from flask import Flask
from flask_restful import Api
from datetime import timedelta
from db import db
from flask_restful import Resource

class Auth(Resource):
    def get(self):
        return {"Username":"WaitingAdmin",
                "Password":"WaitingPassword"}
