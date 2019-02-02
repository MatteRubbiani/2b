from flask_restful import Resource, request
from models.users import UserModel, select_all



class TotalAdmin (Resource):
    def get (self):
        data=request.get_json()
        mail=data["mail"]
        user=UserModel.find_by_mail(mail)
        if user:
            users=select_all()
            a=[]
            if users:
                c=[]
                for i in users:
                    b={"username":i.username,
                    "conteggio":i.conteggio}
                    c.append(b)
                return {"list":c}
