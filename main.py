from app import create_app, app, db, cli
import cli.app
from models import User, PostModel, MessageModel, NotificationModel, TaskModel, AssignmentModel, FyGoalModel
from flask_bootstrap import Bootstrap

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'PostModel': PostModel, 'MessageModel': MessageModel,
            'NotificationModel': NotificationModel, 'TaskModel': TaskModel, 'FyGoalModel': FyGoalModel, 'AssignmentModel': AssignmentModel}