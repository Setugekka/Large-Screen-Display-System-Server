#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
import sys

reload(sys)
sys.setdefaultencoding('utf8')

organization_blueprint = Blueprint(
    'organization',
    __name__,
    url_prefix="/organization"
)


@organization_blueprint.route('/get_list',methods=('GET', 'POST'))
def get_list():
    group=request.args.get('group')
    if group=="应急领导小组":
        data = {
            'name': '应急领导小组',
    'children': [{
      'name': '领导1',
      'children': [{
        'name': '成员1',
        'create': '二珂',
        'selected': 'true',
      }, {
        'name': '成员2',
      }, {
        'name': '成员3',
      }, {
        'name': '成员4',
      }, {
        'name': '成员5',
      }]
    }, {
      'name': '领导2',
      'children': [{
        'name': '成员1',
        'create': "二珂",
      }, {
        'name': '成员2',
      }, {
        'name': '成员3',
      }, {
        'name': '成员4',
      }, {
        'name': '成员5',
      }]
    }, {
     'name': '领导3',
      'children': [{
        'name': '成员1',
        'create': "二珂",
      }, {
        'name': '成员2',
      }, {
        'name': '成员3',
      }, {
        'name': '成员4',
      }, {
        'name': '成员5',
      }]
    }]
  }
    elif group == "安全应急办公室":
        data = {
            'name': '安全应急办公室',
            'children': [{
                'name': '领导1',
                'children': [{
                    'name': '成员1',
                    'create': '二珂',
                    'selected': 'true',
                }, {
                    'name': '成员2',
                }, {
                    'name': '成员3',
                }, {
                    'name': '成员4',
                }]
            }, {
                'name': '领导2',
                'children': [{
                    'name': '成员1',
                    'create': "二珂",
                }, {
                    'name': '成员2',
                }, {
                    'name': '成员3',
                }]
            }, {
                'name': '领导3',
                'children': [{
                    'name': '成员1',
                    'create': "二珂",
                }, {
                    'name': '成员2',
                }, {
                    'name': '成员3',
                }, {
                    'name': '成员4',
                }, {
                    'name': '成员5',
                }, {
                    'name': '成员6',
                    }
                ]
            }]
        }
    elif group == "稳定应急办公室":
        data = {
            'name': '稳定应急办公室',
            'children': [{
                'name': '领导1',
                'children': [{
                    'name': '成员1',
                    'create': '二珂',
                    'selected': 'true',
                }, {
                    'name': '成员2',
                }, {
                    'name': '成员3',
                }, {
                    'name': '成员4',
                }]
            }, {
                'name': '领导2',
                'children': [{
                    'name': '成员1',
                    'create': "二珂",
                }, {
                    'name': '成员2',
                }, {
                    'name': '成员3',
                }, {
                    'name': '成员4',
                }]
            }, {
                'name': '领导3',
                'children': [{
                    'name': '成员1',
                    'create': "二珂",
                }, {
                    'name': '成员2',
                }, {
                    'name': '成员3',
                }, {
                    'name': '成员4',
                }, {
                    'name': '成员5',
                }]
            }]
        }

    return response(jsonify(data))
