# Flask-Blog

##A web application that allows the users to create posts, comment on those posts.

## By [peter kuria](https://github.com/peter302)


## Description
This is a web application that allows various users to create posts. Users can also be able to view posts and comments from other users and comment those posts. For a user to do any of that, they need to have registered.


## User Stories
1. As a user, I would like to view the blog posts on the site
2. As a user, I would like to comment on blog posts
3.   As a user, I would like to view the most recent posts
3. As a user, I would like to an email alert when a new post is made by joining a subscription.
4. As a user, I would like to see random quotes on the site
5. As a writer, I would like to sign in to the blog.
6. As a writer, I would also like to create a blog from the application.
7. As a writer, I would like to delete comments that I find insulting or degrading.
8. As a writer, I would like to update or delete blogs I have create


## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display blogposts |enter the site URL
|Create a post | **Click** create a post | A page with a form to create a post will pop up |
|Add a comment | **Click** Add Comment |A page with a form to create a comment will pop up  |

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/peter302/flask-blog-post.git
* $ cd flask_blog
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh
