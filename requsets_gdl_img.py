# //python3
# -*- coding: utf-8 -*-

import random
import requests
import time
from lxml import etree

agentsList = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
]
agent = random.choice(agentsList)

headers_base = {
    'Host': 'www.gandianli.com',
    'Connection': 'keep-alive',
    'User-Agent': agent,
    # 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}
path = r'C:/Users/Administrator/Desktop/111/'
print(path)


# url_one = 'http://ershou.gandianli.com/'
# response = requests.get(url_one, headers=headers_base)
def Download_more(url_More):
    response = requests.get(url_More, headers=headers_base,)
    print(response)
    # print(type(response))
    # print(response.text)
    html1 = etree.HTML(response.text)  # 解析html
    src1 = html1.xpath("//body/div[5]/div[3]/form/div[4]/div/div/a/img/@src")  # 提取列表
    print(src1)
    for srcc in src1:
        img_onePage = requests.get(srcc, headers=headers_base, verify=False)
        # print(type(srcc))
        print(srcc)
        b = ''.join(srcc.split("/")[-1:])
        name = '.'.join(b.split(".")[:2])
        # print(type(name))
        print(name)
        with open(path + name, 'wb') as f:
            f.write(img_onePage.content)
        time.sleep(2)

for index in range(1, 20):
    url_More = 'http://ershou.gandianli.com/list.php?catid=&page=' + \
               str(index) + '&price=0&thumb=0&vip=0&day=0&order=&list=1'
    Download_more(url_More)
    time.sleep(1)
    print(index)
    print(url_More)
