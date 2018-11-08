#encoding:utf-8
from bs4 import BeautifulSoup
from flask import Blueprint, jsonify,request
from . import response
import json
import requests
import re


weather_data_blueprint = Blueprint(
    'weather_data',
    __name__,
    url_prefix="/weather_data"
)


@weather_data_blueprint.route('/rain_data',methods=('GET', 'POST'))
def rain_data():
    session = requests.Session()
    headers = {'User-Agent':'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    loginUrl = 'http://59.46.127.110/ProService/servlet/Login?param=%257B%2522loginname%2522%253A%2522zyk%2522%252C%2522passwd%2522%253A%2522zyk123%2522%257D'
    login = session.post(loginUrl,headers=headers)
    # print login.text
    boss = session.get("http://59.46.127.110/ProService/qxfw/provinceActual.jsp",headers=headers)
    soup = BeautifulSoup(boss.text, 'html.parser')
    data = soup.select('.table td')
    # print data[24].text
    index_list = [1,8,17,21,24,28,32,37,41,43,46,50,57,59]
    rain = []
    for i in index_list:
        rain.append({'city': data[i*10].text, 'one_hour': data[i*10+4].text})
    # print rain
    alert = session.get("http://59.46.127.110/ProService/qxfw/index.jsp",headers=headers)
    soup_alert = BeautifulSoup(alert.text, 'html.parser')
    pattern = re.compile(r'alert=(.*)"data":(.*)}')
    script = soup_alert.find("script", text=pattern)
    result = pattern.search(script.text).group(2)
    print result
    weather_data = [{"rain":rain},{"prevention": result}]
    return response(jsonify(weather_data))

@weather_data_blueprint.route('/rain_data_detail/<id>',methods=('GET', 'POST'))
def rain_data_detail(id):
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    loginUrl = 'http://59.46.127.110/ProService/servlet/Login?param=%257B%2522loginname%2522%253A%2522zyk%2522%252C%2522passwd%2522%253A%2522zyk123%2522%257D'
    login = session.post(loginUrl, headers=headers)
    url="http://59.46.127.110/ProService/qxfw/dialogContent.jsp?id=" + id
    rs= session.get(url, headers=headers)
    res=rs.text
    res=res.replace('./lib/jquery/jquery-1.3.2.min.js','https://cdn.bootcss.com/jquery/1.3.2/jquery.min.js')
    return res

