#!/usr/bin/env python
# @Time     :2019-11-07 21:30:13   #@Author   :azhenglianxi
# @Software :PyCharm
from Selenium_auto.funtion_Interface import *
from selenium.webdriver.common.by import By
import time



# 创建一个基础页面 用于存放一些公共方法
class BasePage():
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    # 点击方法 传入元素
    def click_ele(self,locator):
        self.driver.find_element(locator[0],locator[1]).click()

    # 写入一个输入方法
    def input_text(self,locator,text):
        self.driver.find_element(locator[0],locator[1]).clear()
        self.driver.find_element(locator[0], locator[1]).send_keys(text)

    # 清楚的方法
    # def clear_input(self):
    #     pass

#具体的业务方法
class Loginpage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        # self.driver = driver
        # self.driver.implicitly_wait(10)
        # pass

    def login(self, username, password):
        # 使用配置文件进行处理
        self.driver.get('http://localhost/mgr/login/login.html')
        input(23332423)
       # self.driver.find_element_by_id('username').send_keys(username)
        self.input_text([By.ID,'username'],username)
        self.input_text([By.ID, 'password'], password)
        self.click_ele(By.CSS_SELECTOR,'.btn-success')
        #self.driver.find_element_by_id('password').send_keys(password)
      #  self.driver.find_element_by_css_selector('.btn-success').click()


class CoursePage(BasePage):

    # 初始化方法
    def __init__(self, driver):
        BasePage.__init__()
        # self.driver = driver
        # self.driver.implicitly_wait(10)

    # get网页链接的方法
    def get_curse(self):
        self.driver.get('http://localhost/mgr/ps/mgr/index.html#/')

    # 添加课程操作的方法
    def add_curse(self, name, desc, idx):
      #  self.driver.find_element_by_css_selector('[ng-click="showAddOne=true"]').click()
        self.click_ele([By.CSS_SELECTOR,'[ng-click="showAddOne=true]'])
        self.input_text([By.CSS_SELECTOR,'[ng-model="addData.name]'])
        #self.driver.find_element_by_css_selector('[ng-model="addData.name"]').clear()
        self.input_text([By.CSS_SELECTOR],'[ng-model="addData.desc]')
        #self.driver.find_element_by_css_selector('[ng-model="addData.name"]').send_keys(name)
      #  self.driver.find_element_by_css_selector('[ng-model="addData.desc"]').send_keys(desc)
        self.input_text([By.CSS_SELECTOR,'[ng-model="addData.display_idx"]'],idx)
        #self.driver.find_element_by_css_selector('[ng-model="addData.display_idx"]').send_keys(idx)
        self.click_ele([By.CSS_SELECTOR,'[ng-click="addOne()"]'])
      #  self.driver.find_element_by_css_selector('[ng-click="addOne()"]').click()

    # 删除方法
    def del_curse(self):
        self.driver.implicitly_wait(1)
        while 1:
            del_btns = self.driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
            print(del_btns)
            if del_btns == []:
                break

            del_btns[0].click()  # 去第一个元素操作
            self.driver.find_element_by_css_selector('.btn-primary').click()

        self.driver.implicitly_wait(10)

        # 退出浏览器

    def exit_chrome(self):
        input('''请输入任意数''')
        self.driver.close()
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()
        time.sleep(2)


if __name__ == '__main__':
    dirver = ChromeDriverBrowser()
    Loginpage(dirver).login('auto', 'sdfsdfsdf')
    cp = CoursePage(dirver)
    # cp.get_curse()
    cp.del_curse()  # 频繁出错  #需要处理
    cp.add_curse('shuxue课', 'wqewqe', 1)

    cp.refresh()
    cp.exit_chrome()
