from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class AllergensForm(FlaskForm):
    allergs = StringField('Аллергены', validators=[DataRequired()])
    submit = SubmitField('Изменить')