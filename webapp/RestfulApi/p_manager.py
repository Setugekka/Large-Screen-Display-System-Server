from flask import Blueprint, jsonify,request
from . import response
from webapp.models import p_manager,db
p_manager_blueprint = Blueprint(
    'p_manager',
    __name__,
    url_prefix="/p_manager"
)
@p_manager_blueprint.route('/count_all',methods=('GET', 'POST'))
def count_all():
    data=p_manager.query.count()
    return response(jsonify({"property":"p_manager_count_all","data":data}))

@p_manager_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_all():
    data = p_manager.query.all()
    result=map(lambda i:{"Id":i.Id,"Classification":i.Classification,"Field":i.Field,"Name":i.Name,"Sex":i.Sex,"Birthday":i.Birthday,"Education":i.Education,"Level":i.Level,"Working_seniority":float(i.Working_seniority),"Phone":i.Phone,"City":i.City},data)
    return response(jsonify(result))


@p_manager_blueprint.route('/count_by_city',methods=('GET', 'POST'))
def count_by_city():
    city=request.args.get('city')
    if city=='null':
        data = p_manager.query.count()
    else:
        data=p_manager.query.filter(p_manager.City == city).count()
    return response(jsonify({"property": "p_manager_count_by_city","city":city, "data": data}))

@p_manager_blueprint.route('/distribution_by_major_city',methods=('GET', 'POST'))
def distribution_by_major_city():
    city = request.args.get('city')
    if city=='null':
        data=db.session.query(p_manager.Major,db.func.count('*').label("dcount")).group_by(p_manager.Major).all()
    else:
        data = db.session.query(p_manager.Major, db.func.count('*').label("dcount")).filter(p_manager.City == city).group_by(
            p_manager.Major).all()
    class_list=[]
    value_list=[]
    for i in data:
        class_list.append(i[0])
        value_list.append(i[1])
    return response(jsonify({"property": "p_manager_distribution_by_major_city", "city": city, "class_list": class_list,"value_list":value_list}))

