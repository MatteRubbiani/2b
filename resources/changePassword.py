from flask_restful import Resource, request
from models.users import UserModel
import hashlib, uuid

class ChangePassword(Resource):
    def post(self):
        mail=request.args.get('mail')
        oldPassword=request.args.get('oldPassword')
        newPassword=request.args.get('newPassword')
        user=UserModel.find_by_mail(mail)
        if user:
            epsw=oldPassword.encode('utf-8')
            hashed_password = hashlib.sha512(epsw).hexdigest()
            if user.password==hashed_password:
                epsw=newPassword.encode('utf-8')
                hashed_password = hashlib.sha512(epsw).hexdigest()
                user.password=hashed_password
                user.save_to_db()
                return {"message":"password changed successfully"}, 200
            return {"message":"wrong password"}, 401
        return {"message":"user does not exist"}, 500
