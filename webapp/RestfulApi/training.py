#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
import sys

reload(sys)
sys.setdefaultencoding('utf8')

training_blueprint = Blueprint(
    'training',
    __name__,
    url_prefix="/training"
)


@training_blueprint.route('/get_result',methods=('GET', 'POST'))
def get_result():
    city = request.args.get('city')
    city = city[:-1]
    town_list = []
    commited_list = []
    uncommited_list = []
    data=[
        {
            'name': '沈阳',
            'children': [
                {
                    'name':'和平区',
                    'value':1
                },
                {
                    'name': '皇姑区',
                    'value': 1
                },
                {
                    'name': '沈河区',
                    'value': 1
                },
                {
                    'name': '大东区',
                    'value': 1
                },
                {
                    'name': '铁西区',
                    'value': 1
                },
                {
                    'name': '苏家屯区',
                    'value': 1
                },
                {
                    'name': '沈北新区',
                    'value': 1
                },
                {
                    'name': '于洪区',
                    'value': 1
                },
                {
                    'name': '辽中区',
                    'value': 1
                },
                {
                    'name': '新民市',
                    'value': 1
                },
                {
                    'name': '康平县',
                    'value': 1
                },
                {
                    'name': '法库县',
                    'value': 1
                },

            ]
        },
        {
            'name': '大连',
            'children': [
                {
                    'name': '西岗区',
                    'value': 1
                },
                {
                    'name': '中山区',
                    'value': 1
                },
                {
                    'name': '沙河口区',
                    'value': 0
                },
                {
                    'name': '甘井子区',
                    'value': 1
                },
                {
                    'name': '旅顺口区',
                    'value': 0
                },
                {
                    'name': '金州区',
                    'value': 1
                },
                {
                    'name': '普兰店区',
                    'value': 1
                },
                {
                    'name': '瓦房店市',
                    'value': 1
                },
                {
                    'name': '庄河市',
                    'value': 1
                },
                {
                    'name': '长海县',
                    'value': 0
                }

            ]
        },
        {
            'name': '鞍山',
            'children': [
                {
                    'name': '铁西区',
                    'value': 1
                },
                {
                    'name': '立山区',
                    'value': 1
                },
                {
                    'name': '千山区',
                    'value': 1
                },
                {
                    'name': '铁东区',
                    'value': 1
                },
                {
                    'name': '海城市',
                    'value': 1
                },
                {
                    'name': '台安县',
                    'value': 1
                },
                {
                    'name': '岫岩满族自治县',
                    'value': 1
                },
            ]
        },
        {
            'name': '抚顺',
            'children': [
                {
                    'name': '新抚区',
                    'value': 1
                },
                {
                    'name': '望花区',
                    'value': 0
                },
                {
                    'name': '东洲区',
                    'value': 1
                },
                {
                    'name': '抚顺县',
                    'value': 0
                },
                {
                    'name': '新宾满族自治县',
                    'value': 1
                },
                {
                    'name': '清原满族自治县',
                    'value': 0
                },
            ]
        },
        {
            'name': '本溪',
            'children': [
                {
                    'name': '溪湖区',
                    'value': 0
                },
                {
                    'name': '明山区',
                    'value': 1
                },
                {
                    'name': '南芬区',
                    'value': 0
                },
                {
                    'name': '本溪满族自治县',
                    'value': 1
                },
                {
                    'name': '桓仁满族自治县',
                    'value': 1
                },

            ]
        },
        {
            'name': '丹东',
            'children': [
                {
                    'name': '振兴区',
                    'value': 1
                },
                {
                    'name': '元宝区',
                    'value': 1
                },
                {
                    'name': '振安区',
                    'value': 0
                },
                {
                    'name': '东港市',
                    'value': 1
                },
                {
                    'name': '凤城市',
                    'value': 1
                },
                {
                    'name': '宽甸满族自治县',
                    'value': 1
                }]
        },
        {
            'name': '盘锦',
            'children': [
                {
                    'name': '双台子区',
                    'value': 1
                },
                {
                    'name': '兴隆台区',
                    'value': 1
                },
                {
                    'name': '大洼区',
                    'value': 1
                },
                {
                    'name': '盘山县',
                    'value': 1
                }
            ]
        },
    {
        'name': '营口',
        'children': [
            {
                'name': '站前区',
                'value': 0
            },
            {
                'name': '西安区',
                'value': 1
            },
            {
                'name': '鲅鱼圈区',
                'value': 0
            },
            {
                'name': '老边区',
                'value': 0
            },
            {
                'name': '盖州市',
                'value': 1
            },
            {
                'name': '大石桥市',
                'value': 1
            }
        ]
    },
    {
        'name': '葫芦岛',
        'children': [
            {
                'name': '连山区',
                'value': 0
            },
            {
                'name': '龙岗区',
                'value': 1
            },
            {
                'name': '南票区',
                'value': 0
            },
            {
                'name': '兴城市',
                'value': 1
            },
            {
                'name': '绥中县',
                'value': 0
            },
            {
                'name': '建昌县',
                'value': 1
            }
        ]
    },
    {
        'name': '朝阳',
        'children': [
            {
                'name': '双塔区',
                'value': 1
            },
            {
                'name': '龙城区',
                'value': 1
            },
            {
                'name': '北票市',
                'value': 1
            },
            {
                'name': '凌源市',
                'value': 1
            },
            {
                'name': '朝阳县',
                'value': 1
            },
            {
                'name': '建平县',
                'value': 1
            },
            {
                'name': '喀喇沁左翼蒙古族自治县',
                'value': 1
            },
        ]
    },
    {
        'name': '阜新',
        'children': [
            {
                'name': '海州区',
                'value': 1
            },
            {
                'name': '新邱区',
                'value': 1
            },
            {
                'name': '太平区',
                'value': 0
            },
            {
                'name': '清河门区',
                'value': 1
            },
            {
                'name': '细河区',
                'value': 1
            },
            {
                'name': '阜新蒙古族自治县',
                'value': 0
            },
            {
                'name': '彰武县',
                'value': 0
            },
        ]
    },
    {
        'name': '辽阳',
        'children': [
            {
                'name': '白塔区',
                'value': 1
            },
            {
                'name': '文圣区',
                'value': 1
            },
            {
                'name': '宏伟区',
                'value': 0
            },
            {
                'name': '弓长岭区',
                'value': 1
            },
            {
                'name': '太子河区',
                'value': 1
            },
            {
                'name': '灯塔市',
                'value': 1
            },
            {
                'name': '辽阳县',
                'value': 1
            },

        ]
    },
    {
        'name': '铁岭',
        'children': [
            {
                'name': '清河区',
                'value': 1
            },
            {
                'name': '调兵山市',
                'value': 1
            },
            {
                'name': '开原市',
                'value': 1
            },
            {
                'name': '铁岭县',
                'value': 1
            },
            {
                'name': '昌图县',
                'value': 0
            },
            {
                'name': '西丰县',
                'value': 1
            }]
    },
    {
        'name': '锦州',
        'children': [
            {
                'name': '古塔区',
                'value': 1
            },
            {
                'name': '凌河区',
                'value': 1
            },
            {
                'name': '太和区',
                'value': 1
            },
            {
                'name': '凌海市',
                'value': 1
            },
            {
                'name': '北镇市',
                'value': 1
            },
            {
                'name': '黑山县',
                'value': 0
            },
            {
                'name': '义县',
                'value': 1
            }
        ]
    }
    ]
    for i in data:
        print (i)
        if i['name'] == city:
            town_list = i['children']
            for town in town_list:
                if town['value'] == 1:
                    commited_list.append(town['name'])
                else:
                    uncommited_list.append(town['name'])
    if uncommited_list == []:
        uncommited_list.append('全部提交')
    return response(jsonify({"commited_list": commited_list,"uncommited_list":uncommited_list}))

