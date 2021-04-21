# -*- coding:utf8 -*-
from flask import Flask, request, render_template, redirect, url_for, session, flash
import manage_db
from functools import wraps
from datetime import timedelta

app = Flask(__name__)
app.config.from_object('config')

def login_required(function):
    @wraps(function) 
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            flash(u'سجّل دخولك أولا لإجراء هذه العمليّة')
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
        flash(u'أضيف المقال بنجاح!')
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
    flash(u'حُذف المقال بنجاح!')
    return redirect(url_for('home'))

# Login Route
@app.route("/login", methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
	
        if username == app.config['USERNAME'] and password == app.config['PASSWORD']: 
            # create new session with name 'logged_in'
            session['logged_in'] = True
            # to add 'remember me' option
            session.permanent = True
            # Make session last for only 30 min, here other options:
            # timedelta(days=0) # الأيام
            # timedelta(seconds=0) # الثواني
            # timedelta(minutes=0) # الدّقائق
            # timedelta(hours=0) # السّاعات
            # timedelta(weeks=0) # الأسابيع
            app.permanent_session_lifetime = timedelta(minutes=30)
            flash(u'سُجّل دخولك بنجاح')
            return redirect(url_for('home'))
        else: 
            return redirect(url_for('home'))
	
# Logout Route 
@app.route("/logout") 
def logout(): 
	session.pop('logged_in', None)
    flash(u'سُجّل خروجك بنجاح!')
	return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=true)