from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
#import image

app = Flask(__name__)
app.static_folder = 'static'
app.config.from_pyfile('config.py')
app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()