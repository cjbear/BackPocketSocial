from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_babel import _, get_locale
#from guess_language import guess_language
from app import db
from app.main.forms import EditProfileForm, PostForm, SearchForm, TaskForm
from app.models import User, Post, Todotask
from app.translate import translate
from app.main import bp

from app.api import bp

@bp.route('/barriers/<int:id>', methods=['GET'])
def get_user(id):
    pass

@bp.route('/barriers', methods=['GET'])
def get_users():
    pass

@bp.route('/barriers/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass

@bp.route('/barriers/<int:id>/followed', methods=['GET'])
def get_followed(id):
    pass

@bp.route('/barriers', methods=['POST'])
def create_user():
    pass

@bp.route('/barriers/<int:id>', methods=['PUT'])
def update_user(id):
    pass
