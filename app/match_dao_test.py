import pytest
import sqlite3

import match_dao, player_dao, tournament_dao
import config
from models import Player, Match, Tournament

class FakeG(object):
    def __init__(self):
        self.db = sqlite3.connect(config.TEST_DATABASE)
        script = open(config.SCHEMA).read()
        self.db.executescript(script)
        self.db.execute('pragma foreign_keys = ON')

@pytest.fixture
def g():
    fG = FakeG()
    match_dao.g = fG
    player_dao.g = fG
    tournament_dao.g = fG

def test_create_and_find_match(g):
    p = Player("test player")
    p2 = Player("test player 2")
    player_dao.create(p)
    p.id = 1
    player_dao.create(p2)
    p2.id = 2
    t = Tournament(0,'','T1','type',0)
    tournament_dao.create(t)
    t.id = 1

    match_dao.create([p.id, p2.id], t.id)
    retrieved_match = match_dao.find(1)

    assert retrieved_match.id == 1
    assert retrieved_match.player1.fname == p.fname
    assert retrieved_match.player2.fname == p2.fname


def test_create_and_find_scheduled_by_tournament(g):
    p = Player("test player")
    p2 = Player("test player 2")
    p3 = Player("test player 3")
    player_dao.create(p)
    p.id = 1
    player_dao.create(p2)
    p2.id = 2
    player_dao.create(p3)
    p3.id = 3
    t = Tournament(0,'','T1','type',0)
    tournament_dao.create(t)
    t.id = 1
    t2 = Tournament(0,'','T2','type',0)
    tournament_dao.create(t2)
    t2.id = 2

    match_dao.create([p.id,p2.id], t.id)
    match_dao.create([p.id,p2.id], t2.id)
    match_dao.create([p.id,p3.id], t2.id)
    retrieved_matches = match_dao.find_scheduled_by_tournament(t2.id)

    assert len(retrieved_matches) == 2
    assert retrieved_matches[0].player2.fname == p2.fname
    assert retrieved_matches[1].id == 3

def test_update_match_with_result(g):
    p = Player("test player")
    p2 = Player("test player 2")
    player_dao.create(p)
    p.id = 1
    player_dao.create(p2)
    p2.id = 2
    t = Tournament(0,'','T1','type',0)
    tournament_dao.create(t)
    t.id = 1
    match_dao.create([p.id, p2.id], t.id)
    match_id = 1
    match = Match(player1=p,player2=p2,id=match_id)
    match.score1 = 19
    match.score2 = 21

    match_dao.update(match)
    retrieved_match = match_dao.find(match_id)
    scheduled_matches = match_dao.find_scheduled_by_tournament(t.id)
    completed_matches = match_dao.find_completed_by_tournament(t.id)

    assert retrieved_match.score1 == 19
    assert retrieved_match.score2 == 21
    assert retrieved_match.player1.fname == p.fname
    assert retrieved_match.player2.fname == p2.fname
    assert retrieved_match.player1.id == p.id
    assert retrieved_match.player2.id == p2.id
    assert len(scheduled_matches) == 0
    assert len(completed_matches) == 1

def test_undo_match(g):
    p = Player("test player")
    p2 = Player("test player 2")
    player_dao.create(p)
    p.id = 1
    player_dao.create(p2)
    p2.id = 2
    t = Tournament(0,'','T1','type',0)
    tournament_dao.create(t)
    t.id = 1
    match_dao.create([p.id, p2.id], t.id)
    match_id = 1
    match = Match(player1=p,player2=p2,id=match_id)
    match.score1 = 19
    match.score2 = 21
    match_dao.update(match)

    match_dao.undo(match)
    retrieved_match = match_dao.find(match_id)
    scheduled_matches = match_dao.find_scheduled_by_tournament(t.id)
    completed_matches = match_dao.find_completed_by_tournament(t.id)

    assert retrieved_match.score1 == 0
    assert retrieved_match.score2 == 0
    assert retrieved_match.player1.fname == p.fname
    assert retrieved_match.player2.fname == p2.fname
    assert retrieved_match.player1.id == p.id
    assert retrieved_match.player2.id == p2.id
    assert len(scheduled_matches) == 1
    assert len(completed_matches) == 0

