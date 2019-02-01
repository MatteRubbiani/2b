from db import db


class ClassModel(db.Model):
    __tablename__="classes"

    id = db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(50))
    tag=db.Column(db.String(30))
    admin=db.Column(db.Integer)


    def __init__(self, id, nome, tag, admin):
        self.id=id
        self.nome=nome
        self.tag=tag
        self.admin=admin

    @classmethod
    def find_by_tag(cls, tag):
        return ClassModel.query.filter_by(tag=tag).first()

    @classmethod
    def find_by_admin(cls, admin):
        classi=ClassModel.query.filter_by(admin=admin)
        if classi:
            x=[]
            for i in classi:
                x.append(i)
            return x
        return None

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
