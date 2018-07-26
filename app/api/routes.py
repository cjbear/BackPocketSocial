#surveys routes.py

import json
from datetime import datetime

from flask import jsonify
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_sqlalchemy import SQLAlchemy

from app.api import bp
from app import db
from app.api import bp

from app.models.User import User
from app.models.FyGoalModel import FyGoalModel


@bp.route('/menu', methods=['GET'])
def menu():
    return render_template('api/menu.html')

@bp.route('/fygoals', methods=['GET'])
def fygoals():
    return render_template('api/fyGoals.html')

@bp.route('/fygoal/<username>', methods=['GET', 'POST'])
def add_fygoal(username):
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    try:
        data = fygoal_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

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
                finalGoal_fy01  = ['pages']['name']['page3']['elements']['name']['finalGoal_fy01'],
                author = current_user
                )
            db.session.add(new_fygoal)
            db.session.commit()
            result = fygoal_schema.dump(FyGoalModel.query.get(fygoal.id))
            return jsonify({
                'message': 'Your goal is saved.',
                'new_fygoal': result,
        })

    return render_template('api/fyGoalResult.html')


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