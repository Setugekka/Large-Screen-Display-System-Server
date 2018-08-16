#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
from webapp.models import m_equipment,db
m_equipment_blueprint = Blueprint(
    'm_equipment',
    __name__,
    url_prefix="/m_equipment"
)
@m_equipment_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_all():
    city = request.args.get('city')
    if city == '':
        city = "all"
        data = m_equipment.query.all()
    else:
        data = m_equipment.query.filter(m_equipment.City == city).all()
    result = map(trans_result_from_data, data)
    print(data)
    data_for_tree = {
        'Name': "物资情况",
        'children': [{
            'Name': "基干装备",
            'children': result,
            'Id': "001",
            'City':city,
            'Type':"11",
            'Num':"175",
            'Model':"111",
            'Standard':"11",
            'Unit':"件"
        }],
    }
    return response(jsonify(data_for_tree))


def trans_result_from_data(i):
    if i.Num:
        data = {
            "Id": i.Id,
            "Name": i.Name,
            "Num": float(i.Num),
            "Unit": i.Unit,
            "Type": i.Type,
            "Model": i.Model,
            "Standard": i.Standard,
            "City": i.City,
        }
    else:
        data = {
            "Id": i.Id,
            "Name": i.Name,
            "Num": float(0),
            "Unit": i.Unit,
            "Type": i.Type,
            "Model": i.Model,
            "Standard": i.Standard,
            "City": i.City,
        }
    return data



@m_equipment_blueprint.route('/equipmentlist_by_city',methods=('GET', 'POST'))
def equipmentlist_by_city():
    city = request.args.get('city')
    equipmentlist=[]
    if city == 'null':
        data = db.session.query(m_equipment.Name, db.func.count('*').label("dcount")).group_by(m_equipment.Name).all()
    else:
        data = db.session.query(m_equipment.Name, db.func.count('*').label("dcount")).filter(
            m_equipment.City == city).group_by(m_equipment.Name).all()
    for i in data:
        equipmentlist.append(i[0])
    print(equipmentlist)
    return response(jsonify({"property": "equipmentlist_by_city", "city": city, "equipmentlist": equipmentlist}))