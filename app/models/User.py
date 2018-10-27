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

from app import db, login
from app.search import add_to_index, remove_from_index, query_index
from sqlalchemy import Column, Integer, DateTime

from app.models.PostModel import PostModel
from app.models.TaskModel import TaskModel
from app.models.FyGoalModel import FyGoalModel
from app.models.AssignmentModel import AssignmentModel
from app.models.MessageModel import MessageModel
from app.models.NotificationModel import NotificationModel
from app.models.FyPrioritiesModel import FyPrioritiesModel
from app.models.BarriersModel import BarriersModel


class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)

#This class is used to create a dictionary with a user collection of resources /
#survey results. For example, if an advisor wants to see the fygoals for all students. 

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data

#define models
roles_users = db.Table('role_users',
db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __table_args__ = {'extend_existing': True} 
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    mobileNumber = db.Column(db.String(12))
    about_me = db.Column(db.String(140))
    profile_photo = db.Column(db.LargeBinary)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    tasks = db.relationship('TaskModel', backref='user', lazy='dynamic')
    posts = db.relationship('PostModel', backref='author', lazy='dynamic')
    fygoals = db.relationship('FyGoalModel', backref='author', lazy='dynamic')

    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    assignments = db.relationship('AssignmentModel', 
                                    foreign_keys='AssignmentModel.student_id',
                                    backref='author', lazy='dynamic')
    
    messages_sent = db.relationship('MessageModel',
                                    foreign_keys='MessageModel.sender_id',
                                    backref='author', lazy='dynamic')

    messages_received = db.relationship('MessageModel',
                                    foreign_keys='MessageModel.recipient_id',
                                    backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)

    notifications = db.relationship('NotificationModel', backref='user',
                                    lazy='dynamic')

    fypriorities = db.relationship('FyPrioritiesModel', backref='user',
                                    lazy='dynamic')
    
    fygoals = db.relationship('FyGoalModel', backref='user',
                                    lazy='dynamic')

    barriers = db.relationship('BarriersModel', backref='user',
                                    lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8') 

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return MessageModel.query.filter_by(recipient=self).filter(
            MessageModel.timestamp > last_read_time).count()

    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = NotificationModel(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n

    def launch_task(self, name, description, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue('app.tasks.' + name, self.id,
                                                *args, **kwargs)
        task = TaskModel(id=rq_job.get_id(), name=name, description=description,
                    user=self)
        db.session.add(task)
        return task

    def get_tasks_in_progress(self):
        return TaskModel.query.filter_by(user=self, complete=False).all()

    def get_task_in_progress(self, name):
        return TaskModel.query.filter_by(name=name, user=self,
                                    complete=False).first()
#The to_dict function
    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'post_count': self.posts.count(),
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'avatar': self.avatar(128)
            }
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(100))
    profile_photo = db.Column(db.String(300))
    location = db.Column(db.String(100))

    def __init__(self, user_id, username, profile_pic, location):
        self.user_id = user_id
        self.username = username
        self.profile_pic = profile_pic
        self.location = location

    def __repr__(self):
        return '<UserDetails> %r' % self.username 
 
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))













