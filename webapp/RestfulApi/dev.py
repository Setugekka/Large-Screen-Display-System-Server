from flask import Blueprint, redirect, render_template, request
from webapp.socket import EmitService
es=EmitService()
dev_blueprint = Blueprint(
    'dev',
    __name__,
    url_prefix="/"
)
@dev_blueprint.route('hello',methods=('GET', 'POST'))
def hello():
    return "hello world"

@dev_blueprint.route('socket')
def index():
    return render_template('dev/index.html')

@dev_blueprint.route('p_o_s')
def pos_test():
    city=request.args.get('city')
    value=request.args.get('value')
    es.update_option_public_option_status(city,value)
    return 'success'

@dev_blueprint.route('s_m')
def sm_test():
    city=request.args.get('city')
    value=request.args.get('value')
    cood=[120.62,39]
    es.update_option_system_map(city,cood,'一般事件',value)
    return 'success'