import player_dao, tournament_dao, scheduler
from models import Player, Match

def setup_round_robin(player_ids, tournament_id):
    for player_id in player_ids:
        player_dao.enter_tournament(player_id, tournament_id)
    tournament_dao.begin(tournament_id)
    pairs = scheduler.round_robin(player_ids)
    tournament_dao.add_pairs(pairs,tournament_id)

def find_matches(tournament_id):
    p1 = Player('Albert')
    p2 = Player('Bernard')
    p3 = Player('Charles')
    p4 = Player('DeMarcus')
    c1 = '''    cm1 = Match(p1,p2)
    cm1.score1 = 4
    cm1.score2 = 3
    cm2 = Match(p1,p3)
    cm1.score1 = 44
    cm2.score2 = 3
    completed = [cm1, cm2]'''
    sm1 = Match(p2,p4)
    sm2 = Match(p3,p4)
    schedule = [sm1,sm2]
    c2 = '''    class Foo:
        def __init__(self):
            self.description = 'fake'
            self.begun = 1
    
    return render_template('play-tournament.html',
                           tournament = Foo(),
                           completed = completed,
                           schedule = schedule)
'''
    print "IN PANTS"
    print schedule
    return schedule
