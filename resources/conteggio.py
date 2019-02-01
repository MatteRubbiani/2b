from db import db
from flask_restful import Resource, request


from models.users import UsersModel, class_users


class Conteggio(Resource):
    def get(self):
        mail = request.args.get('mail')
        user=UsersModel.find_by_mail(mail)
        if user:
            users=class_users(user.classe_id)
            if users:
                x=[]
                for i in users:
                    a={i.username:i.conteggio}
                    x.append(a)


        return {"message": "user added to list"}, 200
