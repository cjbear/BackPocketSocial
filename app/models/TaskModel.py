import base64
import json
import os
import jwt
import redis
import rq

from datetime import datetime, timedelta
from time import time
from hashlib import md5

from flask import current_app, url_for
from flask_login import UserMixin
from flask_security import Security, SQLAlchemyUserDatastore, RoleMixin, login_required

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, DateTime

from app import db, login
from app.search import add_to_index, remove_from_index, query_index
from app.models import User

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  
    name = db.Column(db.String(128), index=True)
    priority = db.Column(db.String(10))
    due_date = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    description = db.Column(db.String(128))
    done = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<TaskModel {}>'.format(self.body)

