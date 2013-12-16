import pytest
import sqlite3

import tourney, match_dao, player_dao, tournament_dao

from models import Standing

class MockStandingsDao(object):
    def __init__(self):
        self.standings = []

    def find(self,id):
        return self.standings

@pytest.fixture
def inject():
    mockStandingsDao = MockStandingsDao()
    tourney.standings_dao = mockStandingsDao

def test_sorts_by_percentage(inject):
    standing0 = Standing(win=1,loss=0,tie=0)
    standing1 = Standing(win=8,loss=7,tie=3)
    standing2 = Standing(win=2,loss=9,tie=3)

    tourney.standings_dao.standings = [standing2,standing1,standing0]
    standings = tourney.find_standings(1)

    assert standings[0] == standing0
    assert standings[1] == standing1
    assert standings[2] == standing2
