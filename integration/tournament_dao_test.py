import pytest

import app.tournament_dao as tournament_dao
from app.models import Tournament

from test_utils import FakeG


@pytest.fixture
def g():
    tournament_dao.g = FakeG()


def test_create_tournament(g):
    t = Tournament(0, description='test-tourn')

    created_t = tournament_dao.create(t)

    assert t.description == created_t.description
    assert created_t.start_date is not None
    assert created_t.tournament_id == 1


def test_create_and_find_tournament(g):
    t = Tournament(0, description='test-tourn')

    tournament_dao.create(t)
    retrieved_t = tournament_dao.find(1)

    assert retrieved_t.description == t.description


def test_create_and_delete_tournament(g):
    t = Tournament(0, description='test-tourn')
    tournament_dao.create(t)
    retrieved_t = tournament_dao.find(1)
    id = retrieved_t.tournament_id

    tournament_dao.delete(id)
    all_tournaments = tournament_dao.find_all()

    assert all_tournaments == []


def test_begin_tournament(g):
    t = Tournament(0, description='test-tourn')
    t = tournament_dao.create(t)

    tournament_dao.update_status(t.tournament_id, 1)
    retrieved_t = tournament_dao.find_all_by_status(1)

    assert retrieved_t[0].description == t.description
    assert retrieved_t[0].status == 1


def test_find_all_new_tournaments(g):
    t = Tournament(0, description='test-tourn')
    t2 = Tournament(0, description='test-tourn-2')
    tournament_dao.create(t)
    tournament_dao.create(t2)

    tourns = tournament_dao.find_all_by_status(0)

    assert len(tourns) == 2
    assert tourns[0].description == t.description
    assert tourns[1].description == t2.description


def test_complete_tournament(g):
    t = Tournament(0, description='test-tourn')
    t = tournament_dao.create(t)

    tournament_dao.update_status(t.tournament_id, 2)
    retrieved_t = tournament_dao.find_all_by_status(2)

    assert retrieved_t[0].description == t.description
    assert retrieved_t[0].status == 2
