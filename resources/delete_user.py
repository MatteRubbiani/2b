from db import db
from flask_restful import Resource, request


from models.users import UserModel, class_users, select_all


class DeleteUser(Resource):
    def post(self):
        data=request.get_json()
        mail=data["mail"]
        admin=data["admin"]
        password=data["password"]
        if (admin=="matteo" and password=="matteo"):
            user=UserModel.find_by_mail(mail)
            if user:
                user.delete_from_db()
                return "done",200
            return "ops", 405
        return "pesce", 401
