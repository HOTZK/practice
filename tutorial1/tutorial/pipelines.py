# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class WbtcPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, db='scrapy_58',
                                    user='root', passwd='123456', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 排空 非空返回
        if item['fangming']:
            mysql = "insert into wbtc2sf values (0,%s,%s,%s)" % (item['jiage'], item['fangming'], item['fangxing'])
            self.cursor.execute(mysql)
        return item

    def close_spider(self, spider):
        self.cursor.execute('commit')
        self.cursor.close()
        self.conn.close()




class WbtcPipeline_2(object):
    def __init__(self):
        # 新建一个 set 类型集合
        # 这是一种 元素 不重复的集合
        self.item_set = set()

    def process_item(self, item, spider):
        # 判断 数据 是否在集合中
        # 如果不在集合中
        if item['fangming'] not in self.item_set:
            # 将数据 添加到 集合中
            self.item_set.add(item['fangming'])
            if item['jiage'] not in self.item_set:
                # 将数据 添加到 集合中
                self.item_set.add(item['jiage'])
                if item['fangxing'] not in self.item_set:
                    # 将数据 添加到 集合中
                    self.item_set.add(item['fangxing'])
                    # self.item_set.add(item)
                    # 返回 item 数据
                    # with open(r'G:/python.movie/3/' + str(self.index)+'.csv', 'w', encoding='utf-8') as f:
                    #     f.write('\n'.join(self.wbtc_item)+'\n')
                    return item

