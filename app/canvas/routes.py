#canvas\routes.py

'''
These routes are designed to use the Canvas LMS API to retrieve user's assignments
from their Canvas courses. 

Here is the Canvas LMS API documentation: https://canvas.instructure.com/doc/api/index.html.

CanvasAPI is an open source Pyton library could be 
used to more easily write these routes: https://github.com/ucfopen/canvasapi

Example code using CanvasAPI can be found here: 
https://canvasapi.readthedocs.io/en/latest/examples.html#boilerplate

'''

from canvasapi import Canvas
from flask import Flask
import requests
import json
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_babel import _, get_locale
#from guess_language import guess_language
from app import db
from app.canvas import bp

from app.models.User import User
from app.models.AssignmentModel import AssignmentModel

#
course_id = 12345
API_URL = 'https://canvas.instructure.com/api/v1/'
API_KEY = '7~pMe69XczZkRi2anWMxItDgHpAeC0HnHvb0lZlAghSoxu5gS1GdmEjsn98c8Waf7C'
canvas = Canvas(API_URL, API_KEY)

@bp.route('/getAssignments/<username>', methods=['GET', 'POST'])
@login_required
def get_assignments(username):
    assignments = course.get_assignments()
    for assignment in assignments:
        print(assignment)   
        db.session.commit(assignment)
        flash(_('Your assignments are saved.'))
    return render_template('canvas/getAssignments.html')

@bp.route('/showAssignments/<username>', methods=['GET', 'POST'])
@login_required
def showAssignments(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    assignments = user.assignments.order_by(AssignmentModel.timestamp.desc()).paginate(page, current_app.config['ASSIGNMENTS_PER_PAGE'], False)
    next_url = url_for('main.user', username=user.username, page=assignments.next_num) if assignments.has_next else None
    prev_url = url_for('main.user', username=user.username, page=assignments.prev_num) if assignments.has_prev else None
    return render_template('canvas/showAssignments.html', user=user, assignments=assignments.items,
                        next_url=next_url, prev_url=prev_url)
        


#canvasapi.paginated_list.PaginatedList
#canvasapi.assignment.Assignment
