
#comminications forms.py: messages, notifications, reflections, todos

from flask import request
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.fields import *
from wtforms_components import StringField, SelectField, DateField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User
import calendar


class PostForm(FlaskForm):
    post = TextAreaField(_l('Write a reflection.'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

class TaskForm(FlaskForm):
    todo_name = TextAreaField(_l(u'Task'), validators=[DataRequired()])
    todo_priority = SelectField(_l('Priority'), choices=[('high', 'high'), ('medium', 'medium'),('low', 'low')], coerce=str, option_widget=None, validators=[DataRequired()])
    due_date = DateField(_l('DatePicker', format='%Y-%m-%d'))
    submit = SubmitField(_l('Submit'))

class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))