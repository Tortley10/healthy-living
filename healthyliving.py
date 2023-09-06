from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4d1b6a8662eff78fccab9ee6ca898d89'

@app.route("/")
def index():
    image_veg = url_for('static', filename='images/Picture of Vegetable (1).png')
    image_about = url_for('static', filename='images/About Picture.png')
    image_sleep = url_for('static', filename='images/Sleeping Picture.png')
    return render_template("index.html", title = index, image_veg = image_veg, image_about = image_about, image_sleep = image_sleep)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title = register, form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'abuse':
            return redirect(url_for('home'))
    return render_template("login.html", title = login, form = form)

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True)