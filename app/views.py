import sqlite3, logging

from flask import render_template, redirect, session, g, request, url_for

import config
from app import app
from models import Player, Standing
import tournament_dao, player_dao, match_dao, tourney

@app.route('/', methods = ['GET'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/tournament/<id>', methods = ['GET'])
def tournament(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tournament = tournament_dao.find(id)
    if not tournament.status:
        return render_template('edit-tournament.html', 
                               tournament=tournament)
    return redirect(url_for('play_tournament', id=id))

@app.route('/play-tournament/<id>')
def play_tournament(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('play-tournament.html', 
                           tournament_id=id)

@app.route('/tournament/undo/<tourn_id>/<match_id>' , methods = ['GET','POST'])
def undo_match(tourn_id, match_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tourney.undo_match(match_id)
    return redirect(url_for('play_tournament',id=tourn_id))

@app.route('/player')
def player():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('player.html')

@app.route('/login' , methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == config.PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = 'Invalid Password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.db = connect_db()
    g.db.execute('pragma foreign_keys = ON')
    g.db.commit()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def connect_db():
    return sqlite3.connect(config.DATABASE)

