import requests
import json

s = requests.session()

def Login(url):
    data = {'email': '您的邮箱', 'password': '您的密码'} #账号和密码
    s.post(url, data=data)

def getHTMLText(url):
    r = s.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def get_json(html):
    j = json.loads(html)
    id = j['feedlist'][0]['activities'][0]['activity_id'] #获取对应"activity_id"值
    date = j['feedlist'][0]['activities'][0]['start_date_china'][:10] #获取日期
    return id, date

def Download(id, date):
    url = 'http://www.tulipsport.com/exportgpx'
    data = {'aid': id}
    r = s.post(url, data=data)
    j = json.loads(r.text)
    download_url = j['msg']
    r = s.get(download_url)
    filename = date + '.gpx'
    with open(filename, 'w') as f:
        f.write(r.text)
        f.close()

if __name__ == "__main__":
    login_url = 'http://www.tulipsport.com/login'
    url = 'http://www.tulipsport.com/getfeeds?feedtype=mine&&uid=965fadb51cb94f14d6d3257beffa9d12&&pi=1'
    Login(login_url) #登录
    html = getHTMLText(url)
    id, date = get_json(html)
    Download(id, date) #导出轨迹
