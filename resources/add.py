from db import db
from flask_restful import Resource, request


from models.users import UserModel, class_users, select_all


class Add(Resource):
    def post(self):
        data=request.get_json()
        mail=data["mail"]
        user=UserModel.find_by_mail(mail)
        if user is None:
            return "does not exist", 500

        if user.ordine:
            return "already in list"
        users=class_users(user.classe_id)
        if users:
            ids=[]
            for i in users:
                if i.ordine is not None:
                    ids.append(i.ordine)
            if ids:
                top=max(ids)
                ordine1=top+1
            else:
                ordine1=1
        else:
            ordine1=1
        user.ordine=ordine1
        user.conteggio=user.conteggio+1
        user.save_to_db()
        return user.conteggio
        return {"message": "user added to list"}, 200

    def delete(self):
        data=request.get_json()
        mail=data["mail"]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.ordine is not None:
                user.ordine=None
                user.save_to_db()
                return {"message":"deleted"}, 200
            return "not in list"
        return {"message":"user does not exist"}, 500

    def get(self):
        data=request.get_json()
        mail=data["mail"]
        user=UserModel.find_by_mail(mail)
        if user is None:
            return "does not exist"
        users=select_all()
        a=[]
        if users:
            k=[]
            for i in users:
                if i.ordine is not None:
                    k.append(i)
            newlist = sorted(k, key=lambda x: x.ordine)
            for i in newlist:
                    a.append(i.username)
            return a
            c=""
            if a:
                for i in a:
                    if i:
                        c=c+i+","
                d=c[:-1]
                return {"name":d}, 200
        return {"name":""}
