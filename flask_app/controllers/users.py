from flask_app import app
from flask_app.models.user import User
from flask import Flask, render_template, redirect, session, request
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/login')
def r_login():
    print('rendering login page...')

    return render_template('login.html')

@app.route('/success')
def r_success():
    print('rendering login page...')

    return render_template('success.html')

@app.route('/user/register', methods=['POST'])
def f_register_user():

    if not User.validate_user_registration(request.form):
        session['first_name'] = request.form.get('first_name')
        session['last_name'] = request.form.get('last_name')
        session['email'] = request.form.get('email')
        session['logged_in'] = False

        return redirect('/login')

    session.clear()

    pw_hash = bcrypt.generate_password_hash(request.form.get('password'))
    print(pw_hash)

    data = {
        'first_name': request.form.get('first_name'),
        'last_name' : request.form.get('last_name'),
        'email' : request.form.get('email'),
        'password' : pw_hash
    }


    # user_id = User.save(data)

    # session['user_id'] = user_id

    return redirect('/success')


