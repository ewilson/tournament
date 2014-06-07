import player_dao
import tournament_dao
import match_dao
import standings_dao
import scheduler
from models import Player, Match, Tournament


def setup_round_robin(tournament_id):
    players = player_dao.find_in_tournament(tournament_id)
    pairs = scheduler.round_robin([p.id for p in players])
    for pair in pairs:
        match_dao.create(list(pair), tournament_id)


def undo_match(match_id):
    match = match_dao.find(match_id)
    match_dao.undo(match)
    return match_dao.find(match_id)


def update_match(match_id, player1_id, player2_id, score1, score2):
    player1 = Player(player_id=player1_id)
    player2 = Player(player_id=player2_id)
    match = Match(match_id=match_id, player1=player1, player2=player2,
                  score1=score1, score2=score2)
    match_dao.update(match)
    return match_dao.find(match_id)


def create_tournament(description, tourn_type):
    tournament = Tournament(0, '', description, tourn_type, 0)
    return tournament_dao.create(tournament)


def find_standings(tournament_id):
    standings = standings_dao.find(tournament_id)
    return sorted(standings, key=lambda x: (x.perc, x.win, x.pf - x.pa), reverse=True)

