import os
from flask import Flask
from flask_restful import Api
from datetime import timedelta

class Auth(Resource):
    def get(self):

        return {"Username":"WaitingAdmin",
                "Password":"WaitingPassword"}
