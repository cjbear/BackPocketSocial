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

@bp.route('/fypriorities', methods=['GET'])
def fypriorities():
    return render_template('api/fyPriorities.html')

@bp.route('/completefypriorities', methods=['GET', 'POST'])
def completefypriorities():
    return render_template('api/completefypriorities.html')

@bp.route('/add_fypriorities', methods=['GET', 'POST'])
def add_fypriorities(data):
    if request.method == 'POST':
        req_data = request.get_json()
        fyPrioritiesData = fyPrioritiesResponse.json()
        for key, value in fyPrioritiesData.items():
            if not value:
                return jsonify({'error': 'value for {} is empty'.format(key)})
        new_fyPriorities = FyPrioritiesModel(
            Major               = ['pages']['name']['page1']['elements']['name']['Declare my major by the end of this academic year.']['choices']['value']['value']['value'],
            GradRequirements    = ['pages']['name']['page1']['elements']['name']['Identify the graduation requirements for the major program that I am considering.']['choices']['value']['value']['value'],
            Gpa                 = ['pages']['name']['page1']['elements']['name']['Achieve or maintain my grade point average.']['choices']['value']['value']['value'],
            AcademicSupport     = ['pages']['name']['page1']['elements']['name']['Increase use of on campus academic support services.']['choices']['value']['value']['value'],
            CareerOptions       = ['pages']['name']['page1']['elements']['name']['Research and identify potential career options.']['choices']['value']['value']['value'],
            SportActivity       = ['pages']['name']['page1']['elements']['name']['Try a new sport or activity.']['choices']['value']['value']['value'],
            Finances            = ['pages']['name']['page1']['elements']['name']['Improve management of my personal finances.']['choices']['value']['value']['value'],
            FacultyComm         = ['pages']['name']['page1']['elements']['name']['Increase communication with, and seek advice from, faculty and advisors.']['choices']['value']['value']['value'],
            LivingSituation     = ['pages']['name']['page1']['elements']['name']['Improve my living situation.']['choices']['value']['value']['value'],
            Friends             = ['pages']['name']['page1']['elements']['name']['Make more friends.']['choices']['value']['value']['value'],
            SocialClub          = ['pages']['name']['page1']['elements']['name']['Participate in a social club.']['choices']['value']['value']['value'],
            PhysicalFitness     = ['pages']['name']['page1']['elements']['name']['Improve my physical fitness.']['choices']['value']['value']['value'],
            Stress              = ['pages']['name']['page1']['elements']['name']['Manage my stress and anxiety.']['choices']['value']['value']['value'],
            Volunteer           = ['pages']['name']['page1']['elements']['name']['Do volunteer work.']['choices']['value']['value']['value'],
            StudyAbroad         = ['pages']['name']['page1']['elements']['name']['Find and apply for a study abroad program.']['choices']['value']['value']['value'],
            
            AddPriority01       = ['pages']['name']['page2']['elements']['items']['name']['addFyPriority01'],
            AddPriority02       = ['pages']['name']['page2']['elements']['items']['name']['addFyPriority02'],
            AddPriority03       = ['pages']['name']['page2']['elements']['items']['name']['addFyPriority02'],
            FyPriorityReflection= ['pages']['name']['page2']['elements']['items']['name']['fyPrioritiesReflection'],
            )
        db.session.add(new_fyPriorities)
        db.session.commit()

    return render_template('api/barriersResults.html')

