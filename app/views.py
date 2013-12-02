from flask import render_template, redirect, flash, g, request, url_for
import sqlite3
import config
from app import app
from forms import TournForm, PlayerForm, TourneyEntryForm, MatchForm
from models import Player, Standing
import tournament_dao, player_dao, tourney

@app.route('/', methods = ['GET','POST'])
def index():
    form = TournForm()
    if form.validate_on_submit():
        tourney.create_tournament(form.description.data,form.tourn_type.data)
    tournaments = tournament_dao.find_all()
    return render_template('index.html', 
                           tournaments=tournaments,
                           form=form)

@app.route('/tournament/<id>', methods = ['GET','POST'])
def tournament(id):
    tournament = tournament_dao.find(id)
    form = TourneyEntryForm()
    if not tournament.begun and not form.is_submitted():
        players = player_dao.find_all()
        form.enter.choices = [(player.id, player.fname) for player in players]
        return render_template('edit-tournament.html', 
                               tournament=tournament,
                               players=player,
                               form=form)
    if form.is_submitted():
        tourney.setup_round_robin(form.enter.data, id)
    return redirect(url_for('play_tournament', id=id))

@app.route('/play-tournament/<id>', methods = ['GET','POST'])
def play_tournament(id):
    form = MatchForm()
    print form
    if request.method == 'POST': #NEED TO CLEAN UP VALIDATION
        tourney.update_match(form.id.data, form.player1_id.data,
                             form.player2_id.data, form.score1.data,
                             form.score2.data)
    model = {}
    model['tournament'] = tournament_dao.find(id)
    model['schedule'] = tourney.find_scheduled_matches(id)
    model['completed'] = tourney.find_completed_matches(id)
    standing_row_1 = Standing('CBJ',60,12,10)
    standing_row_2 = Standing('UNH',12,13,12)
    standing_row_3 = Standing('MSU',0,5,6)
    model['standings'] = [standing_row_1, standing_row_2, standing_row_3]
    return render_template('play-tournament.html', 
                           model=model,
                           form=form)

@app.route('/tournament/undo/<tourn_id>/<match_id>' , methods = ['GET','POST'])
def undo_match(tourn_id, match_id):
    tourney.undo_match(match_id)
    return redirect(url_for('play_tournament',id=tourn_id))

@app.route('/player', methods = ['GET','POST'])
def player():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(form.fname.data)
        player_dao.create(player)
        form.fname.data = ''
    players = player_dao.find_all()
    return render_template('player.html', 
                           players=players,
                           form=form)

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

def connect_db():
    return sqlite3.connect(config.DATABASE)

