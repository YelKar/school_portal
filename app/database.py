from app import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(500), nullable=False)

    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))

    sex = db.Column(db.String(1))
    classroom = db.Column(db.String(3))

    email = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f"<users {self.id}>"

