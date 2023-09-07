from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4d1b6a8662eff78fccab9ee6ca898d89'

@app.route("/")
def index():
    image_veg = url_for('static', filename='images/Picture of Vegetable (1).png')
    image_about = url_for('static', filename='images/About Picture.png')
    image_sleep = url_for('static', filename='images/Sleeping Picture.png')
    return render_template("index.html", image_veg = image_veg, image_about = image_about, image_sleep = image_sleep)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'abuse':
            flash('You have been logged in!', 'success')
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
    return render_template("home.html", image_v = image_v, image_about = image_about, image_sleep = image_sleep, image_comm = image_comm)

@app.route("/account")
def account():
    return render_template("account.html", title = 'Account')

if __name__ == '__main__':
    app.run(debug = True)