from flask import g
import sqlite3, logging

from models import Tournament

def find_all():
    select = '''select id, start_date, description, tourn_type, status
                from tournament'''

    cur = g.db.execute(select)
    return [Tournament(*row) for row in cur.fetchall()]

def find_all_by_status(status):
    select = '''select id, start_date, description, tourn_type, status
                from tournament
                where status = ?'''
    cur = g.db.execute(select,[status])
    return [Tournament(*row) for row in cur.fetchall()]

def find(id):
    select = "select * from tournament where id = ?"
    cur = g.db.execute(select, [id])
    return Tournament(*cur.fetchone())

def create(tourn):
    insert_tournament = """
        insert into tournament (start_date, tourn_type, description, status)
        values (date('now'), ?, ?, 0)"""
    logging.debug(insert_tournament)
    g.db.execute(insert_tournament, [tourn.tourn_type, tourn.description])
    cur = g.db.execute('select last_insert_rowid() from tournament')
    id = cur.fetchone()[0]
    g.db.commit()
    return find(id)

def delete(id):
    delete = "delete from tournament where id = ?"
    g.db.execute(delete, [id])
    g.db.commit()

# Not currently used
def update(tourn):
    update = """
        update tournament set start_date = ?,
                              tourn_type = ?,
                              description = ?,
                              status = ? where id = ?"""
    data = [tourn.start_date, tourn.tourn_type, tourn.description, 
            tourn.status, tourn.id]
    g.db.execute(update, data)
    g.db.commit()

def update_status(tourn_id, status):
    update = "update tournament set status = ? where id = ?"
    data = [status, tourn_id]
    g.db.execute(update, data)
    g.db.commit()

