import player_dao, tournament_dao, match_dao, scheduler
from models import Player, Match

def setup_round_robin(player_ids, tournament_id):
    for player_id in player_ids:
        player_dao.enter_tournament(player_id, tournament_id)
    tournament_dao.begin(tournament_id)
    pairs = scheduler.round_robin([player_dao.find(id) for id in player_ids])
    for pair in pairs:
        match = Match(*tuple(pair))
        match_dao.create(match, tournament_id)

def find_matches(tournament_id):
    matches = match_dao.find_scheduled_by_tournament(tournament_id)
    return matches
