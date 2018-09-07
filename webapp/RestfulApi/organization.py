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
      'name': '安全应急办公室',
      'children': [{
        'name': '测试用户',
        'create': '二珂',
        'selected': 'true',
      }, {
        'name': '项目管理中心',
      }, {
        'name': '电力调试控制中心',
      }, {
        'name': '安全监察质量部',
      }, {
        'name': '办公中心',
      }]
    }, {
      'name': '稳定应急办公室',
      'children': [{
        'name': '运维检修部',
        'create': "二珂",
      }, {
        'name': '农电工作部',
      }, {
        'name': '信息通讯中心',
      }, {
        'name': '物资供应中心',
      }, {
        'name': '综合服务',
      }]
    }, {
     'name': '紧急灾难处理中心',
      'children': [{
        'name': '变电抢修',
        'create': "二珂",
      }, {
        'name': '二次抢修',
      }, {
        'name': '物资调配',
      }, {
        'name': '通讯中心',
      }, {
        'name': '医疗分队',
      }]
    }]
  }
    elif group == "安全应急办公室":
        data = {
            'name': '安全应急办公室',
            'children': [{
                'name': '项目管理中心',
                'children': [{
                    'name': '主要负责人：赵xx',
                    'create': '二珂',

                }, {
                    'name': '负责人：李xx',
                }, {
                    'name': '联络员：王xx',
                }]
            }, {
                'name': '电力调度控制中心',
                'children': [{
                    'name': '带电作业',
                    'create': "二珂",
                }, {
                    'name': '电缆运检',
                }, {
                    'name': '配电运检',
                }, {
                    'name': '变电运检',
                }, {
                    'name': '输电运检',
                }]
            }, {
                'name': '安全监察质量部',
                'children': [{
                    'name': '部长：张xx',
                    'create': "二珂",
                }, {
                    'name': '副部长：吴xx',
                }
                ]
            }, {
                'name': '办公中心',
                'children': [{
                    'name': '和平客户服务中心',
                    'create': "二珂",
                }, {
                    'name': '沈河客户服务中心',
                }, {
                    'name': '大东客户服务中心',
                }, {
                    'name': '皇姑客户服务中心',
                }, {
                    'name': '铁西客户服务中心',
                }, {
                    'name': '浑南客户服务中心',
                    }
                ]
            }]
        }
    elif group == "稳定应急办公室":
        data = {
            'name': '稳定应急办公室',
            'children': [{
                'name': '运维检修部',
                'children': [{
                    'name': 'TBD',
                    'create': '二珂',
                }]
            }, {
                'name': '农电工作部',
                'children': [{
                    'name': 'TBD',
                    'create': "二珂",
                }]
            }, {
                'name': '信息通讯',
                'children': [{
                    'name': 'TBD',
                    'create': "二珂",
                }]
            }, {
                'name': '物资供应',
                'children': [{
                    'name': 'TBD',
                    'create': "二珂",
                }]
            }, {
                'name': '综合服务',
                'children': [{
                    'name': 'TBD',
                    'create': "二珂",
                }]
            }]
        }

    return response(jsonify(data))
