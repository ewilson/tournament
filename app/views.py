import sqlite3

from flask import render_template, redirect, session, g, request, url_for

import config
from app import app
import tournament_dao
import tourney


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/mock-tournament/id/edit')
def mock_edit_tournament():
    return render_template('tournaments.id.edit.html')

@app.route('/mock-tournament/id/view')
def mock_view_tournament():
    return render_template('tournaments.id.view.html')

@app.route('/mock-tournament/id/standings/view')
def mock_view_standings_tournament():
    return render_template('tournaments.id.standings.view.html')

@app.route('/mock-tournament/id/view/match-id/update')
def mock_update_match():
    return render_template('tournaments.id.view.match-id.update.html')

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
