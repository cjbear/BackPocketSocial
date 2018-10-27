import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy import create_engine
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

engine = create_engine('mysql+mysqldb://root:Oak@8126103@localhost:3306/backpocketdb')

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:Oak@8126103@localhost:3306/backpocketdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = '$2ajfskal$KLJK34$3r$jklJKL$2ad'
   

    BOOTSTRAP_USE_MINIFIED = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    POSTS_PER_PAGE = 25
    TASKS_PER_PAGE = 25
    ASSIGNMENTS_PER_PAGE = 25
    BARRIERS_PER_PAGE = 25






   

