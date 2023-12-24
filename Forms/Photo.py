from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired



class PhotoForm(FlaskForm):
    file = FileField('Фото', validators=[DataRequired()])
    submit = SubmitField('Проверить')