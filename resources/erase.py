from db import db
from flask_restful import Resource, request


from models.users import UserModel, select_all


class Erase(Resource):

    def delete(self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            users=select_all()
            if users:
                for i in users:
                    i.conteggio=0
                    i.ordine=None
                    user.save_to_db()
                return {"message":"users deleted"},200
            return {"message":"no users"}, 500
        return {"message":"user does not exist"},500
