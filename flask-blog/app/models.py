
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    #method to save new user







class Blogpost(db.Model):
    __tablename__='blogpost'
    id=db.column(db.Integer,primary_key=True)
    title=db.column(db.string(255),index=True)
    content=db.column(db.text())
    comments=db.relationship('Comments',backref='comment')

    #method to save a new blogpost
    def post_save(self):
        db.session.add(self)
        db.session.commit()



class Comments(db.Model):
    __tablename__='comment'

    id=db.column(db.Integer,primary_key=True)
    content=db.column(db.text(),index=True)
    blogpost_id=db.column(db.Integer,db.ForeigKey('blogpost.id'))

    #a method to save a new comments
    def comment_save(self):
        db.session.add(self)
        db.session.commit()

    #a method to delete comments
