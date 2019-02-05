import smtplib
from flask_restful import Resource
from itsdangerous import URLSafeTimedSerializer
from models.users import UserModel



class ConfirmMail (Resource):
    def get (self, token):

        s = URLSafeTimedSerializer("password1")
        try:
            mail=s.loads(token, salt="emailconfirm")
            user=UserModel.find_by_mail_confirm(mail)
            if user:
                if user.confermato!=True:
                    user.confermato=True
                    user.save_to_db()
                    return "user confirmed"
                return "user already confirmed", 400
            return "user does not exist", 400
        except:
            return "your token is expired"
