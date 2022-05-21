

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))

# @app.before_request
# def before_request():
#     g.user = None

#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.pop('user_id', None)

#         username = request.form['username'] #Gets name parameter of input tag
#         password = request.form['password']
        
#         #Checks is user is in user database
#         user = [x for x in users if x.username == username][0]
        
#         #Checks if input and password is correct
#         if user and user.password == password:
#             session['user_id'] = user.id
#             return redirect(url_for('profile'))

#         #if incorrect redirect to login page || Implement a better version incorrect details popup
#         return redirect(url_for('login'))

#     #if not posting then return page again
#     return render_template('login.html')

# @app.route('/profile')
# def profile():
#     if not g.user:
#         return redirect(url_for('login'))
#         # return 'cannot find'
#         # abort(403)
#     #GET USER DETAILS AND PASSWORD AND ID
#     # PLAYER_HISTORY(id=0, username='hello',date_poster=,)
#     return render_template('profile.html')


# '''
# app = Flask(__name__)
# # app.debug = True
# app.secret_key = 'development key' #Secret keys are needed to run session


# @app.route('/login')
# def login():

#     if request.method == 'POST': #If access of page is to POST something
#         session.pop('user-id', None) # Will pop existing user session if already one in the session

#         username = request.form['username'] 
#         password = request.form['password'] #Gets name parameter of input tag with name password

#         #Check if user is a valid user else check password
#         #Uses loop to see if user in array
#         # || EVENTUALLY REPLACE THIS TO FIND NAME IN DATABASE ||
#         user = [x for x in users if x.username == username][0]
#         # Will fail is entered user not in the list/database || CREATE AN EXCEPTION CASE
#         #Check for password |\ Check queries

#         #IF Login is correct redirects to profile else redirects back to login
#         if user and user.password == password:
#             #Login the user
#             session['user-id']==user.id
#             return redirect(url_for('profile'))
#         #Suppose to return a message flashing but for now it just redirects back to the login page
#         return redirect(url_for('login'))
    
#     #If not post return template
#     return render_template('login.html')


#     #If user input successful app redirects to profile page


# @app.route('/profile')
# def profile():
#     if not g.user:
#         return redirect(url_for('login'))

#     return render_template('profile.html')


# # app.debug = True
# '''