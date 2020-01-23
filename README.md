## Flask-Blog
   -  web application that allows the users to create posts, comment on those posts.

## Author
   - By peter kuria


## Description
  - This is a web application that allows various users to create posts. Users can also be able to view posts and comments from other users and comment those posts. For a user to do any of that, they need to have registered.

## User Stories
 - As a user, I would like to view the blog posts on the site
 - As a user, I would like to comment on blog posts
 - As a user, I would like to view the most recent posts
 - As a user, I would like to an email alert when a new post is made by joining a subscription.
 - As a user, I would like to see random quotes on the site
 - As a writer, I would like to sign in to the blog.
 - As a writer, I would also like to create a blog from the application.
 - As a writer, I would like to delete comments that I find insulting or degrading.
 - As a writer, I would like to update or delete blogs I have create
## Specifications
  ## Behaviour	Input	Output
    - Display blogposts	enter the site URL	
    - Create a post	Click create a post	A page with a form to create a post will pop up
    - Add a comment	Click Add Comment	A page with a form to create a comment will pop up
 ## Prerequisites
  -Python3.6
## Setup/Installation Requirements
  - internet access
  - $ git clone https://github.com/peter302/flask-blog-post.git
  - $ cd flask_blog
  - $ python3.6 -m venv virtual (install virtual environment)
  - $ source virtual/bin/activate
  - $ python3.6 -m pip install -r requirements.txt (install all dependencies)
  - Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
  - $ ./start.sh
## How it works
  - A user needs to sign up
  - A user the needs to sign in to vote and post pitches
## CREDITS
  - Google.com, StackOverflow.com and LMS
## Support and Contacts
   - In case You have any issues using this code please do no hesitate to get in touch with me through petermbaik@gmail.com or leave a commit here on github.

## Known Bugs
   - No known bugs

## Technologies Used
  - Python3.6
  - Flask framework
  - Bootstrap
  - PostgreSQL
## License
  ## MIT License (c)2020 
        -Peter Kuria
        
        
        -  - Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWA
