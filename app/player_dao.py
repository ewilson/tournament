from flask import g
import sqlite3, logging

from models import Player

def find_all():
    select = '''select fname, id from player'''
    cur = g.db.execute(select)
    return [Player(*row) for row in cur.fetchall()]

def find(id):
    select = "select fname, id from player where id = ?"
    cur = g.db.execute(select,[id])
    return Player(*cur.fetchone())

def create(player):
    insert_player = "insert into player (fname) values (?)"
    logging.debug(insert_player)
    g.db.execute(insert_player,[player.fname])
    cur = g.db.execute('select last_insert_rowid() from player')
    g.db.commit()
    return cur.fetchone()[0]

def delete(id):
    return True

def enter_tournament(player_id, tournament_id):
    insert_entry = "insert into entry (player_id, tournament_id) values (?, ?)"
    logging.debug(insert_entry)
    g.db.execute(insert_entry,[player_id,tournament_id])
    g.db.commit()

# Not currently used, but tested and useful
def find_in_tournament(tournament_id):
    select = '''
    select p.fname, p.id from player p, entry e
    where p.id = e.player_id and e.tournament_id = ? '''
    cur = g.db.execute(select, [tournament_id])
    return [Player(*row) for row in cur.fetchall()]

