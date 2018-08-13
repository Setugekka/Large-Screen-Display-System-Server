#/usr/bin/envpython
#-*-coding:UTF-8-*-
from flask import Blueprint,jsonify
from webapp.models import db,Generator
from sqlalchemy import func
generator_blueprint=Blueprint(
    'generator',
    __name__,
    url_prefix="/generator"
)
#返回发电车总数
@generator_blueprint.route('/count',methods=('GET','POST'))
def count():
    res = db.session.query(Generator).count()
    return jsonify({'data':res})

#按指定类别汇总(如：/count/City按城市汇总,/count/Position按位置汇总,/count/Capacity按容量汇总,/count/Department按部门汇总,/count/Factory按厂商汇总,/count/Condition按车辆状况汇总)
@generator_blueprint.route('/count/<category>',methods=('GET','POST'))
def count_cat(category):
    cat = "Generator."+category
    res = db.session.query(eval(cat),func.count(eval(cat))).group_by(eval(cat)).all()
    #将多维数组转化为字典
    res_dict={}
    for item in res:
        res_dict[item[0]]=item[1]
    return jsonify({'data':res_dict})

# 按指定城市的部门汇总
@generator_blueprint.route('/count/department/<city>',methods=('GET','POST'))
def count_city(city):
    res=db.session.query(Generator.Department, func.count(Generator.Department)).group_by(Generator.Department).filter(Generator.City == city).all()
    #将多维数组转化为字典
    res_dict={}
    for item in res:
        res_dict[item[0]]=item[1]
    return jsonify({'data':res_dict})

#按容量汇总(data),所有的容量值(cap_dist) 绘制雷达图用
@generator_blueprint.route('/count/capacity',methods=('GET','POST'))
def count_capacity():
    res = db.session.query(Generator.Capacity,func.count(Generator.Capacity)).group_by(Generator.Capacity).all()
    res_array1 = [0,0,0,0,0] #容量
    res_array2 = ['<200','200-300','300-400','400-450','450-500'] #数量 暂时手动分为五档
    for item in res:
        if item[0]<200:
            res_array1[0]+=item[1]
        elif item[0]<300:
            res_array1[1]+=item[1]
        elif item[0]<400:
            res_array1[2]+=item[1]
        elif item[0]<450:
            res_array1[3]+=item[1]
        else:
            res_array1[4]+=item[1]
    return jsonify({'data': res_array1,'cap_dist':res_array2})