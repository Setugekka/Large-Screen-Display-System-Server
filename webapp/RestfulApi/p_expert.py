#encoding:utf-8
from flask import Blueprint, jsonify,request
from . import response
from webapp.models import p_expert,db
p_expert_blueprint = Blueprint(
    'p_expert',
    __name__,
    url_prefix="/p_expert"
)
@p_expert_blueprint.route('/count_all',methods=('GET', 'POST'))
def count_all():
    data=p_expert.query.count()
    return response(jsonify({"property":"p_expert_count_all","data":data}))

@p_expert_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_all():
    data = p_expert.query.all()
    result=map(lambda i:{"Id":i.Id,"Classification":i.Classification,"Field":i.Field,"Name":i.Name,"Sex":i.Sex,"Birthday":i.Birthday,"Education":i.Education,"Level":i.Level,"Working_seniority":float(i.Working_seniority),"Phone":i.Phone,"City":i.City},data)
    return response(jsonify(result))


@p_expert_blueprint.route('/count_by_city',methods=('GET', 'POST'))
def count_by_city():
    city=request.args.get('city')
    if city=='null':
        data = p_expert.query.count()
    else:
        data=p_expert.query.filter(p_expert.City == city).count()
    return response(jsonify({"property": "p_expert_count_by_city","city":city, "data": data}))

@p_expert_blueprint.route('/distribution_by_major_city',methods=('GET', 'POST'))
def distribution_by_major_city():
    city = request.args.get('city')
    if city=='null':
        data=db.session.query(p_expert.Classification,db.func.count('*').label("dcount")).group_by(p_expert.Classification).all()
    else:
        data = db.session.query(p_expert.Classification, db.func.count('*').label("dcount")).filter(p_expert.City == city).group_by(
            p_expert.Classification).all()
    class_list=[]
    value_list=[]
    for i in data:
        class_list.append(i[0])
        value_list.append(i[1])
    # return response(jsonify({"property": "p_expert_distribution_by_major_city", "city": city, "class_list": class_list,"value_list":value_list}))
    return response(jsonify({"property": "p_expert_distribution_by_major_city", "city": city, "class_list": ['自然灾害','事故灾难','安全检查','信访' ,'继电保护', '消防安全管理', '电网规划管理', '后勤管理', '基建' ,'配电运检', '变电检修','规划设计'],"value_list":[1,3,5,4,3,1,5,7,6,2,3,3]}))
