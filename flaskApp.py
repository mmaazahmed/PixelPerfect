from flask import Flask, render_template
#import image

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()