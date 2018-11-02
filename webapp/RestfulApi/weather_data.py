#encoding:utf-8
from bs4 import BeautifulSoup
from flask import Blueprint, jsonify,request
from . import response
import requests

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
    soup_alert = BeautifulSoup(alert.text, 'html5lib')
    data_alert =  soup_alert.find_all('script')
    # rain[1].append(data_alert)
    print data_alert
    return response(jsonify(rain))

# @weather_data_blueprint.route('/alert_data',methods=('GET', 'POST'))
# def alert_data():
#     requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
#     session = requests.Session()
#     headers = {'User-Agent':'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#     loginUrl = 'http://59.46.127.110/ProService/servlet/Login?param=%257B%2522loginname%2522%253A%2522zyk%2522%252C%2522passwd%2522%253A%2522zyk123%2522%257D'
#     login = session.post(loginUrl,headers=headers)
#     print login.text
#     boss = session.get("http://59.46.127.110/ProService/qxfw",headers=headers)
#     soup = BeautifulSoup(boss.text, 'html.parser')
#     data = soup.select('.alert table')
#     print data
#     return response(data)
