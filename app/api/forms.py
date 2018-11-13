#api\forms.py
#This code is underconstruction; it is not yet used in the working program. I am figureing out a program that would help students
#create measurable goals using metrics that could be tracked. The trick is to anticipate
#the various units of measurement. 

from flask import request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import Form
from wtforms.fields import *
from wtforms_components import StringField, SelectField, DateField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User
import calendar

from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

photos = UploadSet('photos', IMAGES)

class TrackGoalForm(FlaskForm):
    name = TextAreaField(_l(u'Goal Name'), validators=[DataRequired()])
    
    #describe what your accomplishment will look like
    smart_description = TextAreaField(_l('Description'))

    #Enter the date when you plan to achieve your goal. Suggestion: It is more satisfying to achieve smaller goals in short periods of time, such as one to six months from today.
    #add logic: if date > then six months from today, give user pop-up message suggesting a shorter time frame.
    due_date = DateField(_l('Due Date', format='%Y-%m-%d'))
    
    #Does your goal fit into a particular dimension of your well-being? If so, select it below.
    dimension = SelectField(_l('Well-being Dimension'), choices=[('Environmental', 'Environmental'), ('Intellectual', 'Intellectual'), ('Financial', 'Financial'), 
        ('Mental-Emotional', 'Mental-Emotional'), ('Occupational', 'Occupational'), ('Physical', 'Physical'), ('Social', 'Social'), ('Spiritual', 'Spiritual'), ], coerce=str, option_widget=None, validators=[DataRequired()])
    
    #how will you know that you have accomplished the goal?
  
    #enter the number of units that will demonstrate you have successfully accomplished the goal
    #For example, if your goal is to lose weight, enter the number of pounds or kilos that you plan to lose.
    #If you want to achieve a specific GPA, enter the GPA number.
    #If you plan to complete an single event (run a 10k foot race or a marathon) or earn a single techincal certification, enter 1. 
    unit_number = IntField(_l('Measurement Number'),
                             validators=[Length(min=0, max=10)]
    
    #enter the type of measurement
    unit_type = SelectField(_l(u'Unit of Measurement'), choices=[('number', 'number'), ('lbs', 'lbs'), ('kg', 'kg'), ('hours', 'hours'), ('minutes', 'minutes'), ('GPA', 'GPA')], coerce=str, option_widget=None, validators=[DataRequired()])

    done = SelectField(u'Complete?', choices=[('no', 'No'), ('yes', 'Yes'),])
    submit = SubmitField(_l('Submit'))