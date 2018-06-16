#surveys routes.py

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_babel import _, get_locale
#from guess_language import guess_language
from app import db
#from app.api.forms import [insert relevant api/forms here ]
from app.models import User, FyOneGoals
from app.translate import translate
from app.api import bp
import json
from flask import jsonify
from app.models import FyOneGoals


from app.api import bp

@bp.route('/fygoal/<int:id>', methods=['GET'])
def get_fygoal(id):
    req_data = request.get_json()
    
    FirstDraftGoal  = ['pages']['name']['page1']['elements']['name']['FirstDraftGoal']
    startDate       = ['pages']['name']['page1']['elements']['name']['startDate']
    endDate         = ['pages']['name']['page1']['elements']['name']['endDate']
    specific_fy01   = ['pages']['name']['page2']['elements']['name']['specific_fy01']
    measurable_fy01 = ['pages']['name']['page2']['elements']['name']['measurable_fy01']
    achievable_fy01 = ['pages']['name']['page2']['elements']['name']['achievable_fy01']
    relevant_fy01   = ['pages']['name']['page2']['elements']['name']['relevant_fy01']
    timely_fy01     = ['pages']['name']['page2']['elements']['name']['timely_fy01']
    finalGoal_fy01  = ['pages']['name']['page3']['elements']['name']['finalGoal_fy01']

    return 

@bp.route('/fygoal', methods=['GET'])
def get_users():
    pass

@bp.route('/fygoal/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass

@bp.route('/fygoal/<int:id>/followed', methods=['GET'])
def get_followed(id):
    pass

@bp.route('/fygoal', methods=['POST'])
def create_user():
    pass

@bp.route('/fygoal/<int:id>', methods=['PUT'])
def update_user(id):
    pass
