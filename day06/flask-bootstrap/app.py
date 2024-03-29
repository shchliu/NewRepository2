from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SDFBHRHTTJT'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("立即登录")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run()
