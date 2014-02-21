from flask import request, jsonify
import json
import sqlite3
from app import app
from models import Player, ComplexEncoder
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

@app.route('/api/tournament/<id>', methods = ['POST','DELETE'])
def tournament2(id):
    if request.method == 'POST':
        return _post_tourney_entries(id, request)
    elif request.method == 'DELETE':
        return _delete_tournament(id)

def _post_tourney_entries(id, request):
    try:
        player_ids = request.form['entries']
        tourney.setup_round_robin(player_ids, id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'success':True, 'id':id})

def _delete_tournament(id):
    try:
        tournament_dao.delete(id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'success':True, 'id':id})

@app.route('/api/match/<id>', methods = ['POST','DELETE'])
def match(id):
    if request.method == 'POST':
        return _post_match(id, request)
    elif request.method == 'DELETE':
        return _delete_match(id)

def _post_match(id, request):
    try:
        params = request.form
        match = tourney.update_match(id, params['player1_id'], 
                                     params['player2_id'],
                                     params['score1'], params['score2'])
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return json.dumps(match.reprJSON(), cls=ComplexEncoder)

def _delete_match(id):
    try:
        match = tourney.undo_match(id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return json.dumps(match.reprJSON(), cls=ComplexEncoder)

@app.route('/api/tournament/<id>/player', methods = ['GET'])
def get_entries(id):
    players = player_dao.find_in_tournament(id)
    return jsonify({'players':[p.__dict__ for p in players]})

@app.route('/api/tournament/<tournament_id>/player/<player_id>', 
           methods = ['POST','DELETE'])
def add_or_delete_entry(tournament_id, player_id):
    try:
        if request.method == 'POST':
            player = player_dao.enter_tournament(player_id, tournament_id)
        elif request.method == 'DELETE':
            player = player_dao.unenter_tournament(player_id, tournament_id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'success':True, 'player':player.__dict__})

@app.route('/api/tournament/<tournament_id>/status/<status>', 
           methods = ['POST'])
def update_status(tournament_id, status):
    try:
        tournament_dao.update_status(tournament_id, status)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success':False, 'message':message}),409
    else:
        return jsonify({'success':True, 'id':tournament_id})

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

