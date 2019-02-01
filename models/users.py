from db import db


class UserModel(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    mail=db.Column(db.String(40))
    password=db.Column(db.String(150))
    username=db.Column(db.String(40))
    ordine=db.Column(db.Integer)
    classe_id=db.Column(db.Integer)
    conteggio=db.Column(db.Integer)
    confermato=db.Column(db.Boolean)

    def __init__(self, id, mail, username, password , ordine, classe_id, conteggio, confermato):
        self.id=id
        self.mail=mail
        self.username=username
        self.ordine=ordine
        self.classe_id=classe_id
        self.conteggio=conteggio
        self.confermato=confermato



    @classmethod
    def find_by_mail(cls, mail):
        return UserModel.query.filter_by(mail=mail).first()

    @classmethod
    def find_by_id(cls, id):
        return UserModel.query.filter_by(id=id).first()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


def class_users (classe_id):
    users= UserModel.query.filter_by(classe_id=classe_id)
    list=[]
    if users:
        for i in  users:
            list.append(i)
        return list

def add_to_class (mail, classe_id):
    user=UserModel.query.filter_by(mail=mail).first()
    user.classe_id=classe_id
    user.save_to_db()
