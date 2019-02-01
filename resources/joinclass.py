from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel
from models.users import UserModel


class JoinClass(Resource):

    #@jwt_required()
    def post(self):
        mail=request.args.get('mail')
        tag=request.args.get('tag')
        user=UserModel.find_by_mail(mail)
        if user:
            classe=ClassModel.find_by_tag(tag)
            if classe:
                user.classe_id=classe.id
                user.save_to_db()
                return {"message":"user added to class succesfully"}, 200
            return {"message":"class does not exist"} , 500
        return {"message":"user does not exist"}, 500

    #@jwt_required()
    def delete (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                user.classe_id=None
                user.save_to_db()
                return "user removed", 200
            return "user not in a class", 500
        return {"message":"user does not exist"}, 500
