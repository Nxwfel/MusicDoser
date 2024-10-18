from flask import render_template,request,flash,redirect,url_for,jsonify
from flask_login import login_user,logout_user,login_required,current_user
from flask_admin import AdminIndexView

from pygame import mixer
import os

from models import User
from forms import RegistrationForm,LoginForm,LogoutForm

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')

def register_routes(app,db,bcrypt,limiter):    
    mixer.init()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register',methods=['GET','POST'])
    def register():
        
        form = RegistrationForm()
        if request.method == 'POST':
            if form.validate_on_submit():  # Validate the form 

                email = form.email.data
                password = form.password.data

                # Check if User exists by Email
                existing_user = User.query.filter_by(email=email).first()
                if existing_user:
                    flash(message='User already exists. Please login.', category='error')
                    return redirect(url_for('login'))
                
                # Hash the Password
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                
                # Create New User and Save to Database
                new_user = User(email=email,password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created successfully! You can now log in.', 'success')
                return redirect(url_for('login'))
            else:
                # If form validation fails, display errors
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'Error in {field}: {error}', 'error')

        return render_template('register.html', form=form)
        
        
    @app.route('/login', methods=['GET', 'POST'])
    @limiter.limit("10 per minute")
    def login():
        # Check if its logged in
        if current_user.is_authenticated:
            flash(message='You Already Logged in',category='error')
            return redirect(url_for('index'))
        
        form = LoginForm()
        
        if request.method == 'POST':
            if form.validate_on_submit():
                user = User.query.filter_by(email=form.email.data).first()
                
                # Check if the User exists and Password Incorrect
                if user:
                    if bcrypt.check_password_hash(user.password,form.password.data):
                        login_user(user)
                        flash(message='Login successful!',category='success')
                        return redirect(url_for('index'))
                else:
                    flash(message='Login unsuccessful. Please check your email and password.',category='error')
            else:
                # If form validation fails, display errors
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'Error in {field}: {error}', 'error')

        return render_template('login.html',form=form)

    @app.route('/logout',methods=['GET','POST'])
    @login_required
    def logout():
        form = LogoutForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                logout_user()
                flash('You have been logged out.', 'success')
                return redirect(url_for('index'))
            
        return render_template('logout.html',form=form)
    

    @app.route('/tracks/<int:track_id>')
    @login_required
    def get_track(track_id):
        return render_template(f'track_{track_id}.html')

    
    @app.route('/play/<track_name>')
    def play_track(track_name):
        track_path = os.path.join('static', 'tracks', track_name)
        if os.path.exists(track_path):
            mixer.music.load(track_path)
            mixer.music.play()
            return jsonify({'status': 'playing', 'track': track_name}), 200
        return jsonify({'status': 'error', 'message': 'Track not found'}), 404

    @app.route('/stop')
    def stop_track():
        mixer.music.stop()
        return jsonify({'status': 'stopped'}), 200