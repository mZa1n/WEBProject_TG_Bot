from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


# Форма удаления задачи
class TasksFormDel(FlaskForm):
    content = StringField('Номер задачи', validators=[DataRequired()])
    submit = SubmitField('Удалить задачу')
