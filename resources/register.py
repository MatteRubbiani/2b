from flask_restful import Resource, request
import datetime
from itsdangerous import URLSafeTimedSerializer
import smtplib
import hashlib, uuid


from db import db

from models.users import UserModel

class Register(Resource):
    def post(self):
        data=request.get_json()
        mail=data["mail"]
        username=data["username"]
        password=data["password"]
        user=UserModel.find_by_mail(mail)
        #if user:
            #if user.confermato==True:
                #return "mail already taken", 400
        now = datetime.datetime.now()
        epsw=password.encode('utf-8')
        hashed_password = hashlib.sha512(epsw).hexdigest()
        user=UserModel(None, mail, username, None, 0, None, 0, False)
        user.password=password

        user.save_to_db()
        s = URLSafeTimedSerializer("password1")
        token=s.dumps(mail, salt="emailconfirm")
        #link="http://127.0.0.1:5000/confirm/"+token
        link="https://smartmates.herokuapp.com/confirm/"+token
        subject="Conferma la tua mail su WaitingList"

        text = """

Ciao {}!
Grazie per esserti registrato.
Clicca il link qui sotto per completare la registrazione.


{}

Se non hai richiesto un account non preoccuparti, qualcuno si sara' confuso.

Saluti,

il Team WaitingList



         """.format(username,link)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login("smartmates2018@gmail.com", "smartmates1")
        #server.sendmail("smartmates2018gmail.com", mail, message)

        return {"message":"user created, to be confirmed"}, 200
