from flask import render_template,url_for,request,abort,redirect
from ..models import Blogpost,User,Comments
from .import main
from forms import CommentForm,PostForm
from flask_login import login_required,current_user

@main.route('/')
def index():
    '''a function to take a user to the home page'''

    posts=Blogpost.query.all()
    title="welcome to our new blog post"

    return render_template('index.html',title=title,posts=posts)

@main.route('/post',methods=['GET','POST'])
@login_required
def post():
    form=PostForm()

    if form.validate_on_submit():
        title=form.title.data
        content=form.content.data
        date_posted=form.date_posted.data

        new_post=Blogpost(title=title,content=content)
        new_post.post_save()
        return redirect(url_for('main.index'))
    title='make a new blog here'
    return render_template('post.html',title=title,postform=form)


@main.route('/post/comment/<int:post_id>')
@login_required
def view_comment(post_id):
    post=Blogpost.query.filter_by(id=post_id)
    comments=Comments.query.filter_by(blogpost_id=post_id).all()
    if not comments:
        return redirect(url_for('main.new_comment'))
    title=f'comments section for {{post.title}}'

     return render_template('comment.html',title=title,post=post,comments=comments)




@main.route('/post/new_comment/<int:post_id>',methods=['GET','POST'])
def new_comment(post_id):
    post=Blogpost.query.filter_by(id=post_id)
    form=commentform()

    if form.validate_on_submit():
        content=form.content.data
        new_comment=Comments(content=content,blogpost_id=post.id)

        new_comment.comment_save()

        return redirect(url_for('main.view_comment'))
    title='make a new comment here'

    return render_template('new_comment.html',title=title,post=post,commentform=form)
