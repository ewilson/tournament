from flask import g
import sqlite3

from models import Match, Player

def find(id):
    select = """
    select p.fname, p.id from player p, attempt a
    where p.id = a.player_id and a.match_id = ?
    """
    cur = g.db.execute(select, [id])
    players = [Player(*row) for row in cur.fetchall()]
    m = Match(*players)
    m.id = id
    return m

def create(match, tournament_id):
    insert_match = "insert into match (tournament_id) values (?)"
    insert_entry = """
    insert into attempt (player_id, match_id)
    values (?,?)
    """
    g.db.execute("BEGIN TRANSACTION")
    g.db.execute(insert_match,[tournament_id])
    cursor = g.db.execute('SELECT max(id) FROM match')
    match_id = cursor.fetchone()[0]
    g.db.execute(insert_entry,[match.player1.id, match_id])
    g.db.execute(insert_entry,[match.player2.id, match_id])
    g.db.commit()

