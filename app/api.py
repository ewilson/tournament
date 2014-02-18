from flask import request, jsonify
import sqlite3
from app import app
from models import Player
import tournament_dao, player_dao, match_dao, tourney

@app.route('/api/tournament', methods = ['POST'])
def post_tournament():
    try:
        description = request.form['description']
        tourn_type = ''
        tournament = tourney.create_tournament(description, tourn_type)
    except sqlite3.IntegrityError:
        message = "DB ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify(tournament.__dict__)

@app.route('/api/tournament/status/<status>', methods = ['GET'])
def get_new_tournaments(status):
    tourneys = tournament_dao.find_all_by_status(status)
    return jsonify({'tournaments':[t.__dict__ for t in tourneys]})

@app.route('/api/tournament/<id>', methods = ['DELETE'])
def delete_tournament2(id):
    try:
        tournament_dao.delete(id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'success':True, 'id':id})

@app.route('/api/player/<id>', methods = ['DELETE'])
def delete_player(id):
    try:
        player_dao.delete(id)
    except sqlite3.IntegrityError:
        message = "Players in tournaments cannot be deleted."
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'success':True, 'id':id})

@app.route('/api/player', methods = ['GET','POST'])
def api_player():
    if request.method == 'POST':
        return _post_player(request)
    elif request.method == 'GET':
        return _get_player()

def _post_player(request):
    try:
        fname = request.form['fname']
        id = player_dao.create(Player(fname))
    except sqlite3.IntegrityError:
        message = "Player name must be unique."
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'id':id,'fname':fname})

def _get_player():
    players = player_dao.find_all()
    return jsonify({'players':[p.__dict__ for p in players]})