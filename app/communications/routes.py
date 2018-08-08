#commuications routes.py: messages, notifications, reflections, todos

import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_babel import _, get_locale
from app import db
from app.main.forms import EditProfileForm, SearchForm 
from app.communications.forms import MessageForm, PostForm, TaskForm
from app.communications import bp

from app.models.User import User
from app.models.PostModel import PostModel
from app.models.TaskModel import TaskModel
from app.models.MessageModel import MessageModel
from app.models.NotificationModel import NotificationModel

@bp.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    current_user.add_notification('unread_message_count', 0)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        MessageModel.timestamp.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('communications.messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('communications.messages', page=messages.prev_num) \
        if messages.has_prev else None
    return render_template('communications/messages.html', messages=messages.items,
                           next_url=next_url, prev_url=prev_url)

@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        msg = MessageModel(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        user.add_notification('unread_message_count', user.new_messages())
        db.session.commit()
        flash(_('Your message has been sent.'))
        return redirect(url_for('communications.user', username=recipient))
    return render_template('communications/send_message.html', title=_('Send Message'),
                           form=form, recipient=recipient)

@bp.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
        NotificationModel.timestamp > since).order_by(NotificationModel.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications])

@bp.route('/export_posts')
@login_required
def export_posts():
    if current_user.get_task_in_progress('export_posts'):
        flash(_('An export task is currently in progress'))
    else:
        current_user.launch_task('export_posts', _('Exporting posts...'))
        db.session.commit()
    return redirect(url_for('communications.user', username=current_user.username))


@bp.route('/reflections/<username>', methods=['GET', 'POST'])
@login_required
def reflections(username):
    form = PostForm()
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(PostModel.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('communications.reflections', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('communications.reflections', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('communications/reflections.html', title=_('Reflections'), form=form, user=user,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)

@bp.route('/add_reflection/<username>', methods=['GET', 'POST'])
@login_required
def add_reflection(username):
    form = PostForm()
    if form.validate_on_submit():
        posts = PostModel(timestamp = datetime.date.today(), body=form.post.data, author=current_user)
        db.session.commit()
        flash(_('Your reflection is published.'))
        return redirect(url_for('communications.reflections', username=current_user.username))
    return render_template('communications/add_reflection.html', title='Add reflection.', form=form)


@bp.route('/todo/<username>', methods=['GET', 'POST'])
@login_required
def todo(username):
    form = TaskForm()
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    tasks = user.tasks.order_by(TaskModel.timestamp.desc()).paginate(
        page, current_app.config['TASKS_PER_PAGE'], False)
    next_url = url_for('communications.todo', page=tasks.next_num) \
        if tasks.has_next else None
    prev_url = url_for('communications.todo', page=tasks.prev_num) \
        if tasks.has_prev else None
    return render_template('communications/todo.html', title=_('Todo List'), form=form, user=user,
                           tasks=tasks.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/add_todo/<username>', methods=['GET', 'POST'])
@login_required
def add_todo(username):
    form = TaskForm()
    if form.validate_on_submit():
        tasks = TaskModel(name=form.name.data, priority=form.priority.data, due_date=form.due_date.data, description=form.description.data, done = form.done.data, user=current_user)
        db.session.commit()
        flash(_('Your task is posted.'))
        return redirect(url_for('communications.todo', username=current_user.username))
    return render_template('communications/add_todo.html', title='Add todo task.', form=form)