from flask import render_template, redirect, flash, g
import sqlite3
import config
from app import app
from forms import TournForm, PlayerForm, TourneyEntry
from models import Tournament, Player
import tournament_dao, player_dao

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

@app.route('/tournament/<id>', methods = ['GET','POST'])
def tournament(id):
    tournament = tournament_dao.find(id)
    entries = player_dao.find_in_tournament(id) 
    other_players = player_dao.find_not_in_tournament(id)
    form = TourneyEntry()
    form.enter.choices = [(player.id, player.fname) for player in entries]
    if form.is_submitted():
        print "Data",form.enter.data
    return render_template('tournament.html', 
                           tournament=tournament,
                           entries=entries,
                           other_players=other_players,
                           form=form)

@app.route('/player', methods = ['GET','POST'])
def player():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(0,form.fname.data)
        player_dao.create(player)
        form.fname.data = ''
    players = player_dao.find_all()
    return render_template('player.html', 
                           players=players,
                           form=form)

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

