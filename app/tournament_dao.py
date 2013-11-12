from flask import g
import sqlite3

from models import Tournament

def find_all():
    select = '''select id, start_date, description, tourn_type, begun
                from tournament'''
    cur = g.db.execute(select)
    return [Tournament(*row) for row in cur.fetchall()]

def find(id):
    select = "select * from tournament where id = ?"
    cur = g.db.execute(select, [id])
    return Tournament(*cur.fetchone())

def create(tourn):
    insert_tournament = """
        insert into tournament (start_date, tourn_type, description, begun)
        values (date('now'), ?, ?, 0)"""
    print insert_tournament
    g.db.execute(insert_tournament, [tourn.tourn_type, tourn.description])
    g.db.commit()

# Not currently used
def update(tourn):
    update = """
        update tournament set start_date = ?,
                              tourn_type = ?,
                              description = ?,
                              begun = ? where id = ?"""
    data = [tourn.start_date, tourn.tourn_type, tourn.description, 
            tourn.begun, tourn.id]
    g.db.execute(update, data)
    g.db.commit()

def begin(tourn_id):
    update = "update tournament set begun = ? where id = ?"
    data = [1, tourn_id]
    g.db.execute(update, data)
    g.db.commit()

