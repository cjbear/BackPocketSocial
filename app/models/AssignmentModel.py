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
from canvasapi import Canvas

class AssignmentModel(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    description =  db.Column(db.String(128), index=True)
    due_at =  db.Column(db.DateTime())
    unlock_at =  db.Column(db.DateTime())
    lock_at =  db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    API_URL = 'https://canvas.instructure.com/api/v1/courses/1234368/assignments.json?'
    API_KEY = '7~pMe69XczZkRi2anWMxItDgHpAeC0HnHvb0lZlAghSoxu5gS1GdmEjsn98c8Waf7C'

    def __init__(self, canvas, id, description, due_at, unlock_at, lock_at):
        self.canvas = Canvas(API_URL, API_KEY)
        self.id = id
        self.description = description
        self.due_at = due_at
        self.unlock_at = unlock_at
        self.lock_at = lock_at

    def __repr__(self):
        return '<AssignmentModel {}>'.format(self.body)