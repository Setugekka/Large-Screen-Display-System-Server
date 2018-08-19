#/usr/bin/envpython
#-*-coding:UTF-8-*-
from flask import Blueprint,jsonify
from webapp.models import db,m_urgent_material
from sqlalchemy import func
from decimal import *
def dataFormatter(x):
    return x[0]

def dataDoubleCol(x):
    return {'name':x[0],'value':str(x[1])}


def getPosition(x):
    resTemp=db.session.query(m_urgent_material.Position).distinct().filter(m_urgent_material.City==x).all()
    positionList = map(dataFormatter,resTemp)
    return positionList
def getItem(pos):
    resTemp=db.session.query(m_urgent_material.Name,m_urgent_material.Num).distinct().filter(m_urgent_material.Position==pos).all()
    itemList = map(dataDoubleCol,resTemp)

    return {'name':pos,'children':itemList}

urgentmaterial_bluprint=Blueprint(
    'urgentmaterial',
    __name__,
    url_prefix='/urgentmaterial'
)

@urgentmaterial_bluprint.route('/treedata')
def treeData():
    #
    resTemp = db.session.query(m_urgent_material.City).distinct().all()
    CityList=map(dataFormatter,resTemp)
    PositionList = map(getPosition,CityList)


    itemList = []
    for pos in PositionList:
        itemList.append(map(getItem,pos))
    urgent_material_children=[]
    for i in range(len(CityList)):
         urgent_material_children.append({'children':itemList[i],'name':CityList[i]})
    final_data = {'name':'应急物资','children':urgent_material_children}

    return jsonify({'data':final_data})