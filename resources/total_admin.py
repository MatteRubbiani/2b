from flask_restful import Resource, request
from models.users import UserModel, select_all



class TotalAdmin (Resource):
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            users=select_all()
            a=[]
            if users:
                c=[]
                for i in users:
                    b={"username":i.username,
                    "conteggio":i.conteggio,
                    "isYou":0,
                    "mail":i.mail}
                    c.append(b)
                return c
