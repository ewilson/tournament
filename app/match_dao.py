from datetime import datetime

from flask import g

from models import Match, Player


def find(id):
    select = """
    select p.fname, p.id, a.score, m.entered_time 
    from player p, attempt a, match m
    where p.id = a.player_id 
    and a.match_id = ?
    and m.id = a.match_id
    """
    m = Match(match_id=id)
    cur = g.db.execute(select, [id])
    attempts = cur.fetchall()
    player1 = Player(*attempts[0][:2])
    m.player1 = player1
    m.score1 = attempts[0][2]
    player2 = Player(*attempts[1][:2])
    m.player2 = player2
    m.score2 = attempts[1][2]
    m.entered_time = attempts[0][-1]
    return m


def find_by_tournament(tournament_id):
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
    g.db.execute(insert_match, [tournament_id])
    cursor = g.db.execute('SELECT max(id) FROM match')
    match_id = cursor.fetchone()[0]
    for player_id in player_ids:
        g.db.execute(insert_entry, [player_id, match_id])
    g.db.commit()


def update(match):
    update = """
    update attempt set score = ?, opp_score = ?
    where player_id = ? and match_id = ?"""
    g.db.execute("BEGIN TRANSACTION")
    g.db.execute(update, [match.score1, match.score2, match.player1.player_id, match.match_id])
    g.db.execute(update, [match.score2, match.score1, match.player2.player_id, match.match_id])
    g.db.execute('update match set entered_time = ? where id = ?',
                 [datetime.now(), match.match_id])
    g.db.commit()


def undo(match):
    update = """
    update attempt set score = 0, opp_score = 0
    where player_id = ? and match_id = ?
    """
    g.db.execute("BEGIN TRANSACTION")
    g.db.execute(update, [match.player1.player_id, match.match_id])
    g.db.execute(update, [match.player2.player_id, match.match_id])
    g.db.execute('update match set entered_time = null where id = ?',
                 [match.match_id])
    g.db.commit()

