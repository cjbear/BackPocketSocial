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
    id = db.Column(db.String(36), primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  
    name = db.Column(db.String(128), index=True)
    priority = db.Column(db.String(10))
    due_date = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    complete = db.Column(db.Boolean, default=False)

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100