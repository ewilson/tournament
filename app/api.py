from sqlite3 import IntegrityError

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
    except IntegrityError:
        message = "DB ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify(tournament)


@app.route('/api/tournament/status/<status>', methods=['GET'])
def get_new_tournaments(status):
    tourneys = tournament_dao.find_all_by_status(status)
    return jsonify({'tournaments': tourneys})


@app.route('/api/tournament/<tournament_id>', methods=['GET', 'POST', 'DELETE'])
def tournament_http(tournament_id):
    if request.method == 'POST':
        return _post_tourney_entries(tournament_id)
    elif request.method == 'DELETE':
        return _delete_tournament(tournament_id)
    elif request.method == 'GET':
        return _get_tournament(tournament_id)


def _post_tourney_entries(tournament_id):
    try:
        player_ids = request.form['entries']
        tourney.setup_round_robin(player_ids, tournament_id)
    except IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'tournament_id': tournament_id})


def _delete_tournament(tournament_id):
    try:
        tournament_dao.delete(tournament_id)
    except IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'tournament_id': tournament_id})


def _get_tournament(tournament_id):
    try:
        tournament = tournament_dao.find(tournament_id)
    except IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        if tournament:
            return jsonify({'success': True, 'tournament': tournament})
        else:
            return jsonify({'success': False, 'message': 'Not Found'}), 404


@app.route('/api/match/<match_id>', methods=['POST', 'DELETE'])
def match_http(match_id):
    if request.method == 'POST':
        return _post_match(match_id)
    elif request.method == 'DELETE':
        return _delete_match(match_id)


def _post_match(match_id):
    try:
        params = request.form
        match = tourney.update_match(match_id, params['player1_id'],
                                     params['player2_id'],
                                     params['score1'], params['score2'])
    except IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'match': match})


def _delete_match(match_id):
    try:
        match = tourney.undo_match(match_id)
    except IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'match': match})


@app.route('/api/tournament/<tournament_id>/match', methods=['GET'])
def get_matches(tournament_id):
    matches = match_dao.find_by_tournament(tournament_id)
    return jsonify({'matches': matches})


@app.route('/api/tournament/<tournament_id>/standings', methods=['GET'])
def get_standings(tournament_id):
    standings = tourney.find_standings(tournament_id)
    return jsonify({'standings': standings})


@app.route('/api/tournament/<tournament_id>/player', methods=['GET'])
def get_entries(tournament_id):
    players = player_dao.find_in_tournament(tournament_id)
    return jsonify({'players': players}), 200,  {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/api/tournament/<tournament_id>/player/<player_id>',
           methods=['POST', 'DELETE'])
def entry_http(tournament_id, player_id):
    try:
        if request.method == 'POST':
            player = player_dao.enter_tournament(player_id, tournament_id)
        elif request.method == 'DELETE':
            player = player_dao.unenter_tournament(player_id, tournament_id)
    except IntegrityError:
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
    except IntegrityError:
        message = "ERROR!"
        return jsonify({'success': False, 'message': message}), 409
    else:
        return jsonify({'success': True, 'tournament_id': tournament_id})


@app.route('/players/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    try:
        player_dao.delete(player_id)
    except IntegrityError:
        message = "Players in tournaments cannot be deleted."
        return message, 409
    else:
        return jsonify({'success': True, 'tournament_id': player_id})


@app.route('/players', methods=['GET', 'POST'])
def player_http():
    if request.method == 'POST':
        return _post_player()
    elif request.method == 'GET':
        return _get_player(), 200,  {'Content-Type': 'application/json; charset=utf-8'}


def _post_player():
    try:
        fname = request.json['player']['fname']
        player_id = player_dao.create(Player(fname))
    except IntegrityError:
        message = "Player name must be unique."
        return message, 409
    else:
        return jsonify({'player':{'id': player_id, 'fname': fname}})


def _get_player():
    players = player_dao.find_all()
    return jsonify({'players': players})

