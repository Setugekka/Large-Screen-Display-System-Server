import os
from flask_script import Manager, Server
from webapp import create_app
from webapp.models import *

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())
manager = Manager(app)
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    # return dict(app=app, db=db, users=users, roles=roles, finance_basics=finance_basics, stock_basics=stock_basics)
    return 0

if __name__ == "__main__":
    manager.run()