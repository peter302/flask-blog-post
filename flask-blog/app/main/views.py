from flask import render_template,url_for,request,abort,redirect
from .models import Blogpost,User,Comments
from .import main
from forms import commentform,postform
from flask_login import login_required,current_user

@main.route('/')
def index():
    '''a function to take a user to the home page'''

    title="welcome to our new blog post"
    posts=Blogpost.get_posts()

    return render_template('index.html',title=title,posts=posts)

@main.route('/post')
def post('/post'):
    form=postforms()

    if form.validate_on_submit():
        title=form.title.data
        content=form.content.data
        date_posted=form.date_posted.data

        new_post=Blogpost(title=title,content=content,date_posted=date_posted)
        new_post.post_save()

        return redirect(url_for('main.index'))
    return render_template('post.html',postform=form)


    


@main.route('/post/comment')
def new_comment(post_id):
    post=Blogpost.query.filter_by(id=post_id).first()
    form=commentform()

    if form.validate_on_submit():
        content=form.content.data
        new_comment=Comments(content=content,blogpost_id=post_id,user_id=current_user.id)

        new_comment.comment_save()

        return redirect(url_for('main.comment'))
    title='make a new comment here'

    return render_template('new_comment.html',title=title,post=post,commentform=form)
