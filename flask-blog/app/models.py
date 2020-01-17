
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __table__='users'
    id=db.column(db.Integer,primary_key=True)
    name=db.column(db.string(255),index=True)
    email=db.column(db.text(),unique=True)
    blog=db.relationship('Blogpost',bakref='blogpost.id',lazy='dynamic')
    comment=db.relationship('Comments',bakref='comment',lazy='dynamic')

    def user_save(self):
        db.session.add(self)
        db.session.commit()




class Blogpost(db.Model):
    __table__='blogpost'
    id=db.column(db.Integer,primary_key=True)
    title=db.column(db.string(255),index=True)
    content=db.column(db.text())
    date_posted=db.column(db.DateTime(),default=datetime.utcnow)
    user_id=db.column(db.Integer,db.ForeigKey('users.id'))
    comments=db.relationship('Comments',backref='comment')



class Comments(db.Model):
    __table__='comment'

    id=db.column(db.Integer,primary_key=True)
    content=db.column(db.text(),index=True)
    user_id=db.column(db.Integer,db.ForeigKey('users.id'))
    blogpost_id=db.column(db.Integer,db.ForeigKey('blogpost.id'))
