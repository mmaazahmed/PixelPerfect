from flask import render_template, url_for
from app import app
from crypt import methods
from flask import request
from scripts import pixelate

guess_history=[]
@app.route('/',methods=["POST"])
@app.route('/index') 
def index():
    if request.method=='POST':
        guess= request.form.get("guesstxt")
        print("my guess was",guess)
        guess_history.append(guess)
        pixelate.init()
        pixelate.pixel("bmo.png",len(guess_history))
        print("imhere",guess_history)
        return render_template('base.html')
    else:
        return render_template('base.html')