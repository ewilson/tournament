import sqlite3

from flask import render_template, redirect, session, g, request, url_for

import config
from app import app
import tournament_dao
import tourney

@app.route('/')
def i2():
    return render_template('index2.html')

@app.route('/old', methods=['GET'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/tournament/<tournament_id>', methods=['GET'])
def get_tournament(tournament_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tournament = tournament_dao.find(tournament_id)
    if not tournament.status:
        return render_template('edit-tournament.html',
                               tournament=tournament)
    return redirect(url_for('play_tournament', tournament_id=tournament_id))


@app.route('/play-tournament/<tournament_id>')
def play_tournament(tournament_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('play-tournament.html',
                           tournament_id=tournament_id)


@app.route('/tournament/undo/<tourn_id>/<match_id>', methods=['GET', 'POST'])
def undo_match(tourn_id, match_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tourney.undo_match(match_id)
    return redirect(url_for('play_tournament', tournament_id=tourn_id))


@app.route('/player')
def player():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('player.html')


@app.route('/login', methods=['GET', 'POST'])
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
