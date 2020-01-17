from flask import Flask
from from flask_login import LoginManager
from flask_bootstrap import Bootstrap


login_manager=LoginManager()
bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__)

    #initializing extensions
    bootstrap.init_app(app)
    
