from flask import render_template, redirect, flash, g
import sqlite3
import config
from app import app
from forms import TournForm
from models import Tournament

@app.route('/', methods = ['GET','POST'])
def index():
    form = TournForm()
    if form.validate_on_submit():
        insert_tournament = """
        insert into tournament (start_date, tourn_type, description, begun)
        values (date('now'), '%s', '%s', 0)
        """ % (form.tourn_type.data, form.description.data)
        print insert_tournament
        g.db.execute(insert_tournament)
        g.db.commit()
    cur = g.db.execute('select id, start_date, tourn_type, description from tournament')
    tournaments = [Tournament(*row) for row in cur.fetchall()]
    return render_template('index.html', 
                           tournaments=tournaments,
                           form=form)

@app.route('/tournament/<id>')
def tournament(id):
    select = "select * from tournament where id = %d" % int(id)
    tournament = Tournament()
    tournament.begun = 0
    return render_template('tournament.html', tournament=tournament)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def connect_db():
    return sqlite3.connect(config.DATABASE)

