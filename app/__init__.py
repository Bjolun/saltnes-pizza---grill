import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
