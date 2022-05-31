from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from converters import converter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urlDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_text = db.Column(db.String(200), index=True)
    short_url_text = db.Column(db.String(20))

# db.create_all()

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    if request.method == "GET":
        return render_template("shorten.html", result="")
    elif request.method == "POST":
        result = shorten()
        db.session.add(URL(url_text=request.form['url'], short_url_text=result))
        db.session.commit()
        return render_template("shorten.html", result=result)

@app.route("/urls")
def show_urls():
    return render_template("urls.html", urls=URL.query.all())

if __name__ == "__main__":
    app.run(debug=True)