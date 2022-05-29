import os
from flask import Flask
from flask import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from PixelPerfect import PixelPerfect
#from flask_sqlalchemy import SQlAlchemy


app= Flask(__name__)
PixelPerfect.initialiseGame()
app.config.from_object(Config)  

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

basedir= os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir,'database.db'))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///pixel-perfect.fb'



db = SQLAlchemy(app)
migrate=Migrate(app,db)


from app import routes,api

