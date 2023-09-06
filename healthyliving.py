from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    image_veg = url_for('static', filename='images/Picture of Vegetable (1).png')
    image_about = url_for('static', filename='images/About Picture.png')
    image_sleep = url_for('static', filename='images/Sleeping Picture.png')
    return render_template("index.html", image_veg = image_veg, image_about = image_about, image_sleep = image_sleep)

@app.route("/register")
def register():
    return render_template("forms.html")

if __name__ == '__main__':
    app.run(debug = True)