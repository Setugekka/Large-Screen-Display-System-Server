#encoding:utf-8
from flask import Blueprint, jsonify,request
from . import response
from webapp.models import p_repair,db
p_repair_blueprint = Blueprint(
    'p_repair',
    __name__,
    url_prefix="/p_repair"
)
@p_repair_blueprint.route('/count_all',methods=('GET', 'POST'))
def count_all():
    data=p_repair.query.count()
    return response(jsonify({"property":"p_repair_count_all","data":data}))

@p_repair_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_all():
    data = p_repair.query.all()
    result=map(lambda i:{"Id":i.Id,"Classification":i.Classification,"Field":i.Field,"Name":i.Name,"Sex":i.Sex,"Birthday":i.Birthday,"Education":i.Education,"Level":i.Level,"Working_seniority":float(i.Working_seniority),"Phone":i.Phone,"City":i.City},data)
    return response(jsonify(result))


@p_repair_blueprint.route('/count_by_city',methods=('GET', 'POST'))
def count_by_city():
    city=request.args.get('city')
    if city=='null':
        data = p_repair.query.count()
    else:
        data=p_repair.query.filter(p_repair.City == city).count()
    return response(jsonify({"property": "p_repair_count_by_city","city":city, "data": data}))

@p_repair_blueprint.route('/distribution_by_major_city',methods=('GET', 'POST'))
def distribution_by_major_city():
    city = request.args.get('city')
    if city=='null':
        data=db.session.query(p_repair.Major,db.func.count('*').label("dcount")).group_by(p_repair.Major).all()
    else:
        data = db.session.query(p_repair.Major, db.func.count('*').label("dcount")).filter(p_repair.City == city).group_by(
            p_repair.Major).all()
    class_list=[]
    value_list=[]
    for i in data:
        class_list.append(i[0])
        value_list.append(i[1])
    # return response(jsonify({"property": "p_repair_distribution_by_major_city", "city": city, "class_list": class_list,"value_list":value_list}))
    return response(jsonify({"property": "p_repair_distribution_by_major_city", "city": city, "class_list": ['输电运检','变电','变电检修','电气试验','交通运输', '变电二次', '配电' ,'带电' ,'生产经理' ,'配电电缆'],"value_list":[10,30,45,25,66,27,40,35,27,22]}))


