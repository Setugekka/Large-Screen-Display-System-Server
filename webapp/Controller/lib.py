from bs4 import BeautifulSoup
import requests

def rain_data():
    session = requests.Session()
    headers = {'User-Agent':'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    loginUrl = 'http://59.46.127.110/ProService/servlet/Login?param=%257B%2522loginname%2522%253A%2522zyk%2522%252C%2522passwd%2522%253A%2522zyk123%2522%257D'
    login = session.post(loginUrl,headers=headers)
    print login.text
    boss = session.get("http://59.46.127.110/ProService/qxfw/provinceActual.jsp",headers=headers)
    jobSoup = BeautifulSoup(boss.text, 'html.parser')
    jobPrimary = jobSoup.select('.table td')
    print jobPrimary[24].text
    index_list = [1,8,17,21,24,28,32,37,41,43,46,50,57,59]
    rain = []
    for i in index_list:
        rain.append({'city': jobPrimary[i*10].text,'1h': jobPrimary[i*10+4].text})
    print rain
    return rain
