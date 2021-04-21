# -*- coding:utf8 -*-
from flask import Flask, request, render_template
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template('index.html', page = u"الصّفحة الرّئيسيّة")

# Hello Page
@app.route("/hello")
def hello():
    return render_template('index.html', page = u"صفحة التّرحيب")

# Posts Page
@app.route("/posts")
def posts():
    posts = [ u"مُحتوى المقال الأول", u"مُحتوى المقال الثاني", u"مُحتوى المقال الثالث", u"مُحتوى المقال الرابع" ]
    return render_template('index.html', posts = posts, page = u"صفحة المقالات")

@app.route("/say_hello/<name>")
def say_hello(name):
    return u"Hello {}".format(name)

@app.route("/first_last")
def first_last():
    first_name = request.args.get('first_name').capitalize()
    last_name = request.args.get('last_name').upper()
    return u"<h3>First Name: {} <br>Last Name: {}</h3>".format(first_name, last_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1200)