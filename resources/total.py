from flask_restful import Resource, request
from models.users import UserModel, select_all



class Total (Resource):
    def get (self):
        data=request.get_json()
        mail=data["mail"]
        user=UserModel.find_by_mail(mail)
        if user:
            users=select_all()
            a=[]
            if users:
                newlist = sorted(users, key=lambda x: x.ordine)
                for i in newlist:
                    if i.ordine!=None:
                        a.append(i)
                c=[]
                for i in a:
                    b={"username":i.username,
                    "conteggio":i.conteggio}
                    c.append(b)
                return {"list":c}
