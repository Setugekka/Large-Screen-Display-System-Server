#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
import sys
from webapp.models import plan_list,db

reload(sys)
sys.setdefaultencoding('utf8')

plan_blueprint = Blueprint(
    'plan',
    __name__,
    url_prefix="/plan"
)


def dataFormatter(rec):
    return {'name':rec.Name,'Id':rec.Id,'Belong_to':rec.Belong_to,'Level': rec.Level}


@plan_blueprint.route('/get_url',methods=('GET', 'POST'))
def get_list():
    url='/assets/pdf/ws.pdf'
    return response(jsonify(url))


@plan_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_all():
    all_plan=[]
    data_1 = plan_list.query.filter(plan_list.Level == 1).all()
    data_2 = plan_list.query.filter(plan_list.Level == 2).all()
    data_3 = plan_list.query.filter(plan_list.Level == 3).all()
    data_4 = plan_list.query.filter(plan_list.Level == 4).all()
    for i in data_1:
       i = dataFormatter(i)
       i['children'] = []
       i['value'] = 1
       for a in data_2:
           a = dataFormatter(a)
           a['value'] = 2
           a['children'] = []
           for b in data_3:
               b = dataFormatter(b)
               b['value'] = 3
               b['children'] = []
               for c in data_4:
                   c = dataFormatter(c)
                   c['value'] = 4
                   if c['Belong_to'] == b['Id']:
                       b['children'].append(c)
               if b['Belong_to'] == a['Id']:
                       a['children'].append(b)
           if a['Belong_to'] == i['Id']:
               i['children'].append(a)

    all_plan.append(i)

    return response(jsonify(all_plan))


