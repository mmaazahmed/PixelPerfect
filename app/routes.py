#from ast import Global
#from pickle import TRUE

from datetime import datetime
from flask import render_template, url_for
from app import app
#from crypt import methods
from flask import request
from config import Config



@app.route('/')
@app.route('/index')
def index():
    #print(datetime.now())
    return render_template('index.html')

    
    
@app.route('/login.html')
def login():
    return render_template('login.html')

