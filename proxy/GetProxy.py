import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}


class GetProxy:

    # 默认爬取第1页，可选参
    def getProxy(self=None, page=1):
        print('开始获取代理')
        http = []
        for value in range(page, page + 1):
            print('正在获取第%d页ip池' % page)
            url = 'https://www.kuaidaili.com/free/inha/%d/' % value

            res = requests.get(url=url, headers=headers)

            res.encoding = 'utf-8'

            html = BeautifulSoup(res.text, 'lxml')

            req = html.select('#list table tbody tr')

            for var in req:
                ip = var.select('tr td')[0].get_text()
                port = var.select('tr td')[1].get_text()
                http.append('http://' + ip + ':' + port)
            # 防止访问过快-10
            # time.sleep(5)
        return http
