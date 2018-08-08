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


class FyPrioritiesModel(db.Model):
    id =db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Major = db.Column(db.String(20))
    GradRequirements = db.Column(db.String(20))
    Gpa  = db.Column(db.String(20))
    AcademicSupport = db.Column(db.String(20))
    CareerOptions = db.Column(db.String(20))
    SportActivity = db.Column(db.String(20))
    Finances = db.Column(db.String(20))
    FacultyComm  = db.Column(db.String(20))
    LivingSituation = db.Column(db.String(20))
    Friends = db.Column(db.String(20))
    SocialClub = db.Column(db.String(20))
    PhysicalFitness = db.Column(db.String(20))     
    Stress = db.Column(db.String(20))             
    Volunteer = db.Column(db.String(20))           
    StudyAbroad = db.Column(db.String(20))         
            
    AddPriority01 = db.Column(db.String(20))       
    AddPriority02 = db.Column(db.String(20))       
    AddPriority03 = db.Column(db.String(20))       
    FyPriorityReflection = db.Column(db.String(20))
    
    isPartialCompleted = db.Column(db.Boolean(True))
    isCompleted = db.Column(db.Boolean(True))

                    
                
                           
                
                  
                   
                        
                     
                 
                         
                     
