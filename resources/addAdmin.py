from flask_restful import Resource, request

from models.users import UserModel

class AddAdmin (Resource):

    def delete(self):
            mail=request.args.get('mail')
            user=UserModel.find_by_mail(mail)
            if user:
                if user.ordine is not None:
                    user.ordine=None
                    user.conteggio=user.conteggio+1
                    user.totale=user.totale+1
                    user.save_to_db()
                    return {"message":"deleted"}, 200
                return "not in list"
            return {"message":"user does not exist"}, 500

    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail_confirmed(mail)
        if user:
            users=select_all()
            if users:
                c=[]
                for i in users:
                    b={"username":i.username,
                    "totale":i.totale,
                    "isYou":0,
                    "mail":i.mail}
                    c.append(b)
            return c
