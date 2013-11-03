from flask import g
import sqlite3

from models import Tournament

def find_all():
    select = '''select id, start_date, tourn_type, description, begun
                from tournament'''
    cur = g.db.execute(select)
    return [Tournament(*row) for row in cur.fetchall()]

def find(id):
    select = "select * from tournament where id = %d" % int(id)
    cur = g.db.execute(select)
    return Tournament(*cur.fetchone())

def create(tournament):
    insert_tournament = """
        insert into tournament (start_date, tourn_type, description, begun)
        values (date('now'), '%s', '%s', 0)
        """ % (tournament.tourn_type, tournament.description)
    print insert_tournament
    g.db.execute(insert_tournament)
    g.db.commit()

def update(tournament):
    update = """
        update tournament set start_date = '%s',
                              tourn_type = '%s',
                              description = '%s',
                              begun = '%d' where id = '%d'
    """ % (tournament.start_date, tournament.tourn_type, tournament.description, tournament.begun, tournament.id)
    print update
    g.db.execute(update)
    g.db.commit()

