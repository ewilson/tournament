from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class TournForm(Form):
    description = TextField('description', validators=[Required()])
    tourn_type = TextField('tourn_type')
