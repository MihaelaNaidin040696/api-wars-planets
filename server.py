from flask import Flask, render_template, request, url_for, redirect, session
import data_manager
import hash_pass
import re

app = Flask(__name__)
app.secret_key = "_5#y2LF4Q8z\xec]/"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user_credentials = data_manager.get_user(username)
        if not username or not password:
            msg = 'Please, fill in both fields.'
        elif user_credentials:
            msg = 'Username already exists, please choose another one!'
        elif re.match(r"^[A-Za-z\d]$", username):
            msg = 'Username must contain only characters and numbers!'
        else:
            password = hash_pass.hash_password(password)
            data_manager.insert_user_credentials(username, password)
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template(
        'register.html', msg=msg
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and (not request.form['username'] or not request.form['password']):
        msg = 'Please, fill in both fields.'
        return render_template('login.html', msg=msg)
    elif request.method == 'POST' \
            and 'username' in request.form \
            and 'password' in request.form \
            and hash_pass.verify_password(request.form['password'],
                                          data_manager.get_user_pass(request.form['username'])):
        user_credentials = data_manager.get_user(request.form['username'])
        if user_credentials:
            session['loggedin'] = True
            session['id'] = user_credentials['id']
            session['username'] = user_credentials['username']
            return redirect(url_for('index'))
        else:
            msg = 'Wrong username or password.'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
