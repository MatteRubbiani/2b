from db import db
from flask_restful import Resource


from models.users import UserModel


class Delete(Resource):

    def get(self):
        users=UsersModel.get_all()
        if users:
            for i in users:
                i.delete_from_db()
            return {"message":"users deleted"},200

        return {"message":"no users to delete"},501