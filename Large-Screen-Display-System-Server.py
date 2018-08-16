import os
from flask_script import Manager, Server
from webapp import create_app
from webapp.models import db

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())
manager = Manager(app)
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict(app=app,db=db)

if __name__ == "__main__":
    manager.run()