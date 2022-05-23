from crypt import methods
from dbm import dumb
from distutils.log import debug
from email.policy import default
from enum import unique
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
#FORM CLASSES
#------------------
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8, max=40)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8, max=40)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])

#---------------

DATABASE_PATH = '/home/seand/Documents/git/CITS3403-Project/flasklogin'

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ DATABASE_PATH +"/database.db"
db = SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view  = 'login'


#Database Models
#------------------
#user mixin adds 'stuff' to flask db 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class ImageTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagepath = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, unique=True, nullable=False)
    # mimetypes = db.Column(db.Text, nullable=False)


class Player_History(db.Model): #Stores every session for a player
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False) #use Username to return results for that username
    answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
    answer_count = db.Column(db.Integer, nullable=False)
    img_id = db.Column(db.Integer, nullable=False)
    date_submitted = db.Column(db.DateTime, nullable=True)




@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        #Do something about sending pincode to email address
        # return '<h1>' + form.username.data + ' ' + form.email.data  +' ' + form.password.data + '</h1>'
        hashed_pass = generate_password_hash(form.password.data, method='sha256') #encoding password for integrity
        
        #Insert Data into DB
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        #Some arbritray response
        return '<h1> Successfully added New User! </h1>'
    return render_template('signup.html', form=form)


#Create User Loader, Connection to flask login and actual database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    #Check if form submitted #validate submit
    if form.validate_on_submit():
        #Return values submitted
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>' #data of username/password input submitted
        #Query Database if user exists in the database
        user = User.query.filter_by(username=form.username.data).first() #Returns Row Object User
        if user: #User Exists!!
            if check_password_hash(user.password, form.password.data): #Password Correct!
                login_user(user, remember=form.username.data)
                return redirect(url_for('dash'))

        #username or password doesnt exist
        return '<h1> Invalid username or password </h1>' #

    #not submitted render template
    return render_template('login.html', form=form) # Pass form to template for form object to be used in login.html

#Create some Rows for Player historyw 

# def dateNow():
#     today = datetime.datetime.now()
#     date_time = today.strftime("%Y-%m-%d %H:%M:%S")
#     return date_time
shit = "2022-05-23 23:33:40"
# datetime.datetime.now()
def Dump():
    for _ in range(1):
        hist = Player_History(
                    username="Testings", 
                    answer_history= "Taj Mahal|Reeses Puff|Grand Canyon|St. Petersburg",
                    answer_count = 4,
                    img_id = 11, 
                    date_submitted= datetime.datetime.now()
                    )
                    
        db.session.add(hist)
        db.session.commit()

# Dump()

#Cannot Access Dashboard without login
@app.route('/dashboard')
@login_required
def dash():
    headings = ["ID", "Username", "Answer_History", "Answer_Count","img_id","DateSubmitted"]
    player_history = Player_History.query.filter_by(username=current_user.username) #Returns Rows
    return render_template('dashboard.html', name=current_user.username, player_history=player_history, headings=headings)





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)