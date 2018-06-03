# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from lxml import etree


def DriverInto():
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    # driver = webdriver.PhantomJS('D:/ProgramFiles/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get("https://www.taobao.com/")
    time.sleep(5)
    # driver.maximize_window()
    kw = driver.find_element_by_xpath("//*[@id='q']")
    kw.send_keys("墙纸")
    kw.send_keys(Keys.ENTER)
    time.sleep(5)
    # sousuo = driver.find_element_by_xpath("//*[@id='J_TSearchForm']/div[1]/button")  # 找到搜索
    # sousuo.click()  # 点击
def PageList(driver):
    html1 = etree.HTML(driver.page_source)  # 解析当前页面
    print(type(html1))
    jiage_list = html1.xpath("//*[@id='mainsrp-itemlist']//div/div/div/div/div[1]/strong/text()")
    for jiage1 in jiage_list:
        print(jiage1)

def NextPage(driver):
    next_page = driver.find_element_by_link_text("下一页")
    # ActionChains(driver).click(next_page).perform()
    next_page.click()

def OneGood(driver):
    first_goods = driver.find_element_by_xpath("//*[@id='J_Itemlist_Pic_16563394925']")
    first_goods.click()
    handles = driver.window_handles  # 切到窗口栏
    # print(type(handles))
    driver.switch_to_window(handles[-1])  # 倒数第一个窗口
    html1 = etree.HTML(driver.page_source)  # 解析html
    first_price = html1.xpath("//*[@id='J_PromoPrice']/dd/div/span/text()")
    print(first_price)

def CloseOneDriver(driver):
    handles1 = driver.window_handles           # 浏览器窗口列表
    driver.switch_to_window(handles1[-1])  # 倒数第一个窗口
    driver.close()                         # 关闭当前

