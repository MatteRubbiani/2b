from db import db
from flask_restful import Resource, request


from users import UsersModel


class Add(Resource):


    def post(self):
        data=request.get_json()
        nome=data[0]
        user=UsersModel.find_by_name(nome)
        if user:
            return "already exists"

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

        return "user added"

    def delete(self):
        data=request.get_json()
        nome=data[0]
        user=UsersModel.find_by_name(nome)
        if user:
            user.delete_from_db()
            return "deleted"

        return "user does not exist"



    def get(self):
        users=UsersModel.get_all()
        a=[]
        for i in users:
            a.append(i.nome)


        return {"name": a}
