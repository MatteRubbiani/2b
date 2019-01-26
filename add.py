from db import db
from flask_restful import Resource, request


from users import UsersModel


class Add(Resource):


    def post(self):
        data=request.get_json()
        nome = request.args.get('name')
        #nome=data["name"]
        user=UsersModel.find_by_name(nome)
        if user:
            return "already exists", 500
        users=UsersModel.get_all()
        if users:
            ids=[]
            for i in users:
                ids.append(i.ordine)
                top=max(ids)
                ordine=top+1
        else:
            ordine=1
        user=UsersModel(None, nome, ordine)
        user.save_to_db()
        return {"message": "user added"}, 200


    def delete(self):
        data=request.get_json()
        nome=data["name"]
        user=UsersModel.find_by_name(nome)
        if user:
            user.delete_from_db()
            return {"message":"deleted"}, 200
        return {"message":"user does not exist"}, 500




    def get(self):
        users=UsersModel.get_all()
        a=[]
        for i in users:
            a.append(i.nome)
        c=""
        for i in a:
            c=c+i+","

        d=c[:-1]

        return {"name":d}, 200
