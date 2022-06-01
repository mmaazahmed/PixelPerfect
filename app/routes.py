
from datetime import datetime
from flask import render_template, url_for
from app import app
from flask import request
from config import Config
from app import PixelPerfect



@app.route('/')
@app.route('/index')
def index():
    #print(datetime.now())
    PixelPerfect.check_time()
    return render_template('index.html')

    
    
@app.route('/login.html')
def login():
    return render_template('login.html')

