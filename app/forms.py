from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import Required

class TournForm(Form):
    description = TextField('description', validators=[Required()])
    tourn_type = TextField('tourn_type')

class PlayerForm(Form):
    fname = TextField('fname', validators=[Required()])

class EntryForm(Form):
    enter = BooleanField('enter', default = False)

class TourneyEntry(Form):
    enter = SelectMultipleField(
        'Enter',
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False)
        )
