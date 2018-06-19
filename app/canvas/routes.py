
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
from app.models import User, Assignments
from app.translate import translate
from app.canvas import bp

course_id = 12345
API_URL = 'https://canvas.instructure.com/api/v1/'
API_KEY = '7~pMe69XczZkRi2anWMxItDgHpAeC0HnHvb0lZlAghSoxu5gS1GdmEjsn98c8Waf7C'


@bp.route('/assignments', methods=['GET', 'POST'])
def assignments():
    url = 'https://canvas.instructure.com/api/v1/courses/1234368/assignments.json?'
    CANVAS_API_KEY = '7~pMe69XczZkRi2anWMxItDgHpAeC0HnHvb0lZlAghSoxu5gS1GdmEjsn98c8Waf7C'
    headers = {'Authorization': 'Bearer ' + CANVAS_API_KEY}
    params = {
        }
    response = requests.get(url, headers = headers, params=params)
    assignments = response.json()
    print(assignments)
    for assignment in assignments:
        description = assignment["description"],
        due_at = assignment["due_at"],
        unlock_at = assignment["unlock_at"],
        lock_at = assignment["lock_at"]
    return render_template('canvas/assignments.html')


#canvasapi.paginated_list.PaginatedList
#canvasapi.assignment.Assignment