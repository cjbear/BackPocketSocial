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
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  
    fypriority_name = db.Column(db.String(20))
    fypriority_value = db.Column(db.String(20))
    addpriority_name  = db.Column(db.String(20))
    fypriority_reflect = db.Column(db.String(20))
    
    isPartialCompleted = db.Column(db.Boolean(True))
    isCompleted = db.Column(db.Boolean(True))

                    
                
                           
                
                  
                   
                        
                     
                 
                         
                     
