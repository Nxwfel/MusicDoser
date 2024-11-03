from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,Length,DataRequired#,Regexp
from flask_wtf.recaptcha import RecaptchaField

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=50)])
    '''
    Regexp(
        '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])',
        message="Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
    )'''
        
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=50)])
    '''
    Regexp(
        '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])',
        message="Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
    )'''
        
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')
