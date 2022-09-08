from flask import Flask, render_template, redirect, session, request
from flask_app import app

@app.route('/login')
def r_login():
    print('rendering login page...')

    return render_template('login.html')

@app.route('/success')
def r_success():
    print('rendering login page...')

    return render_template('success.html')
