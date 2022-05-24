import os
import threading
import time
from flask import Flask
from flask import Config
from scripts import pixelate


imagepath='bmo.png'



app= Flask(__name__)

isStartUp=True
app.config.from_object(Config)  

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

from app import routes,api

