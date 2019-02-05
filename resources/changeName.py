from flask_restful import Resource, request
from models.users import UserModel


class ChangeName(Resource):
    def post(self):
        mail=request.args.get('mail')
        username=request.args.get('username')
        user=UserModel.find_by_mail(mail)
        if user:
            user.username=username
            user.save_to_db()
            return {"message":"username changed successfully"}, 200
        return {"message":"user does not exist"}, 500
