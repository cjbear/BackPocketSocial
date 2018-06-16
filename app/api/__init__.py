from flask import Blueprint

bp = Blueprint('surveys_api', __name__)

from app.api import routes