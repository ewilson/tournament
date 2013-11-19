import pytest
import sqlite3

import match_dao, player_dao
import config
from models import Player,Match

class FakeG(object):
    def __init__(self):
        self.db = sqlite3.connect(config.TEST_DATABASE)
        script = open(config.SCHEMA).read()
        self.db.executescript(script)

@pytest.fixture
def g():
    fG = FakeG()
    match_dao.g = fG
    player_dao.g = fG

def test_create_and_find_match(g):
    p = Player("test player")
    p2 = Player("test player 2")
    player_dao.create(p)
    p.id = 1
    player_dao.create(p2)
    p2.id = 2
    tournament_id = 3

    match_dao.create([p.id, p2.id], tournament_id)
    retrieved_match = match_dao.find(1)

    assert retrieved_match.id == 1
    assert retrieved_match.player1.fname == p.fname
    assert retrieved_match.player2.fname == p2.fname

#def test_create_and_find_scheduled_by_tournament(g):
    
