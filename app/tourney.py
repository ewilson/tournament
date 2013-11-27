import player_dao, tournament_dao, match_dao, scheduler
from models import Player, Match

def setup_round_robin(player_ids, tournament_id):
    for player_id in player_ids:
        player_dao.enter_tournament(player_id, tournament_id)
    tournament_dao.begin(tournament_id)
    pairs = scheduler.round_robin(player_ids)
    for pair in pairs:
        match_dao.create(list(pair), tournament_id)

def find_scheduled_matches(tournament_id):
    matches = match_dao.find_scheduled_by_tournament(tournament_id)
    return matches

def find_completed_matches(tournament_id):
    matches = match_dao.find_completed_by_tournament(tournament_id)
    return matches

def undo_match(match_id):
    match = match_dao.find(match_id)
    match_dao.undo(match)
