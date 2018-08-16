#/usr/bin/envpython
#-*-coding:UTF-8-*-
from flask import Blueprint,jsonify
from webapp.models import db,Repaircar
from sqlalchemy import func

def dataFormatter(rec):
    return {'Id':rec.Id,'Department':rec.Department,'License_num':rec.License_num,'Car_type':rec.Car_type,'Brand':rec.Brand,
            'Purchase_date':rec.Purchase_date,'Oil_type':rec.Oil_type,'Contact':rec.Contact,'Phone':rec.Phone,'City':rec.City}

repaircar_blueprint=Blueprint(
    'repaircar',
    __name__,
    url_prefix="/repaircar"
)
#返回指定城市的所有记录
@repaircar_blueprint.route('/getbyCity/<city>',methods=('GET','POST'))
def getbyCity(city):
    res = db.session.query(Repaircar).filter(Repaircar.City==city).all()
    res_list=map(dataFormatter,res)
    return jsonify({'data':res_list})
#返回总记录数
@repaircar_blueprint.route('/count',methods=('GET','POST'))
def count():
    res = db.session.query(Repaircar).count()
    return jsonify({'data':res})

#按指定类别汇总（如：/count/City按城市汇总,/count/Department按部门汇总,/count/Car_type按车型汇总,/count/Brand按车辆品牌汇总,/count/Oil_type按所使用燃油类型汇总）
@repaircar_blueprint.route('/count/<category>',methods=('GET','POST'))
def count_cat(category):
    cat = "Repaircar."+category
    res = db.session.query(eval(cat),func.count(eval(cat))).group_by(eval(cat)).all()
    #将多维数组转化为字典
    res_dict={}
    for item in res:
        res_dict[item[0]]=item[1]
    return jsonify({'data':res_dict})

## 按指定城市的部门汇总
@repaircar_blueprint.route('/count/department/<city>',methods=('GET','POST'))
def count_department(city):
    res=db.session.query(Repaircar.Department, func.count(Repaircar.Department)).group_by(Repaircar.Department).filter(Repaircar.City == city).all()
    #将多维数组转化为字典
    res_dict={}
    for item in res:
        res_dict[item[0]]=item[1]
    return jsonify({'data':res_dict})

# 按指定城市的汽车类型汇总
@repaircar_blueprint.route('/count/cartype/<city>',methods=('GET','POST'))
def count_cartype(city):
    res=db.session.query(Repaircar.Car_type, func.count(Repaircar.Car_type)).group_by(Repaircar.Car_type).filter(Repaircar.City == city).all()
    #将多维数组转化为字典
    res_dict={}
    for item in res:
        res_dict[item[0]]=item[1]
    return jsonify({'data':res_dict})

# 按指定城市的汽车油品类型汇总
@repaircar_blueprint.route('/count/oiltype/<city>',methods=('GET','POST'))
def count_oiltype(city):
    res=db.session.query(Repaircar.Oil_type, func.count(Repaircar.Oil_type)).group_by(Repaircar.Oil_type).filter(Repaircar.City == city).all()
    #将多维数组转化为字典
    res_dict={}
    for item in res:
        res_dict[item[0]]=item[1]
    return jsonify({'data':res_dict})
#返回所有城市汽车类型的分布（data），以及汽车类型列表（cartypeList）
@repaircar_blueprint.route('/count/cartype/',methods=('GET','POST'))
def count_cartype_all():
    res_dict={}
    cityList = ["沈阳","大连","鞍山","抚顺","本溪","丹东","锦州","营口","阜新","辽阳","盘锦","铁岭","朝阳","葫芦岛","省检修"]
    cartypeList={}
    for city in cityList:
        restemp=db.session.query(Repaircar.Car_type, func.count(Repaircar.Car_type)).group_by(Repaircar.Car_type).filter(Repaircar.City == city).all()
        #将多维数组转化为字典
        res_array=[]
        for item in restemp:
            res_array.append({'name':item[0],'value':item[1]})
        res_dict[city]=res_array
        res = db.session.query(Repaircar.Car_type).distinct().filter(Repaircar.City == city).all()
        newres=[]
        for t in res:
            newres.append(t[0])
        cartypeList[city]=newres
    return jsonify({'data':res_dict,'cartypeList':cartypeList})
