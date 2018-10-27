import base64
import json
import os
import jwt
import redis
import rq

from time import time
from datetime import datetime, timedelta
from hashlib import md5

from flask import current_app, url_for
from flask_login import UserMixin
from flask_security import Security, SQLAlchemyUserDatastore, RoleMixin, login_required

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, DateTime

from app import db, login
from app.search import add_to_index, remove_from_index, query_index
from app.models import User


        #The to_dict function is supposed to convert the fygoal survey JSON data to
        #a python dictionary. The from_dict method below iterates throught the fields. 
        #If the fields are not empty, then the setattr records the data in the database (I think)
        #IsCompleted = db.Column(db.Boolean, default=False)

class FyGoalModel(db.Model):
    id =db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  
    FirstDraftGoal = db.Column(db.String(1000))
    startDate = db.Column(db.DateTime())
    endDate = db.Column(db.DateTime())
    specific_fy01 = db.Column(db.String(500))
    measurable_fy01 = db.Column(db.String(500))
    achievable_fy01 = db.Column(db.String(500))
    relevant_fy01 = db.Column(db.String(500))
    timely_fy01 = db.Column(db.String(500))
    finalGoal_fy01 = db.Column(db.String(1000))
    #reflection_fy01 = db.Column(db.String(2000))
    
    isPartialCompleted = db.Column(db.Boolean(True))
    isCompleted = db.Column(db.Boolean(True))

    def get_data(self):
        return json.loads(str(self.payload_json))
    
    def __repr__(self, user_id, FirstDraftGoal, startDate, endDate, specific_fy01, measurable_fy01, 
                achievable_fy01, relevant_fy01, timely_fy01, finalGoal_fy01):
        self.user_id = user_id
        self.FirstDraftGoal = FirstDraftGoal
        self.startDate = startDate
        self.endDate = endDate
        self.specific_fy01 = specific_fy01
        self.measurable_fy01 = measurable_fy01
        self.achievable_fy01 = achievable_fy01
        self.relevant_fy01 = relevant_fy01
        self.timely_fy01 = timely_fy01
        self.finalGoal_fy01 = finalGoal_fy01
        self.isPartialCompleted = isPartialCompleted
        self.isCompleted = isCompleted

    def __repr__(self):
        return '<fyGoal > %r' % self.username 

    def to_dict(self, include_email=False):
        fyGoalData = {
            'FirstDraftGoal': self.FirstDraftGoal,
            'startDate': self.startDate,
            'endDate' : self.endDate,
            'specific_fy01' : self.specific_fy01,
            'measurable_fy01' : self.measurable_fy01,
            'achievable_fy01' : self. achievable_fy01,
            'relevant_fy01' : self. relevant_fy01,
            'timely_fy01' : self.timely_fy01,
            'finalGoal_fy01' : self.finalGoal_fy01
            }
        return data

    def from_dict(self, surveyJSON, new_user=False):
        for field in ['FirstDraftGoal', 'startDate', 'endDate','specific_fy01','measurable_fy01','achievable_fy01', 'relevant_fy01', 'timely_fy01', 'finalGoal_fy01']:
            if field in data:
                setattr(self, field, data[field])

    def get_id(self):
        return unicode(self.id)

        from app.search import add_to_index, remove_from_index, query_index

class TrackGoalModel(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  
    name = db.Column(db.String(100))
    smart_description = db.Column(db.String(1000))
    due_date = db.Column(db.DateTime())
    dimension = db.Column(db.String(100))
    unit_number = db.Column(db.String(10))
    unit_type = db.Column(db.String(10))
    done = db.Column(db.String(10))
