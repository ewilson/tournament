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
        choices=[('val_a','Value A'), ('val_b','Value B'), ('val_c','Value C')],
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False)
        )
