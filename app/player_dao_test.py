import sqlite3

import player_dao
import config
from models import Player

class FakeG(object):
    def __init__(self):
        self.db = sqlite3.connect(config.TEST_DATABASE)

player_dao.g = FakeG()

def test_foo():
    p = Player(1,"test player")
    player_dao.create(p)
