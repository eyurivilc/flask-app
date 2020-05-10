from flask import (Flask, make_response, redirect, render_template, request,
                   session)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a productor']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def error_server(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    make = redirect('/hello')
    response = make_response(make)
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
    }

    return render_template('hello.html', **context)
