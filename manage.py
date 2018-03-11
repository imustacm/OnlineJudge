from flask_script import Manager
from flask_script import Shell
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from core import create_app
from core.db import db
from models import models

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, models=models)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
