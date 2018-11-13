#api\routes.py

'''
These routes are for the student questionnaires. These need to be RESTFUL CRUD routes to support json questionnaires created using
the https://surveyjs.io/Overview/Library/. See the javascript files in the static folder.

'''

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

#This route displays the student self-assessments.
@bp.route('/menu', methods=['GET'])
def menu():
    return render_template('api/menu.html')

#BARRIERS SURVEY
#These CRUD routes are for the barriers questionnair.

#Displays a new barrier form.
@bp.route('/barriers_form', methods=['GET'])
def barriers_form():
    return render_template('api/barriers_form.html')

#Retrieves a user's barriers from the database.
@bp.route('/get_barriers/<username>', methods=['GET', 'POST'])
def get_barriers(username):
    user = User.query.filter_by(username=username).first_or_404()
    barriers = user.barriers.order_by(BarriersModel.timestamp.desc())
    return render_template('api/get_barriers.html', user=user) 

#adds user's new barriers to the database when user clicks submit button.
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

#Still to be written: Update user's existing barriers. This would add, replace, or delete individual barriers from user's existing set

'''
@bp.route('/update_barriers/<username>',methods=['POST'])
'''

#Delete's all user's existing barriers.

'''
@bp.route('/delete_barriers/<username>',methods=['POST'])
'''


#FIRST YEAR GOALS survey routes
#These CRUD routes are for the first year goal(s) questionnair.

#Displays a new first year goal form.
@bp.route('/fygoals_form', methods=['GET'])
def fygoals_form():
    return render_template('api/fyGoals_form.html')

#retrieves user's first year goal(s) to the database when user clicks submit button.
@bp.route('/get_fygoals/<username>', methods=['GET', 'POST'])
def get_fygoals(username):
    user = User.query.filter_by(username=username).first_or_404()
    fygoals = user.fygoals.order_by(BarriersModel.timestamp.desc())
    return render_template('api/get_fygoals.html')

#adds user's first year goal to the database when user clicks submit button.
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

#Still to be written: Update user's existing first year goals. 
#This would edit user's existing first year goal.

'''
@bp.route('/update_fygoal/<username>',methods=['POST'])
'''

#Deletes user's first year goal.

'''
@bp.route('/delete_fygoal/<username>',methods=['POST'])
'''

#FIRST YEAR PRIORITIES

#Displays a new first year priorities form.
@bp.route('/fypriorities_form', methods=['GET'])
def fypriorities_form():
    return render_template('api/fyPriorities_form.html')


#Retrieves user's first year priorities from the database.
@bp.route('/get_fypriorities/<username>', methods=['GET', 'POST'])
def get_fypriorities(username):
    user = User.query.filter_by(username=username).first_or_404()
    fypriorities = current_user.fypriorities.all()
    return render_template('api/get_fypriorities.html')


#Adds new first year priorities to the database.
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

#Still to be written: Update user's existing first year priorities. 
#This would edit user's existing first year priorities.

'''
@bp.route('/update_fypriorities/<username>',methods=['POST'])
'''

#Deletes all user's first year priorities.

'''
@bp.route('/delete_fypriorities/<username>',methods=['POST'])
'''

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
