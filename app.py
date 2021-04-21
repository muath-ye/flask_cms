# -*- coding:utf8 -*-
from flask import Flask, request, render_template, redirect, url_for, session
import manage_db
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "\xee\x9dA\x81\x19\x17\xdd\x04\xae9\xc1\x1a-\xf2\xf8\xda\x9a\x99u\x90\x96]\xbaT"

def login_required(function):
    @wraps(function) 
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for('home'))
    return wrapper

# Home Page 
@app.route("/") 
def home(): 
    posts = manage_db.get_posts() 
    return render_template('index.html', posts = posts)

# Create Post Page
@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        manage_db.create(title, content)
    return redirect(url_for('home'))

# Single Post Page 
@app.route("/post/<post_id>") 
def post(post_id): 
    post = manage_db.get_post_by_id(post_id) 
    return render_template('post.html', post = post)

# Delete Post 
@app.route("/delete/<post_id>") 
def delete(post_id): 
    manage_db.delete(post_id)
    return redirect(url_for('home'))

# Login Route
@app.route("/login", methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
	
        if username == "admin" and password == "password": 
            session['logged_in'] = True # create new session with name 'logged_in'
            return redirect(url_for('home'))
        else: 
            return redirect(url_for('home'))
	
# Logout Route 
@app.route("/logout") 
def logout(): 
	session.pop('logged_in', None) 
	return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=true)