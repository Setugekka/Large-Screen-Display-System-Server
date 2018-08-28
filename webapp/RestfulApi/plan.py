#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
import sys

reload(sys)
sys.setdefaultencoding('utf8')

plan_blueprint = Blueprint(
    'plan',
    __name__,
    url_prefix="/plan"
)


@plan_blueprint.route('/get_url',methods=('GET', 'POST'))
def get_list():
    url='/assets/pdf/test.pdf'
    return response(jsonify(url))