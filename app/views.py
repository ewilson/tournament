from flask import render_template, redirect, flash, g
import sqlite3
import config
from app import app
from forms import TournForm
from models import Tournament
import tournament_dao

@app.route('/', methods = ['GET','POST'])
def index():
    form = TournForm()
    if form.validate_on_submit():
        tournament = Tournament(0,'',form.tourn_type.data,
                                form.description.data,0)
        tournament_dao.create(tournament)
    tournaments = tournament_dao.find_all()
    return render_template('index.html', 
                           tournaments=tournaments,
                           form=form)

@app.route('/tournament/<id>')
def tournament(id):
    tournament = tournament_dao.find(id)
    return render_template('tournament.html', tournament=tournament)

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

