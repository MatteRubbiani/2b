from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel
from models.randomtag import randomtag
from models.users import UserModel
from models.classes import ClassModel

class CreateClass(Resource):

    def post(self):
        mail=request.args.get('mail')
        classe=request.args.get('class')
        user=UserModel.find_by_mail(mail)
        if user:
            tag=randomtag()
            class_to_add=ClassModel(None, classe, tag, user.id)
            class_to_add.save_to_db()
            class_added=ClassModel.find_by_tag(tag)
            return {"tag":tag}
        return {"message":"user does not exist"},400
