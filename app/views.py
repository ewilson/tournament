from flask import render_template, redirect, flash, g
import sqlite3

import config

from app import app

@app.route('/')
@app.route('/tournaments')
def index():
    return render_template('tournaments.html')

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def connect_db():
    return sqlite3.connect(config.DATABASE)
