#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
from webapp.models import m_urgent_stuff,db
m_stuff_blueprint = Blueprint(
    'm_stuff',
    __name__,
    url_prefix="/m_stuff"
)
@m_stuff_blueprint.route('/get_all',methods=('GET', 'POST'))
def get_all():
    city = request.args.get('city')
    if city == '':
        city = "all"
        data = m_urgent_stuff.query.all()
    else:
        data = m_urgent_stuff.query.filter(m_urgent_stuff.City == city).all()
    result = map(trans_result_from_data, data)
    print(data)
    data_for_tree = {
        'Name': "物资情况",
        'children': [{
            'Name': "抢修材料",
            'children': result,
            'Id': "002",
            'City':city,
            'Type':"11",
            'Num':"175",
            'Unit':"件",
            'Position': "",
            'Time': "",
            'Keeper': "",
            'Phone': ""
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
            "Position": i.Position,
            "Time": i.Time,
            "Keeper": i.Keeper,
            "City": i.City,
        }
    else:
        data = {
            "Id": i.Id,
            "Name": i.Name,
            "Num": float(0),
            "Unit": i.Unit,
            "Type": i.Type,
            "Position": i.Position,
            "Time": i.Time,
            "Keeper": i.Keeper,
            "City": i.City,
        }
    return data