from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,Length,DataRequired
from flask_wtf.recaptcha import RecaptchaField

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=50)])
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=50)])
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')
