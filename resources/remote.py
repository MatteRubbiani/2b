from db import db
from flask_restful import Resource, request


from models.users import UserModel, select_all


class SelfDistruct(Resource):

    def delete(self):
        data=request.get_json()
        codice=data["secret"]
        if codice=="eliminatutto":
            users=select_all()
            if users:
                for i in users:
                    i.delete_from_db()
            return "fatto"
        return "error 404"
