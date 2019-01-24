from db import db


class UsersModel(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(30))
    ordine=db.Column(db.Integer)


    def __init__(self, id, nome, ordine):
        self.id=id
        self.nome=nome
        self.ordine=ordine



    @classmethod
    def find_by_name(cls, nome):
        return UsersModel.query.filter_by(nome=nome).first()

    @classmethod
    def get_all(cls):
        a=UsersModel.query
        b=[]
        for i in a:
            b.append(i)

        return b


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
