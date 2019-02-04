from flask_restful import Resource, request
from models.users import UserModel, select_all



class Total (Resource):
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            users=select_all()
            a=[]
            if users:
                b=[]
                for i in users:
                    if i.ordine is not None:
                        b.append(i)
                newlist = sorted(b, key=lambda x: x.ordine)
                for i in newlist:
                    if i.ordine!=None:
                        a.append(i)
                c=[]
                for i in a:
                    if i.id==user.id:
                        p=1
                    else:
                        p=0
                    b={"username":i.username,
                    "conteggio":i.conteggio,
                    "isYou":p,
                    "mail":i.mail}
                    c.append(b)
                return c
