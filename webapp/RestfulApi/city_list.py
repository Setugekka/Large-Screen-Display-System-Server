#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
from webapp.models import city_id,db
city_blueprint = Blueprint(
    'city',
    __name__,
    url_prefix="/city"
)

@city_blueprint.route('/get_cityList',methods=('GET', 'POST'))
def get_cityList():
    data = city_id.query.all()
    result=map(lambda i:{"name":i.Name,"value": 1},data)
    return response(jsonify(result))