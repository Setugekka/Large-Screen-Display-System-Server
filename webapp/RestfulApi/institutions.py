#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
import sys

reload(sys)
sys.setdefaultencoding('utf8')

institutions_blueprint = Blueprint(
    'institutions',
    __name__,
    url_prefix="/institutions"
)


@institutions_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_list():
    data = [{
        "value": 3,
        "name": "《中华人民共和国应急法》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国家级别'
    }, {
        "value": 3,
        "name": "《中华人民共和国安全法》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国家级别'
    }, {
        "value": 2.5,
        "name": "《国家能源监管局预案评审及备案细则》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国家能监局'
    }, {
        "value": 2,
        "name": "《国家电网公司应急管理工作规定》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国网公司'
    }, {
        "value": 2,
        "name": "《国家电网公司应急预案管理办法》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国网公司'
    }, {
        "value": 2,
        "name": "《国家电网公司应急预案评审及备案管理办法》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国网公司'
    }, {
        "value": 2,
        "name": "《国家电网公司救援基干管理工作规定》",
        'url': '/assets/pdf/test.pdf',
        'classification': '国网公司'
    }];
    return response(jsonify(data))