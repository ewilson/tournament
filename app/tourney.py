import player_dao, tournament_dao, match_dao, standings_dao, scheduler
from models import Player, Match, Tournament

def setup_round_robin(player_ids, tournament_id):
    for player_id in player_ids:
        player_dao.enter_tournament(player_id, tournament_id)
    tournament_dao.begin(tournament_id)
    pairs = scheduler.round_robin(player_ids)
    for pair in pairs:
        match_dao.create(list(pair), tournament_id)

def undo_match(match_id):
    match = match_dao.find(match_id)
    match_dao.undo(match)

def update_match(match_id, player1_id, player2_id, score1, score2):
    player1 = Player(id=player1_id)
    player2 = Player(id=player2_id)
    match = Match(id=match_id, player1=player1, player2=player2,
                  score1=score1, score2=score2)
    match_dao.update(match)

def create_tournament(description,tourn_type):
    tournament = Tournament(0,'',description,tourn_type,0)
    tournament_dao.create(tournament)

def find_standings(tournament_id):
    standings = standings_dao.find(tournament_id)
    return sorted(standings, key=lambda x: (x.perc,x.win,x.pf-x.pa), reverse=True)

