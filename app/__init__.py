# __init__.py
# imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Creates an instance of the LoginManager
login_manager = LoginManager()

# Creates our Flask Application
app = Flask(__name__)

# NOT A SECRET KEY ! :(
app.config['SECRET_KEY'] = 'dev_key'

# configurating the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# Passes app through SQLAlchemy
db = SQLAlchemy(app)
Migrate(app,db)

from app import views

# Passes in app to configure the application to be able to manage users.
login_manager.init_app(app)

# Tell users what view to go to in order to login
login_manager.login_view = 'login'
