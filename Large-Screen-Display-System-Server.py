#encoding:utf-8
import os
from flask_script import Manager, Server
from webapp import create_app,db,socketio
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())
# socketio启用
# socketio = SocketIO(app)
# manager启动
manager = Manager(app)
manager.add_command("server", Server())
manager.add_command('run', socketio.run(app=app,host='0.0.0.0'))
@manager.shell
def make_shell_context():
    return dict(app=app,db=db)

if __name__ == "__main__":
    manager.run()