from db import db
from flask_restful import Resource


from users import UsersModel


class Delete(Resource):

    def delete(self):
        users=UsersModel.get_all()
        if users:
            for i in users:
                i.delete_from_db()
            return "users deleted",200

        return "no users to delete"
