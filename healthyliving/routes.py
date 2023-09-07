from flask import render_template, url_for, flash, redirect
from healthyliving import app, db, bcrypt
from healthyliving.forms import RegistrationForm, LoginForm
from healthyliving.models import User
from flask_login import login_user, current_user, logout_user

@app.route("/index")
def index():
    image_veg = url_for('static', filename='images/Picture of Vegetable (1).png')
    image_about = url_for('static', filename='images/About Picture.png')
    image_sleep = url_for('static', filename='images/Sleeping Picture.png')
    return render_template("index.html", image_veg = image_veg, image_about = image_about, image_sleep = image_sleep)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template("login.html", title = 'Login', form = form)

@app.route("/home")
def home():
    image_v = url_for('static', filename='images/Picture of Vegetable (1).png')
    image_about = url_for('static', filename='images/About Picture.png')
    image_sleep = url_for('static', filename='images/Sleeping Picture.png')
    image_comm = url_for('static', filename='images/Community Picture.png')
    image_fit = url_for('static', filename='images/Fitness Picture.png')
    image_apple = url_for('static', filename='images/Apple Picture.png')
    return render_template("home.html", image_v = image_v, image_about = image_about, image_sleep = image_sleep, image_comm = image_comm, image_fit = image_fit, image_apple = image_apple)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/account")
def account():
    return render_template("account.html", title = 'Account')