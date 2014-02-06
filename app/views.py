from flask import render_template, redirect, session, g, request, url_for
import sqlite3, logging
import config
from app import app
from forms import TourneyEntryForm, MatchForm
from models import Player, Standing
import tournament_dao, player_dao, match_dao, tourney

@app.route('/', methods = ['GET'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    model = {'new_tournaments':tournament_dao.find_all_by_status(0),
              'active_tournaments':tournament_dao.find_all_by_status(1),
              'completed_tournaments':tournament_dao.find_all_by_status(2)}
    return render_template('index.html', 
                           model=model)

@app.route('/tournament/<id>', methods = ['GET','POST'])
def tournament(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tournament = tournament_dao.find(id)
    if tournament.status == 2:
        return redirect(url_for('conclude_tournament',id=id))
    form = TourneyEntryForm()
    if not tournament.status and not form.is_submitted():
        players = player_dao.find_all()
        form.enter.choices = [(player.id, player.fname) for player in players]
        return render_template('edit-tournament.html', 
                               tournament=tournament,
                               players=players,
                               form=form)
    if form.is_submitted():
        tourney.setup_round_robin(form.enter.data, id)
    return redirect(url_for('play_tournament', id=id))

@app.route('/play-tournament/<id>', methods = ['GET','POST'])
def play_tournament(id):
    logging.debug('Play tourney: ' + str(id))
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    form = MatchForm()
    if form.validate_on_submit():
        tourney.update_match(form.id.data, form.player1_id.data,
                             form.player2_id.data, form.score1.data,
                             form.score2.data)
    model = {}
    model['tournament'] = tournament_dao.find(id)
    model['schedule'] = match_dao.find_scheduled_by_tournament(id)
    model['completed'] = match_dao.find_completed_by_tournament(id)
    model['standings'] = tourney.find_standings(id)
    return render_template('play-tournament.html', 
                           model=model,
                           form=form)

@app.route('/conclude-tournament/<id>')
def conclude_tournament(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tournament_dao.complete(id)
    model = {}
    model['tournament'] = tournament_dao.find(id)
    model['matches'] = match_dao.find_completed_by_tournament(id)
    model['standings'] = tourney.find_standings(id)
    return render_template('completed-tournament.html',model=model)

@app.route('/tournament/delete/<id>')
def delete_tournament(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tournament_dao.delete(id)
    return redirect('/')

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


def connect_db():
    return sqlite3.connect(config.DATABASE)

