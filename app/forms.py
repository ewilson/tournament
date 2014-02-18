from flask.ext.wtf import Form
from wtforms import TextField, HiddenField
from wtforms.validators import Required

class MatchForm(Form):
    id = HiddenField('id', validators=[Required()])
    score1 = TextField('score1', validators=[Required()])
    score2 = TextField('score2', validators=[Required()])
    player1_id = HiddenField('player1_id', validators=[Required()])
    player2_id = HiddenField('player2_id', validators=[Required()])
    
