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
from app.models.FyPrioritiesModel import FyPrioritiesModel
from app.models.BarriersModel import BarriersModel


@bp.route('/menu', methods=['GET'])
def menu():
    return render_template('api/menu.html')

#BARRIERS

@bp.route('/barriers_form', methods=['GET'])
def barriers_form():
    return render_template('api/barriers_form.html')

@bp.route('/get_barriers/<username>', methods=['GET', 'POST'])
def get_barriers(username):
    user = User.query.filter_by(username=username).first_or_404()
    barriers = user.barriers.order_by(BarriersModel.timestamp.desc())
    return render_template('api/get_barriers.html', user=user) 

@bp.route('/add_barriers/<username>',methods=['POST'])
def add_barriers(username, data):
    barriers_data = request.get_json()
    cur = mysql.connection.cursor()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    try:
        data = json.loads(barriers_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    for key, value in barriers.items():
            if not value:
                return jsonify({'error': 'value for {} is empty'.format(key)})
            new_barriers = BarriersModel(
                barrier_name  = ['pages']['elements']['choices']['text'],
                barrier_value = ['pages']['elements']['choices']['value'],
                author = current_user
                )
            db.session.add(new_barriers)
            db.session.commit()
            result = barriers.dump(BarriersModel.query.get(barrier.id))
            return jsonify({
                'message': 'Your barriers are saved.',
                'new_barriers': result,
        })
            return redirect(url_for('api.add_barriers/<username>', username=current_user.username))

#FIRST YEAR GOALS

@bp.route('/fygoals_form', methods=['GET'])
def fygoals_form():
    return render_template('api/fyGoals_form.html')

@bp.route('/get_fygoals/<username>', methods=['GET', 'POST'])
def get_fygoals(username):
    user = User.query.filter_by(username=username).first_or_404()
    fygoals = user.fygoals.order_by(BarriersModel.timestamp.desc())
    return render_template('api/get_fygoals.html')

@bp.route('/add_fygoal/', methods=['GET', 'POST'])
def add_fygoal(data):
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
            new_fygoal = FyGoalModel(
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

#FIRST YEAR PRIORITIES

@bp.route('/fypriorities_form', methods=['GET'])
def fypriorities_form():
    return render_template('api/fyPriorities_form.html')

@bp.route('/get_fypriorities/<username>', methods=['GET', 'POST'])
def get_fypriorities(username):
    user = User.query.filter_by(username=username).first_or_404()
    fypriorities = current_user.fypriorities.all()
    return render_template('api/get_fypriorities.html')

@bp.route('/add_fypriorities/', methods=['GET', 'POST'])
def add_fypriorities(data):
    if request.method == 'POST':
        req_data = request.get_json()
        fyPrioritiesData = fyPrioritiesResponse.json()
        for key, value in fyPrioritiesData.items():
            if not value:
                return jsonify({'error': 'value for {} is empty'.format(key)})
        new_fyPriorities = FyPrioritiesModel(
            fypriority_name     = ['pages']['name']['page1']['elements']['name']['Declare my major by the end of this academic year.']['choices']['value']['value']['value'],
            fypriority_value    = ['pages']['name']['page1']['elements']['choices']['value'],
            addpriority_name    = ['pages']['name']['page2']['elements']['items']['title'],
            fypriorityreflect   = ['pages']['name']['page2']['elements']['title'],
            author = current_user
            )
        db.session.add(new_fyPriorities)
        db.session.commit()

    return render_template('api/barriersResults.html')

#this route sets-up a smart goal to track.
@bp.route('/add_trackgoal/', methods=['GET', 'POST'])
def add_trackgoal(username):
    form = PostForm()
    if form.validate_on_submit():
        trackgoals = TrackGoalModel(timestamp = datetime.date.today(), body=form.post.data, author=current_user)
        db.session.commit()
        flash(_('Your are ready to achieve your goal!'))
        return redirect(url_for('api.trackgoal', username=current_user.username))
    return render_template('api/add_trackgoal.html', title='Add a goal to track.', form=form)

#another route needed to update goal progress. User enters data that shows that he or she is working towards goal.
