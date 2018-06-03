# -*- coding: utf-8 -*-

import random
import requests
from lxml import etree
import time


def Dles():
    agentsList = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    ]
    agent = random.choice(agentsList)

    headers_base = {
        'Host': 'www.gandianli.com',
        'Connection': 'keep-alive',
        'User-Agent': agent,
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }

    https_ip = [
        '123.161.16.20:9797',
        '163.142.44.131:9000',
        '171.116.230.163:9797',
        '182.88.130.77:9797',
    ]
    hs_ip = random.choice(https_ip)
    http_ip = [
        '171.37.178.86:9797',
        '203.174.112.13:3128',
        '123.13.244.89:9999',
        '113.200.214.164:9999',
    ]
    h_ip = random.choice(http_ip)
    Ip_ip = {
        'http': h_ip,
        'https': hs_ip,
    }

    path = r'C:/Users/Administrator/Desktop/111/'
    # print(path)
    url_one = 'http://ershou.gandianli.com/'
    # response = requests.get(url_one, headers=headers_base, proxies=Ip_ip, verify=False)
    response = requests.get(url_one, headers=headers_base, )
    # print(response.text)
    print(response)
    html1 = etree.HTML(response.text)  # 解析html文件
    # print(type(html1))
    # print(html1)
    src = html1.xpath("//body/div[5]/div[3]/form/div/div/div/div/a/text() | \
                      //body/div[5]/div[3]/form/div[4]/div/div/div/div[@class='location f_r']/text()")
    # 根据xpath规范来提取产品名,产地
    print(src)
    print(type(src))
    print(',\n'.join(src))
    src1 = ',\n'.join(src)  # 列表转字符串

    with open(path + '1.txt', 'w') as f:
        f.write(src1)
    time.sleep(2)

a = Dles()
