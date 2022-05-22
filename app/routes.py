from ast import Global
from pickle import TRUE
from flask import render_template, url_for
from app import app
from crypt import methods
from flask import request
from scripts import pixelate

imagepath='bmo.png'
pfs=[4,8,16,32,64]
print(imagepath,pfs)
@app.route('/')
@app.route('/index')
def index():
    pixelate.pixel(imagepath,pfs)
    return render_template('index.html')
    
@app.route('/login.html')
def login():
    return render_template('login.html')

