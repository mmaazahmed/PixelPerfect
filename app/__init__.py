import os
import threading
import time
from flask import Flask
from flask import Config
from PixelPerfect import PixelPerfect
#from flask_sqlalchemy import SQlAlchemy


app= Flask(__name__)
PixelPerfect.initialiseGame()


app.config.from_object(Config)  
#db = SQLAlchemy(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

from app import routes,api

