from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('  Remember me!')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])

    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64)])

    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2',
                                                             message='Password must match')])

    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    submit = SubmitField('Register')
