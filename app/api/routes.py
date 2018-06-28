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
from app.models import User, FyGoals
from app.translate import translate
from app.api import bp
import json
from flask import jsonify


from app.api import bp

@bp.route('/menu', methods=['GET'])
def menu():
    return render_template('api/menu.html')

@bp.route('/fygoals', methods=['GET'])
def fygoals():
    return render_template('api/fyGoals.html')

@bp.route('/fygoalsCompleted', methods=['GET', 'POST'])
def get_fygoal(id):
    if request.method == 'POST':
        fyGoalResult = request.get_json()
        fyGoalData = fyGoalResponse.json()
        for key, value in fyGoalData.items():
            if not value:
                return jsonify({'error': 'value for {} is empty'.format(key)})
        new_fygoal = FyGoals(
            FirstDraftGoal  = ['pages']['name']['page1']['elements']['name']['FirstDraftGoal'],
            startDate       = ['pages']['name']['page1']['elements']['name']['startDate'],
            endDate         = ['pages']['name']['page1']['elements']['name']['endDate'],
            specific_fy01   = ['pages']['name']['page2']['elements']['name']['specific_fy01'],
            measurable_fy01 = ['pages']['name']['page2']['elements']['name']['measurable_fy01'],
            achievable_fy01 = ['pages']['name']['page2']['elements']['name']['achievable_fy01'],
            relevant_fy01   = ['pages']['name']['page2']['elements']['name']['relevant_fy01'],
            timely_fy01     = ['pages']['name']['page2']['elements']['name']['timely_fy01'],
            finalGoal_fy01  = ['pages']['name']['page3']['elements']['name']['finalGoal_fy01']
            )
        db.session.add(new_fygoal)
        db.session.commit()

    return render_template('api/fyGoalsResults.html')


@bp.route('/barriers', methods=['GET'])
def barriers():
    return render_template('api/barriers.html')

@bp.route('/barriersCompleted', methods=['GET', 'POST'])
def barriersCompleted(id):
    if request.method == 'POST':
        barriersResult = request.get_json()
        barriersData = barriersResponse.json()
        for key, value in barriersData.items():
            if not value:
                return jsonify({'error': 'value for {} is empty'.format(key)})
        new_barriers = Barriers(
            FirstDraftGoal  = ['pages']['name']['page1']['elements']['name']['FirstDraftGoal'],
            startDate       = ['pages']['name']['page1']['elements']['name']['startDate'],
            endDate         = ['pages']['name']['page1']['elements']['name']['endDate'],
            specific_fy01   = ['pages']['name']['page2']['elements']['name']['specific_fy01'],
            measurable_fy01 = ['pages']['name']['page2']['elements']['name']['measurable_fy01'],
            achievable_fy01 = ['pages']['name']['page2']['elements']['name']['achievable_fy01'],
            relevant_fy01   = ['pages']['name']['page2']['elements']['name']['relevant_fy01'],
            timely_fy01     = ['pages']['name']['page2']['elements']['name']['timely_fy01'],
            finalGoal_fy01  = ['pages']['name']['page3']['elements']['name']['finalGoal_fy01']
            )
        db.session.add(new_barriers)
        db.session.commit()

    return render_template('api/barriersResults.html')

@bp.route('/fypriorities', methods=['GET'])
def fypriorities():
    return render_template('api/fyPriorities.html')

@bp.route('/completefypriorities', methods=['GET', 'POST'])
def completefypriorities():
    return render_template('api/completefypriorities.html')