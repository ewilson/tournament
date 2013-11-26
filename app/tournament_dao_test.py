import pytest
import sqlite3

import tournament_dao
import config
from models import Tournament

class FakeG(object):
    def __init__(self):
        self.db = sqlite3.connect(config.TEST_DATABASE)
        script = open(config.SCHEMA).read()
        self.db.executescript(script)
        self.db.execute('pragma foreign_keys = ON')

@pytest.fixture
def g():
    fG = FakeG()
    tournament_dao.g = fG

def test_create_and_find_tournament(g):
    t = Tournament(0,description='test-tourn')

    tournament_dao.create(t)
    retreived_t = tournament_dao.find(1)

    assert retreived_t.description == t.description

def test_begin_tournament(g):
    t = Tournament(0,description='test-tourn')
    tournament_dao.create(t)

    tournament_dao.begin(1)
    retreived_t = tournament_dao.find(1)

    assert retreived_t.description == t.description
    assert retreived_t.begun == 1

def test_find_all_tournaments(g):
    t = Tournament(0,description='test-tourn')
    t2 = Tournament(0,description='test-tourn-2')
    tournament_dao.create(t)
    tournament_dao.create(t2)

    tourns = tournament_dao.find_all()

    assert len(tourns) == 2
    assert tourns[0].description == t.description
    assert tourns[1].description == t2.description

