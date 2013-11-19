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
    m = Match(*players, id=id)
    return m

def find_scheduled_by_tournament(tournament_id):
    select = "select id from match where tournament_id = ?"
    cur = g.db.execute(select, [tournament_id])
    matches = [find(row[0]) for row in cur.fetchall()]
    return matches

def create(player_ids, tournament_id):
    insert_match = "insert into match (tournament_id) values (?)"
    insert_entry = """
    insert into attempt (player_id, match_id)
    values (?,?)
    """
    g.db.execute("BEGIN TRANSACTION")
    g.db.execute(insert_match,[tournament_id])
    cursor = g.db.execute('SELECT max(id) FROM match')
    match_id = cursor.fetchone()[0]
    for player_id in player_ids:
        g.db.execute(insert_entry,[player_id, match_id])
    g.db.commit()

def update(id, player_scores):
    update = """
    update attempt set score = ? 
    where player_id = ? and match_id = ?"""
    g.db.execute("BEGIN TRANSACTION")
    for score in player_scores:
        g.db.execute(update,[score['score'],score['player_id'],id])
    g.db.commit()

