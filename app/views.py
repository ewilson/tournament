from flask import render_template, redirect, flash, g
import sqlite3

import config

from app import app

@app.route('/')
@app.route('/tournaments')
def index():
    cur = g.db.execute('select start_date, tourn_type, description from tournament')
    tournaments = [Tournament(*row) for row in cur.fetchall()]
    for t in tournaments:
        print t
    return render_template('tournaments.html', tournaments=tournaments)

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

class Tournament:
    def __init__(self, start_date, tourn_type, description):
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
    
    def __repr__(self):
        return '<%s:%s--%s>' % (self.description, self.tourn_type, self.start_date)
