from flask import g
import sqlite3

from models import Player

def find_all():
    select = '''select id, fname from player'''
    cur = g.db.execute(select)
    return [Player(*row) for row in cur.fetchall()]

def find(id):
    select = "select id, fname from player where id = %d" % int(id)
    cur = g.db.execute(select)
    return Player(*cur.fetchone())

def create(player):
    insert_player = """
        insert into player (fname) values ('%s')
        """ % player.fname
    print insert_player
    g.db.execute(insert_player)
    g.db.commit()
