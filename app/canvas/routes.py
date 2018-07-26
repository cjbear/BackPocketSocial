
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

course_id = 12345
API_URL = 'https://canvas.instructure.com/api/v1/'
API_KEY = '7~pMe69XczZkRi2anWMxItDgHpAeC0HnHvb0lZlAghSoxu5gS1GdmEjsn98c8Waf7C'

@bp.route('/getAssignments/', methods=['GET', 'POST'])
def getAssignments():
    url = 'https://canvas.instructure.com/api/v1/courses/1234368/assignments.json?'
    CANVAS_API_KEY = '7~pMe69XczZkRi2anWMxItDgHpAeC0HnHvb0lZlAghSoxu5gS1GdmEjsn98c8Waf7C'
    headers = {'Authorization': 'Bearer ' + CANVAS_API_KEY}
    params = {
        }
    response = requests.get(url, headers = headers, params=params)
    assignments = response.json()
    for assignment in assignments:
        assignment = AssignmentModel(description=assignment.description, due_at = assignment.due_at, unlock_at = assignment.unlock_at,
            lock_at = assignment.lock_at, author=current_user) 
        db.session.commit()
        flash(_('Your assignments are saved.'))
    return render_template('canvas/getAssignments.html')

@bp.route('/showAssignments/<username>', methods=['GET', 'POST'])
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