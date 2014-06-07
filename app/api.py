import json
import sqlite3

from flask import request

from app import app
from models import Player
import tournament_dao
import player_dao
import match_dao
import tourney
from deepJson import jsonify


@app.route('/api/tournament', methods=['POST'])
def post_tournament():
    try:
        description = request.form['description']
        tourn_type = ''
        tournament = tourney.create_tournament(description, tourn_type)
    except sqlite3.IntegrityError:
        message = "DB ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify(tournament)


@app.route('/api/tournament/status/<status>', methods=['GET'])
def get_new_tournaments(status):
    tourneys = tournament_dao.find_all_by_status(status)
    return jsonify({'tournaments': tourneys})


@app.route('/api/tournament/<id>', methods=['GET', 'POST', 'DELETE'])
def tournament2(id):
    if request.method == 'POST':
        return _post_tourney_entries(id, request)
    elif request.method == 'DELETE':
        return _delete_tournament(id)
    elif request.method == 'GET':
        return _get_tournament(id)


def _post_tourney_entries(id, request):
    try:
        player_ids = request.form['entries']
        tourney.setup_round_robin(player_ids, id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'id': id})


def _delete_tournament(id):
    try:
        tournament_dao.delete(id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'id': id})


def _get_tournament(id):
    try:
        tournament = tournament_dao.find(id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        if tournament:
            return jsonify({'success': True, 'tournament': tournament})
        else:
            return jsonify({'success': False, 'message': 'Not Found'}), 404


@app.route('/api/match/<id>', methods=['POST', 'DELETE'])
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
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'match': match})


def _delete_match(id):
    try:
        match = tourney.undo_match(id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'match': match})


@app.route('/api/tournament/<id>/match', methods=['GET'])
def get_matches(id):
    matches = match_dao.find_by_tournament(id)
    return jsonify({'matches': matches})


@app.route('/api/tournament/<id>/standings', methods=['GET'])
def get_standings(id):
    standings = tourney.find_standings(id)
    return jsonify({'standings': standings})


@app.route('/api/tournament/<id>/player', methods=['GET'])
def get_entries(id):
    players = player_dao.find_in_tournament(id)
    return jsonify({'players': players})


@app.route('/api/tournament/<tournament_id>/player/<player_id>',
           methods=['POST', 'DELETE'])
def add_or_delete_entry(tournament_id, player_id):
    try:
        if request.method == 'POST':
            player = player_dao.enter_tournament(player_id, tournament_id)
        elif request.method == 'DELETE':
            player = player_dao.unenter_tournament(player_id, tournament_id)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'player': player})


@app.route('/api/tournament/<tournament_id>/status/<status>',
           methods=['POST'])
def update_status(tournament_id, status):
    try:
        if status == '1':
            tourney.setup_round_robin(tournament_id)
        tournament_dao.update_status(tournament_id, status)
    except sqlite3.IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'id': tournament_id})


@app.route('/api/player/<id>', methods=['DELETE'])
def delete_player(id):
    try:
        player_dao.delete(id)
    except sqlite3.IntegrityError:
        message = "Players in tournaments cannot be deleted."
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'id': id})


@app.route('/api/player', methods=['GET', 'POST'])
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
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'id': id, 'fname': fname})


def _get_player():
    players = player_dao.find_all()
    return jsonify({'players': players})

