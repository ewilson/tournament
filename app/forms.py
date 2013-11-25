from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectMultipleField, HiddenField
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import Required

class TournForm(Form):
    description = TextField('description', validators=[Required()])
    tourn_type = TextField('tourn_type')

class PlayerForm(Form):
    fname = TextField('fname', validators=[Required()])

class TourneyEntryForm(Form):
    enter = SelectMultipleField(
        'Enter',
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=True))

class MatchForm(Form):
    id = HiddenField('id', validators=[Required()])
    score1 = TextField('score1', validators=[Required()])
    score2 = TextField('score2', validators=[Required()])
    player1_id = HiddenField('player1_id', validators=[Required()])
    player2_id = HiddenField('player2_id', validators=[Required()])
    
