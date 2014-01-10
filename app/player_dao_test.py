import pytest
import sqlite3

import player_dao, tournament_dao
import config
from models import Player, Tournament

class FakeG(object):
    def __init__(self):
        self.db = sqlite3.connect(config.TEST_DATABASE)
        script = open(config.SCHEMA).read()
        self.db.executescript(script)
        self.db.execute('pragma foreign_keys = ON')

@pytest.fixture
def g():
    fG = FakeG()
    player_dao.g = fG
    tournament_dao.g = fG

def test_create_and_find_player(g):
    p = Player("test player")

    player_dao.create(p)
    p2 = player_dao.find(1)
    
    assert p.fname == p2.fname
    assert p2.id == 1

def test_find_all(g):
    players = [Player("TEST" + str(n)) for n in range(5)]
    for player in players:
        player_dao.create(player)

    players2 = player_dao.find_all()
    assert 5 == len(players2)
    assert players2[3].id == 4
    assert players2[3].fname == 'TEST3'

def test_find_in_tournament(g):
    p = Player("Test1")
    p2 = Player("Test2")
    p3 = Player("Test3")
    player_dao.create(p)
    player_dao.create(p2)
    player_dao.create(p3)
    t = Tournament(description="Test Tourn")
    tournament_dao.create(t)

    player_dao.enter_tournament(1,1)
    player_dao.enter_tournament(3,1)
    players = player_dao.find_in_tournament(1)

    assert players[0].fname == p.fname
    assert players[1].fname == p3.fname
    assert len(players) == 2

def test_delete_player(g):
    p = Player("Test1")
    p2 = Player("Test2")
    p3 = Player("Test3")
    player_dao.create(p)
    player_dao.create(p2)
    player_dao.create(p3)

    player_dao.delete(1)
    players = player_dao.find_all()

    assert len(players) == 2
    assert players[0].id == 2
    assert players[1].id == 3

def test_delete_player_in_tournament_fails(g):
    p = Player("Test1")
    player_dao.create(p)
    t = Tournament(description="Test Tourn")
    tournament_dao.create(t)
    player_dao.enter_tournament(1,1)

    try:
        player_dao.delete(1)
    except sqlite3.IntegrityError:
        player_dao.g.db.commit()
        print "Can't delete"
    else:
        assert False

