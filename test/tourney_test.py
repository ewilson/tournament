import pytest

import app.tourney as tourney
from app.models import Standing


class MockStandingsDao(object):
    def __init__(self):
        self.standings = []

    def find(self, id):
        return self.standings


@pytest.fixture
def inject():
    tourney.standings_dao = MockStandingsDao()


def test_sorts_by_percentage(inject):
    standing0 = Standing(win=1, loss=0, tie=0)
    standing1 = Standing(win=8, loss=7, tie=3)
    standing2 = Standing(win=2, loss=9, tie=3)

    tourney.standings_dao.standings = [standing2, standing1, standing0]
    standings = tourney.find_standings(1)

    assert standings[0] == standing0
    assert standings[1] == standing1
    assert standings[2] == standing2


def test_breaks_perc_ties_with_number_wins(inject):
    standing0 = Standing(win=3, loss=2, tie=0)
    standing1 = Standing(win=2, loss=1, tie=2)
    standing2 = Standing(win=1, loss=0, tie=4)

    tourney.standings_dao.standings = [standing2, standing1, standing0]
    standings = tourney.find_standings(1)

    assert standings[0] == standing0
    assert standings[1] == standing1
    assert standings[2] == standing2


def test_breaks_perc_and_win_ties_with_plus_minus(inject):
    standing0 = Standing(win=3, loss=2, tie=0, pf=30, pa=2)
    standing1 = Standing(win=3, loss=2, tie=0, pf=40, pa=22)
    standing2 = Standing(win=3, loss=2, tie=0, pf=50, pa=44)

    tourney.standings_dao.standings = [standing2, standing1, standing0]
    standings = tourney.find_standings(1)

    assert standings[0] == standing0
    assert standings[1] == standing1
    assert standings[2] == standing2
