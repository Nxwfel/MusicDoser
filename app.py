from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tracks/<int:track_id>')
def get_track(track_id):
    return render_template(f'track_{track_id}.html')