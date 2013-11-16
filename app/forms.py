from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectMultipleField
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
    score1 = TextField('score1', validators=[Required()])
    score2 = TextField('score2', validators=[Required()])
