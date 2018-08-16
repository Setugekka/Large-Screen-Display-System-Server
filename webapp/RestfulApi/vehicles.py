#/usr/bin/envpython
#-*-coding:UTF-8-*-
#本模块主要实现汽车数据的跨表查询
from flask import Blueprint,jsonify
from webapp.models import db,Repaircar,Generator
from sqlalchemy import func
vehicles_blueprint=Blueprint(
    'vehicles',
    __name__,
    url_prefix="/vehicles"
)
#返回修理车与发电车总记录数
@vehicles_blueprint.route('/count',methods=('GET','POST'))
def count():
    res1 = db.session.query(Repaircar).count()
    res2 = db.session.query(Generator).count()
    res = res1+res2
    return jsonify({'data':res})

#按指定类别汇总
@vehicles_blueprint.route('/count_city/',methods=('GET','POST'))
def count_cat():
    #按城市统计修理车数
    dataSeries=[]
    cat1 = "Repaircar.City"
    res1 = db.session.query(eval(cat1),func.count(eval(cat1))).group_by(eval(cat1)).all()
    #将多维数组转化为字典
    res_dict1={}
    for item in res1:
        res_dict1[item[0]]=item[1]
    dataSeries.append(res_dict1)
    #按城市统计发电车数
    cat2 = "Generator.City"
    res2 = db.session.query(eval(cat2), func.count(eval(cat2))).group_by(eval(cat2)).all()
    # 将多维数组转化为字典
    res_dict2 = {}
    for item in res2:
        res_dict2[item[0]] = item[1]
    dataSeries.append(res_dict2)
    return jsonify({'data':dataSeries})

