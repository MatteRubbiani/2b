from flask_restful import Resource, request

from db import db

from models.users import UserModel

class Name(Resource):
    def get(self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            return {"message":user.username}
        return {"message":"user does not exist"}
