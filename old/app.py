from flask import Flask
from flask import request, redirect, url_for, render_template, json
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from sqlalchemy import literal
import psycopg2
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cjbear:Oak@8126103@localhost:3305/christopherjohnson'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = '$2ajfskal$KLJK34$3r$jklJKL$2ad'
app.debug = True

mysqldb = SQLAlchemy(app)

#sign-up routes

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email]'], request.form['password'])
    mysqldb.session.add(user)
    mysqldb.session.commit()
    return redirect(url_for('welcome.html'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(somewhere)

#@app.route('/user_list')
#@login_required
#def get_user_list():
 #   users = User.query.all()
 #   userD = UserDetails.query.all()
 #   return render_template('user_list.html', users = users, userD = userD)

@app.route('/editprofile')
@login_required
def edit_profile():
    now_user = User.query.filter_by(email = current_user.email).first()
    return render_template('user_detail.html', now_user = now_user)

@app.route('/add_user_details', methods=['POST'])
def add_user_details():
    user_details = UserDetails(request.form['pid'], request.form['username', request.form['profile_pic'], request.form['location']])
    mysqldb.session.add(user_details)
    mysqldb.session.commit()
    return redirect(url_for('index'))

@app.route('/profile/<id>')
def user_profile(id):
    oneUser = UserDetails.query.filter_by(id=id).first()
    sUser = User.query.filter_by(id = oneUser.user_id).first()
    user_posts = Post.query.filter_by(posted_by = sUser.email)

    return render_template('user_profile.html', oneUser = oneUser, sUser = sUser, user_posts = user_posts)

#Routes for posting messages

@app.route('/feed')
def get_post():
    singlePost = Post.query.all()
    return render_template('post_feed.html', singlePost=singlePost)

@app.route('/posting')
@login_required
def posting():
    now_user = User.query.filter_by(email = current_user.email).first()
    return render_template('add_post.html', now_user = now_user)


@app.route('/add_post', methods=['POST'])
def add_post():
    post = Post(request.form['pcontent'], request.form['pemail'])
    mysqldb.session.add(post)
    mysqldb.session.commit()
    return redirect(url_for('index'))

#define models
roles_users = mysqldb.Table('role_users',
mysqldb.Column('user_id', mysqldb.Integer(), mysqldb.ForeignKey('user.id')),
mysqldb.Column('role_id', mysqldb.Integer(), mysqldb.ForeignKey('role.id')))

class UserDetails(mysqldb.Model):
    id = mysqldb.Column(mysqldb.Integer, primary_key = True)
    user_id = mysqldb.Column(mysqldb.Integer)
    username = mysqldb.Column(mysqldb.String(100))
    profile_pic = mysqldb.Column(mysqldb.String(300))
    location = mysqldb.Column(mysqldb.String(100))

    def __init__(self, user_id, username, profile_pic, location):
        self.user_id = user_id
        self.username = username
        self.profile_pic = profile_pic
        self.location = location

    def __repr__(self):
        return '<UserDetails> %r' % self.username 
 
class Role(mysqldb.Model, RoleMixin):
    id = mysqldb.Column(mysqldb.Integer(), primary_key=True)
    name = mysqldb.Column(mysqldb.String(80), unique=True)
    description = mysqldb.Column(mysqldb.String(255))

class User(mysqldb.Model, UserMixin):
    id = mysqldb.Column(mysqldb.Integer, primary_key=True)
    firstName = mysqldb.Column(mysqldb.String(255))
    lastName = mysqldb.Column(mysqldb.String(255))
    username = mysqldb.Column(mysqldb.String(255))
    email = mysqldb.Column(mysqldb.String(255), unique=True)
    password = mysqldb.Column(mysqldb.String(255))
    active = mysqldb.Column(mysqldb.Boolean())
    confirmed_at = mysqldb.Column(mysqldb.DateTime())
    roles = mysqldb.relationship('Role', secondary=roles_users,
                            backref=mysqldb.backref('users', lazy='dynamic'))
    
    def __init__(self, firstName, lastName, username, email, password, active, confirmed_at, roles):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.active = active
        self.confirmed_at = datetime.datetime.now()
        self.roles = roles

class Post(mysqldb.Model):
    id = mysqldb.Column(mysqldb.Integer, primary_key=True)
    post_content = mysqldb.Column(mysqldb.String(200))
    posted_by = mysqldb.Column(mysqldb.String(100))

    def __init__ (self, post_content, posted_by):
        self.post_content = post_content
        self.posted_by = posted_by

    def __respr__(self):
        return '<Posr %r>' % self.post_content

class FyOneGoals(mysqldb.Model):
    id =mysqldb.Column(mysqldb.Integer, primary_key=True)
    FirstDraftGoal = mysqldb.Column(mysqldb.String(500))
    startDate = mysqldb.Column(mysqldb.String(10))
    endDate = mysqldb.Column(mysqldb.String(10))
    specific_fy01 = mysqldb.Column(mysqldb.String(255))
    measurable_fy01 = mysqldb.Column(mysqldb.String(255))
    achievable_fy01 = mysqldb.Column(mysqldb.String(255))
    relevant_fy01 = mysqldb.Column(mysqldb.String(255))
    timely_fy01 = mysqldb.Column(mysqldb.String(255))
    finalGoal_fy01 = mysqldb.Column(mysqldb.String(255))
    user_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('user.id'))
    user = mysqldb.relationship('User', uselist=False, backref='FyOneGoals')

    def __init__(
            self,
            FirstDraftGoal=None,
            startDate=None,
            endDate=None,
            specific_fy01=None,
            measurable_fy01=None,
            achievable_fy01=None,
            relevant_fy01=None,
            timely_fy01=None,
            finalGoal_fy01=None):
        self.FirstDraftGoal = FirstDraftGoal
        self.startDate = startDate
        self.endDate = endDate
        self.specific_fy01 = specific_fy01
        self.measurable_fy01 = measurable_fy01
        self.achievable_fy01 = achievable_fy01
        self.relevant_fy01 = relevant_fy01
        self.timely_fy01 = timely_fy01
        self.finalGoal_fy01 = timely_fy01

    def get_id(self):
        return unicode(self.id)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(mysqldb, User, Role)
security = Security(app, user_datastore)    

@app.route('/')
@login_required
def index():
    return render_template('index.html')

#survey routes

@app.route('/fygoals', methods=['GET', 'POST'])
@login_required
def api_fygoals():
    return render_template('fy01Goals.html') 


if __name__ == "__main__":
    app.run()
