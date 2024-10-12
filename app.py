from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HomePage.html')

@app.route('/MusicDoser')
def music_doser():
    return render_template('Musicdoser.html')