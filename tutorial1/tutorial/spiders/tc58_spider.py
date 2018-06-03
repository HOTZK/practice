# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import TCitem


class TCmoreSpider(scrapy.Spider):
    name = "wbtcmore"
    allowed_domains = ["58.com"]
    # 局部通道设置
    custom_settings = {
        'ITEM_PIPELINES': {'tutorial.pipelines.WbtcPipeline': 300},
        'ITEM_PIPELINES': {'tutorial.pipelines.WbtcPipeline_2': 200}
    }

    start_urls = ["http://szkunshan.58.com/ershoufang/?PGTID=0d100000-0001-0276-2202-f350f38767ce&ClickID=2"]
    # table2 = []
    # row2 = {}
    wbtc_item = TCitem()
    index = 2

    def parse(self, response):
        li_list = response.xpath("/html/body/div[4]/div[5]/div[1]/ul/li")  # 锁定范围
        if not li_list:
            # print(self.table2)
            return
        for li in li_list:  # 遍历 提取数据
            jiage = li.xpath(".//div[3]/p[1]/b/text()") \
                .extract()[0].strip().replace(' ', '')
            # print(type(jiage))
            wei = li.xpath(".//div[3]/p[1]/text()") \
                .extract()[1].strip().replace(' ', '')

            # if jiage and wei:
            #     self.row2['jiage'] = (jiage + wei)
            # else:
            #     self.row2['jiage'] = " "
            if jiage:
                if wei == '万':
                    self.wbtc_item['jiage'] = (jiage + '0000')
                elif wei == '亿':
                    self.wbtc_item['jiage'] = (jiage + '00000000')
                else:
                    self.wbtc_item['jiage'] = jiage
            else:
                self.wbtc_item['jiage'] = " "
            fangming = li.xpath(".//div[2]/h2/a/text()") \
                .extract()[0].strip().replace(' ', '、')
            # if fangming:
            #     self.row2['fangming'] = fangming
            # else:
            #     self.row2['fangming'] = " "
            if fangming:
                self.wbtc_item['fangming'] = fangming
            else:
                self.wbtc_item['fangming'] = " "
            fangxing = li.xpath(".//div[2]/p[1]/span[1]/text()") \
                .extract()[0].strip().replace(' ', '')
            # if fangxing:
            #     self.row2['fangxing'] = fangxing
            # else:
            #     self.row2['fangxing'] = " "
            if fangxing:
                self.wbtc_item['fangxing'] = fangxing
            else:
                self.wbtc_item['fangxing'] = " "
            # self.wbtc_item['id'] = str('0')
            # print(self.row2)
            # print(jiage+wei)
            # print(fangming)
            # print(fangxing)
            # self.table2.append(self.row2)
            # self.row2 = {} # 清空源数据
            # print(self.wbtc_item)
            yield self.wbtc_item
        # print(self.table2)
        # print(self.index)
        url = 'http://szkunshan.58.com/ershoufang/pn' + str(self.index)

        self.index += 1
        yield scrapy.Request(url, callback=self.parse)
