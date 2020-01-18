
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __table__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.string(255),index=True)
    email=db.Column(db.text(),unique=True)
    pass_secure=db.Column(db.string(55))

    #method to save new user







class Blogpost(db.Model):
    __table__='blogpost'
    id=db.column(db.Integer,primary_key=True)
    title=db.column(db.string(255),index=True)
    content=db.column(db.text())
    date_posted=db.column(db.DateTime(),default=datetime.utcnow)
    comments=db.relationship('Comments',backref='comment')

    #method to save a new blogpost
    def post_save(self):
        db.session.add(self)
        db.session.commit()



class Comments(db.Model):
    __table__='comment'

    id=db.column(db.Integer,primary_key=True)
    content=db.column(db.text(),index=True)
    blogpost_id=db.column(db.Integer,db.ForeigKey('blogpost.id'))

    #a method to save a new comments
    def comment_save(self):
        db.session.add(self)
        db.session.commit()

    #a method to delete comments
